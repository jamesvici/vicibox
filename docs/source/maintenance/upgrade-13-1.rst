.. _upgrade-13-1:

Upgrading to ViciBox 13.1.0
===========================

ViciBox 13.1.0 is based on openSUSE Leap 16.1. A server installed from a ViciBox 13.0.0 Beta runs on Leap 16.0 and can be upgraded in place, without reinstalling. Follow these steps on every server in the cluster.

A normal update with **System updates** in the :ref:`manager` does not do this, because the repositories on a 13.0.0 Beta server point at Leap 16.0.

.. warning::
   This upgrades **MariaDB from 11.8 to 12.3**, and the database files are converted when MariaDB restarts. It can't be undone except by restoring from a backup, so make a full backup of the database first (see :ref:`backups`). Take a snapshot as well if the server is a virtual machine.

Before You Start
----------------
* Plan a maintenance window. Log out the agents and stop dialing, since Asterisk, Apache and MariaDB all restart during the upgrade and every server needs a reboot.
* Make sure each server has at least 5 GB free on ``/``. The upgrade replaces most of the installed packages.
* Run the upgrade from the server's console or from ``screen`` or ``tmux``, so a dropped SSH connection can't interrupt it.

On a cluster, upgrade the servers in this order:

#. Any replica (slave) database servers
#. The master database server
#. The web servers, telephony servers and archive servers

Upgrade the database replicas first because a replica can be newer than its master, but shouldn't be older.

Upgrading a Server
------------------
Log in as the ``root`` user and run these commands at the **#** command prompt.

#. If you added the PHP repository from the Beta 4 announcement to a Beta 3 server, remove it. If ``zypper lr`` doesn't list it, skip this step.

   .. code-block:: console

      zypper rr devel_languages_php_php84

#. Point the ViciBox repositories at Leap 16.1. The PHP 8.4 repository that Beta 4 included is removed, because ViciBox 13.1.0 gets PHP 8.4 from the ViciBox repository. Giving that repository priority 90 keeps PHP on 8.4 rather than the newer version in Leap 16.1, which ViciBox 13.1.0 doesn't use.

   .. code-block:: console

      cd /etc/zypp/repos.d
      for f in openSUSE-Leap-16_0-*.repo; do sed -i 's/16_0/16_1/g; s#/16\.0/#/16.1/#g' "$f"; mv "$f" "${f/16_0/16_1}"; done
      rm -f openSUSE-Leap-16_1-Devel-Lang-PHP84.repo
      zypper mr -p 90 openSUSE-Leap-16_1-ViciDial-ViciBox
      cd

#. Refresh the repositories. If asked whether to trust a repository's signing key, answer ``a`` for always.

   .. code-block:: console

      zypper ref

#. Run the upgrade and answer ``y`` to the list of changes. It downloads every package first, then installs them.

   .. code-block:: console

      zypper dup --allow-vendor-change --download-in-advance

   The list will be long, around 1,600 packages. Two parts of it can look alarming but are expected:

   * **Downgrades**: some packages, Python among them, may be slightly older in Leap 16.1 than the latest Leap 16.0 update.
   * **Removals**: ``dahdi-linux-kmp-default`` is listed as removed because a new version built for the Leap 16.1 kernel replaces it, and ``python3-firewall`` is replaced by ``python313-firewall``.

   MariaDB upgrades its own system tables when it restarts during this step. It shows as ``activating`` while that runs, which can take a minute or more on a large database. Don't interrupt it.

#. Record the new version, so that the login screen and :ref:`bug fixes <bugfix-errata>` show the right one, then reboot.

   .. code-block:: console

      sed -i '1i - ViciBox v.13.1.0' /etc/vicibox-version
      reboot

Checking the Upgrade
--------------------
After the reboot, log in as ``root`` and check that the server is on Leap 16.1 and has the expected versions:

.. code-block:: console

   grep PRETTY_NAME /etc/os-release
   head -1 /etc/vicibox-version
   php -v | head -1
   mariadb --version
   systemctl --failed

* ``PRETTY_NAME`` shows **openSUSE Leap 16.1**.
* The first line of ``/etc/vicibox-version`` shows **ViciBox v.13.1.0**.
* PHP is **8.4.27** or later. It should not be 8.5.
* MariaDB is **12.3**.
* ``systemctl --failed`` lists no failed services.

On a telephony server, also check that the DAHDI modules loaded. This should print at least one line:

.. code-block:: console

   lsmod | grep dahdi

Once every server is upgraded, start the :ref:`manager` with ``vicibox`` and look over the **Cluster** panel, then place a test call before letting agents back in. ViciDial itself isn't changed by this upgrade, so no SVN update is needed.

.. note::
   If you changed ``/etc/postfix/main.cf`` or ``master.cf``, the upgrade leaves your files in place and saves the new defaults next to them as ``.rpmnew``. Your configuration keeps working. You can delete the ``.rpmnew`` files once you've looked them over.
