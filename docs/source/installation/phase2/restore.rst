
.. _restore:

Restore Server
==============

**Restore Server** rebuilds a server that was lost: a failed drive, a replaced machine, or a reinstall. Start from a freshly installed ViciBox (:ref:`phase1`) and the same network settings the old server had (:ref:`network-setup`). Then pick what kind of server it was:

* **A web, telephony or archive server in a cluster.** Every server installed by the manager saves its roles and settings in the master database. The restore reads them back, so the server comes back with the same roles, SIP stack, archive server, time zone, external IP and firewall lists, without having to answer the questions again.
* **The database server, or an Express server.** The database is restored from a backup made with ``vicibox-backup`` or another dump. See :ref:`backups`.

.. warning::
   A cluster member must come back with the **same IP address** it had before, since every other server and the database refer to it by that IP. Set the IP in :ref:`network-setup` before starting the restore.

Restoring a Cluster Member
--------------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Restore Server** and press :kbd:`Enter`.
#. Select **A web, telephony or archive server in a cluster** and press **Continue**.

   .. image:: /images/vicibox13/restore-member-intro.png
      :alt: The Restore Server first screen with its two choices
      :width: 720

#. On **Restore a cluster server**, check that **IP address for ViciDial** is the one the old server had.
#. In **Master database IP**, type in the master database server's IP address, I.E. ``192.168.122.41``. If the database was installed with custom logins, enter them under **Connection settings...**.
#. Press **Look up**. The manager connects to the database and looks up the entry saved for this IP.
#. If there is no entry for this IP but there is one for this server's hostname, the manager offers to move that entry to the new IP. Only accept if the server really moved to a new address.
#. **Roles found for this server** now lists the roles and settings that were saved, and **Enable the built-in firewall** is set the way it was. To change a role's settings, such as the redirect page or the SIP stack, press **Settings...** next to it. Press **Next**.

   .. image:: /images/vicibox13/restore-member-found.png
      :alt: Restore a cluster server after Look up, with the Web server role found
      :width: 720

#. Review the summary, press **Install** and confirm with **Install**.
#. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter`.

If the IP address, the master database IP or the logins are changed after **Look up**, the roles found are cleared and **Look up** has to be pressed again.

.. _restore-audio-store:

Refilling the Audio Store
-------------------------
The first web server in a cluster holds the audio store: the sound files and prompts every telephony server downloads, including the ones uploaded through the ViciDial admin pages. The files are not in the database, so restoring that web server can't bring them all back. The restore puts Asterisk's standard sounds back into the audio store from the web server's own copy, and the end of the restore says that the uploaded prompts are still missing. Nothing in ViciDial uploads those again by itself.

The telephony servers still have their copies. To bring them back:

#. Log in as ``root`` on a telephony server, ideally the first one installed.
#. Type ``/usr/share/astguiclient/ADMIN_audio_store_sync.pl --upload`` and press :kbd:`Enter`. It uploads every sound and prompt the server has that the audio store is missing, which takes a few minutes.


.. image:: /images/vicibox13/restore-web-audio-warning.png
   :alt: The end of a web server restore, with the audio store warning
   :width: 720

The audio store's file list is under :menuselection:`Admin --> Audio Store` in ViciDial. Do this before installing or restoring any other telephony server, so that it gets the uploaded prompts too.

Servers installed with ViciBox 12 or earlier have no saved settings until they are registered with **Adopt cluster** (see :ref:`adopt-cluster`). To restore one that was never registered, start ``vicibox --debug`` and tick **Legacy mode** on the first screen to answer the role questions by hand.

Restoring the Database or an Express Server
-------------------------------------------
The restore accepts:

* a ``vicibox-backup`` database backup (``mysql-HOST-DATE.tar.xz`` or ``.tar.gz``, GPG-encrypted or not),
* a ``mysqldump`` / ``mariadb-dump`` file (``.sql``, ``.sql.gz`` or ``.sql.zst``),
* a ``mydumper`` directory.

Copy the backup to ``/root/mysql`` on the new server, or download it from the backup server during the restore.

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Restore Server** and press :kbd:`Enter`.
#. Select **The database server, or an Express server** and press **Continue**.
#. On **Restore the database server**, check **IP address for ViciDial**. If the restored database server gets a different IP than before, the database is moved to the new IP, and every other server in the cluster then has to be pointed at the new address.

   .. image:: /images/vicibox13/restore-database-backup.png
      :alt: Restore the database server with two backups listed and the firewall choices
      :width: 720

#. The backups found in **Backup directory** are listed, newest first. Pick one. To use another directory, type it in and press **Look**. To fetch a backup from the backup server set up in ``/etc/vicibox-backup.conf``, press **Download...**: the server and login are filled in from that file. Press **Connect**, pick the server that was backed up and the backup file, and press **Download**.

   .. image:: /images/vicibox13/restore-download.png
      :alt: The Download dialog connected to the backup server with a backup listed
      :width: 720


#. If the backup is GPG-encrypted, enter its passphrase. For a backup encrypted to a public key, import the private key first with ``gpg --import`` and enter the key's passphrase, if it has one.
#. **Upgrade ViciDial to the latest SVN revision after the import** is ticked when the server has internet access. Untick it to keep the ViciDial revision the backup was made with.
#. If this server already has databases with the same names as the backup, tick **Replace the existing databases that are in the backup** to overwrite them.
#. Leave **Firewall** at **As it was on this server**: the firewall is then set the way it was saved for this server in the backup, once the backup is imported. Without a saved setting it's off for a database-only server, which should be on a private network, and on otherwise. Pick **On** or **Off** to override it. See :ref:`firewall`.
#. Review the summary, press **Install** and confirm with **Install**. The backup is imported, ViciDial is installed to match it, and the server takes the roles saved in the backup.
#. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter`.

The MariaDB system databases (``mysql``, ``sys``) in a backup are skipped; the ViciDial database logins are recreated from the settings saved in the backup.

.. _resync-slave:

Resyncing a Slave Database
--------------------------
A restored database server starts its replication log over, so every slave database in the cluster stops replicating: its saved position no longer exists. The manager's main screen shows this under **Replication** in the **ViciDial** panel of the slave, as **STOPPED** with MariaDB's error 1236 (*Could not find first log file name in binary log index file*). Resync each slave after restoring the database server:

#. Log in as ``root`` on the slave database server and type ``vicibox`` to start the :ref:`manager`.
#. Select **Resync slave database** and press :kbd:`Enter`. The screen shows the primary it replicates from, the current replication state and the replication login, which it finds in the slave's own copy of the cluster's settings.

   .. image:: /images/vicibox13/resync-resync.png
      :alt: The Resync slave database screen
      :width: 720

#. Press **Resync** and confirm with **Go**.

The slave's databases are replaced with a fresh copy of the primary, and replication starts again from the point that copy ends at. Afterwards the slave's main screen shows **Replication: running from** the primary, and the cluster's history (in the **Cluster** panel) records the resync:

.. image:: /images/vicibox13/dashboard-db2-main.png
   :alt: The main screen of a slave database with Replication running and the resync in the Cluster history
   :width: 720

While the primary is being copied, its tables are locked for writing, so agents and dialing pause for as long as that takes on a large database: do it outside busy hours. The same action fixes a slave that stopped for any other reason, such as a change made on the slave directly.

Screenshots
-----------