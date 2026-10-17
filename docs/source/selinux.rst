.. _selinux:

SELinux
=======

openSUSE Leap 16.0 uses SELinux instead of AppArmor, and ViciBox |release| runs with SELinux **enforcing**. SELinux gives every file, port and process a label and only lets each program touch what its label allows. If Apache is ever compromised through a web page, it can't read the database files or Asterisk's configuration, even though it runs on the same server.

ViciBox sets up the labels ViciDial needs, so a standard install works without any SELinux changes. You'll only run into SELinux when you add something by hand: a directory Apache must write to, Apache on another port, a database in a non-standard place. This page shows how to recognise an SELinux problem and fix it properly.

.. warning::
   Don't turn SELinux off to "fix" a problem. Find the denial and add the missing label or setting instead; it's usually one or two commands.

What ViciBox Configures
-----------------------
.. list-table::
   :widths: 40 60
   :header-rows: 1
   :align: center

   * - Setting
     - Why
   * - ``/srv/www/htdocs`` labelled ``httpd_sys_rw_content_t``
     - ViciDial's PHP writes logs, report images and the audio store under the web root
   * - ``/srv/mysql`` labelled ``mysqld_db_t``
     - The MariaDB data directory on ViciBox
   * - TCP port 446 labelled ``http_port_t``
     - The HTTPS :ref:`dynamic-portal`
   * - ``httpd_can_network_connect`` on
     - Apache connects to the database on another server, to Asterisk and to outside services
   * - PHP's PCRE JIT turned off
     - The JIT needs memory SELinux doesn't give Apache; PHP's regular expressions run without it

.. note::
   SELinux treats ``/srv/www/htdocs`` as ``/var/www/html``. Rules for paths under the web root must be written with ``/var/www/html``; ``semanage`` refuses ``/srv/www/htdocs`` paths with an error about an "equivalency rule".

Checking SELinux
----------------
``getenforce`` shows the mode (**Enforcing**, **Permissive** or **Disabled**) and ``sestatus`` more detail. ``ls -Z`` shows the labels of files and ``ps -eZ`` those of processes:

.. code-block:: none

   vicibox13:~ # ls -Zd /srv/www/htdocs
   system_u:object_r:httpd_sys_rw_content_t:s0 /srv/www/htdocs

Finding a Denial
----------------
The typical signs of an SELinux problem are "Permission denied" errors, or an HTTP 500 error, even though the normal file permissions (``ls -l``) look right. Every blocked access is logged as an AVC denial in ``/var/log/audit/audit.log``.

.. _selinux-log:

SELinux Log in the Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **SELinux log** under **Maintenance** and press :kbd:`Enter`. The top line shows the SELinux mode.
#. Pick the **Period**: **Since boot** (the default), **Today**, **This week** or **Everything in the logs**.
#. The list shows one line per kind of denial: how often it happened, when it first and last happened, and which program (and SELinux type) was refused what on which file, directory or port, and that object's SELinux type. A program that keeps retrying shows up once, with its count.

   .. image:: /images/vicibox13/selinux-log.png
      :alt: The SELinux log with two kinds of denial: Apache refused reading the archive directory nine times, and a file once
      :width: 720

#. To narrow it down, type in **Search**: a program, a file or directory name, a path or an SELinux type, I.E. ``httpd archive``. Every word must match, in any order and in upper or lower case.
#. Press **Explain** (:kbd:`F10`) to run ``audit2why`` on the denials shown. It says what caused each one and suggests a boolean or a rule that would allow it.

   .. image:: /images/vicibox13/selinux-explain.png
      :alt: audit2why's explanation of the archive denial below the search results, with its suggested setsebool command
      :width: 720

.. warning::
   ``audit2why``'s suggestion isn't always the right fix. In the example above it suggests letting Apache read every user's home directory, while the real fix was to give the archive directory the right label. Check the suggestion against the fixes below before running it.

From the Command Line
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ausearch -m avc -ts recent

``-ts recent`` shows the last 10 minutes; use ``-ts today`` for longer. A denial looks like this:

.. code-block:: none

   type=AVC msg=audit(...): avc:  denied  { write } for  pid=3520 comm="httpd-prefork"
     name="newdir" dev="vda4" scontext=system_u:system_r:httpd_t:s0
     tcontext=unconfined_u:object_r:httpd_sys_content_t:s0 tclass=dir permissive=0

It says Apache (``httpd_t``) was refused **write** access to a directory called ``newdir`` labelled ``httpd_sys_content_t`` (read-only web content). ``audit2why`` explains denials in plain words:

.. code-block:: bash

   ausearch -m avc -ts recent | audit2why

Common Fixes
------------
**A file was moved into place and kept its old label.** ``mv`` keeps a file's label, ``cp`` gives it the label of the directory it lands in. Reset files to the labels the rules say they should have:

.. code-block:: bash

   restorecon -Rv /srv/www/htdocs/myfolder

**Apache must write to a new directory.** Label it ``httpd_sys_rw_content_t`` permanently, then apply the label. For a directory outside the web root:

.. code-block:: bash

   semanage fcontext -a -t httpd_sys_rw_content_t "/data/uploads(/.*)?"
   restorecon -Rv /data/uploads

Anything under ``/srv/www/htdocs`` is already writable for Apache on ViciBox; if a file there is not, ``restorecon`` fixes it.

**Apache must listen on another port**, for example when moving the dynamic portal (see :ref:`dynamic-portal`):

.. code-block:: bash

   semanage port -a -t http_port_t -p tcp 8446

**Apache must send email** (for example from a custom PHP page):

.. code-block:: bash

   setsebool -P httpd_can_sendmail on

``getsebool -a | grep httpd`` lists all the switches (booleans) for Apache. ``-P`` makes a change permanent.

**The MariaDB data directory moved**, for example to a separate drive at ``/data/mysql``:

.. code-block:: bash

   semanage fcontext -a -t mysqld_db_t "/data/mysql(/.*)?"
   restorecon -Rv /data/mysql

``semanage fcontext -l -C``, ``semanage port -l -C`` and ``semanage boolean -l -C`` list the local changes made on this server.

Troubleshooting with Permissive Mode
------------------------------------
To check whether SELinux is behind a problem at all, switch it to permissive mode: it then logs denials but doesn't enforce them. This lasts until the next reboot or until you switch back:

.. code-block:: bash

   setenforce 0     # permissive
   # ... try again, then look at the denials with ausearch ...
   setenforce 1     # enforcing again

If the problem goes away in permissive mode, the denials logged meanwhile show what needs a label or a boolean. Fix that, then switch back to enforcing.

.. todo::
   Check that recordings play from the web interface: ``/RECORDINGS/`` is served by Apache from ``/var/spool/asterisk/monitorDONE``, which is labelled ``asterisk_spool_t``. If Apache is denied, ViciBox needs a rule for it and this page should list it under What ViciBox Configures.
