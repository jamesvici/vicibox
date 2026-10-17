.. _backups:

Backups
=======

``vicibox-backup`` backs up a ViciBox server and uploads the backups to another server over FTP, FTPS or SFTP. It's meant to run every night from cron. Restoring is done with **Restore Server** in the :ref:`manager` (see :ref:`restore`).

.. list-table:: What is backed up
   :widths: 20 80
   :header-rows: 1
   :align: center

   * - Type
     - Contents
   * - database
     - Every ViciDial database, dumped with ``mydumper`` (the MariaDB system databases only with ``--system-table``)
   * - web
     - ``/etc`` (all configuration, Asterisk's included), ``/srv/www`` (the web interface and the audio store) and the crontabs
   * - dialer
     - The telephony server's voicemail and sounds, ``/usr/share/astguiclient``, ``/prompt_count.txt`` and the crontabs

The file backups are a full backup once a week (Sunday by default) and only the files changed since then on the other days. Backups can be encrypted with GPG before they leave the server.

Setup
-----
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Backups** under **Maintenance** and press :kbd:`Enter`.
#. Under **Backup server**, pick the **Protocol** (FTP, FTPS or SFTP) and fill in **Server**, **Login** and **Password**. Leave **Port** empty for the protocol's usual port. For SFTP, an **SFTP key file** can be used instead of the password.
#. To encrypt the backups, fill in either **GPG key IDs** (public keys, imported first with ``gpg --import``; keep the private keys off this server) or a **passphrase**. Write the passphrase down somewhere safe: a backup can't be restored without it.
#. Under **Options**, **MariaDB root password** is only needed if root needs a password to log in to MariaDB (on ViciBox it logs in through the socket). **Mail failures to** sends a mail when a backup fails; **Weekly full backup on** and **Compression** can usually stay as they are.
#. Under **Nightly backup**, tick **Back up every night**, set the time and tick what to back up. The choices start out matching the server's roles: **Databases** on a database server, **Configuration and web files** on a web server, **Dialer files** on a telephony server.

   .. image:: /images/vicibox13/backups.png
      :alt: The Backups screen with the backup server, encryption, options and nightly schedule
      :width: 720

#. Press **Test login** to check that the backup server accepts the login, then **Test backup**: it saves the settings and builds the backups without uploading them, with the output in the log window.
#. Press **Save** and confirm. The settings go to ``/etc/vicibox-backup.conf``, readable by root only, and the nightly run to root's crontab.

**Back up now** saves the settings and runs a backup straight away. **List backups** shows this server's backups on the backup server, newest first, to check that they arrive:

.. image:: /images/vicibox13/backups-list.png
   :alt: The list of this server's backups on the backup server, with dates, kinds and sizes
   :width: 720

From the Command Line
---------------------
The same settings can be made by editing ``/etc/vicibox-backup.conf`` (``vim /etc/vicibox-backup.conf``). It holds passwords, so it must stay owned by root with mode 0600; ``vicibox-backup`` refuses to run if anyone else can read it. Test with ``vicibox-backup --type=all --test --verbose``, and add the nightly run to root's crontab with ``crontab -e``:

.. code-block:: none

   0 3 * * * /usr/bin/vicibox-backup --type=all

Use ``--type=database``, ``--type=web`` or ``--type=dialer`` (or a comma-separated combination) to back up only some parts; ``all`` backs up all three. Uploaded backups are stored on the backup server in ``HOSTNAME/TYPE/DATE/`` directories under the login directory. The local copies are removed once they are uploaded; keeping as many old backups as you need is up to the backup server.

``vicibox-backup --help`` lists every option. Command line options override the settings in ``/etc/vicibox-backup.conf`` for a single run.

Restoring
---------
**Restore Server** reads the **[remote]** settings in ``/etc/vicibox-backup.conf`` to download a database backup from the backup server, and the **[gpg]** settings to decrypt it. On a freshly installed replacement server, copy ``/etc/vicibox-backup.conf`` back first (or fill it in again) and the restore finds the backups by itself. See :ref:`restore`.

.. note::
   Restore Server restores databases. To restore files from a web or dialer backup, download the archive from the backup server, decrypt it with ``gpg --decrypt`` if needed, and extract the files you need with ``tar``.
