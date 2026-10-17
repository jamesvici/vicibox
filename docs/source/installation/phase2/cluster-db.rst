
Database
========

Follow these steps to install and configure the database server for a ViciDial cluster:

   #. If not already, log in as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
   #. Select **Install Cluster** and press :kbd:`Enter`. The manager checks the server for a few seconds, then shows what it found: hostname, IP addresses, Asterisk and ViciDial versions. If the network is not set up yet, press **Network setup first...**; otherwise press **Continue**.

      .. image:: /images/vicibox13/install-intro.png
         :alt: The first Install Cluster screen with what was detected on the server
         :width: 720

   #. On **Server setup**, check that **IP address for ViciDial** is this server's LAN address, I.E. ``192.168.122.41``.
   #. Under **Server roles**, tick **Database** and leave the other roles unticked. The note next to it reads **primary database, default logins**.
   #. Under **Firewall**, **Enable the built-in firewall** is unticked for a dedicated database server, which is expected to sit on a private network. Leave it that way unless the server can be reached from the internet.

      .. image:: /images/vicibox13/install-setup-database.png
         :alt: Server setup with only the Database role ticked
         :width: 720

   #. Press **Next**, review the summary, press **Install** and confirm with **Install**.
   #. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter` to reboot and cleanly load ViciDial.
   #. Log in as the ``root`` user and type ``vicibox`` to start the manager. The **Services** panel should show **mariadb** and **vicidial** as active, and the **Cluster** panel lists **DB1** as the master database.

   This will create an entry under :menuselection:`Admin --> Servers` called **DB1**. Do not delete this entry as it's needed for ViciDial to function properly.

Database Settings
-----------------
**Settings...** next to **Database** chooses between a primary and a slave database, and the ViciDial database logins. Leave **Use the default ViciDial database settings** ticked unless you need your own database name, logins and passwords; every other server in the cluster then needs the same settings, under **Connection settings...** on its own Server setup page.

.. image:: /images/vicibox13/install-settings-database.png
   :alt: The Database settings page with the primary and slave choices
   :width: 720

Each Settings page has **OK** (:kbd:`F10`) and **Cancel** (:kbd:`F8` or :kbd:`Esc`); Cancel leaves the settings as they were.

.. _slave-database:

Slave Database
--------------
A slave (replica) database keeps a live copy of the primary, for reports and as a standby. Install it after the primary database:

#. Start **Install Cluster** on the slave's server and press **Continue**.
#. On **Server setup**, tick **Database**, press **Settings...** next to it, select **Slave database (a copy that replicates from the primary)** and press **OK**.
#. A **Master database** section appears: type in the primary database's IP address in **Master database IP**, I.E. ``192.168.122.41``.
#. Press **Next**. The manager connects to the primary and picks the slave's MySQL server ID by itself.
#. Review the summary, press **Install** and confirm with **Install**. The primary's databases are copied to the slave, and replication starts.

On the slave, the **ViciDial** panel of the main screen shows **Replication**: **running from** the primary in green, or **STOPPED** with MariaDB's error in red. If replication stops, for example after the primary was restored from a backup, use **Resync slave database** (see :ref:`resync-slave`).

The slave has the same ViciDial database logins as the primary, so it can take over if the primary fails.

.. _promote-slave:

Promoting the Slave
-------------------
If the primary database fails for good, **Promote to master** turns the slave into the new primary. It takes over the primary's IP address, next to its own, so the web and telephony servers carry on without any changes. It stops replicating, becomes MariaDB server-id 1 as the primary was, and gets the primary's ViciDial cron jobs. What the slave had already received from the primary is applied first, so nothing it had is lost.

#. Make sure the old primary is off: powered down or disconnected from the network. Promote to master refuses while the old primary still answers on its database port or to ping.
#. On the slave, log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Promote to master** under **Maintenance** and press :kbd:`Enter`. The screen shows the slave, the primary and the replication state.

   .. image:: /images/vicibox13/promote-blocked.png
      :alt: Promote to master refusing because the old primary still answers on port 3306
      :width: 720

#. Tick **The old master is powered off or disconnected, and won't come back with its IP address**, press **Promote** and confirm.

.. warning::
   The old primary must not come back on the network with its IP address: there would be two servers on one address and two primaries. Reinstall it, then add it back as a slave of the new primary with **Install Cluster**.
