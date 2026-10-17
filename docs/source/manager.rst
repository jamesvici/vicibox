.. _manager:

ViciBox Manager
===============

The ViciBox Manager is the administration program for ViciBox |release|. It replaces YaST, which openSUSE Leap 16.0 no longer includes, and the separate ``vicibox-*`` scripts of earlier ViciBox releases. Everything in this manual that changes the server, from setting a static IP to installing a ViciDial cluster, starts here.

Starting the Manager
--------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter`.

The manager opens on its main screen. On a new server, the first root login opens its **Welcome to ViciBox** screen instead (see :ref:`phase1`), and the main screen after that.

The manager looks and works like the text mode of YaST from earlier ViciBox releases: white on blue, with the function keys listed in the bar at the bottom. It can be run over SSH or on the server's console. Over SSH the mouse works too; on the server's own console (80x25 characters) the Actions menu leaves out the reasons why an action is greyed out, but everything works the same with the keyboard.

.. image:: /images/vicibox13/dashboard-db1-main.png
   :alt: The main screen of an Express server: System, ViciDial and Cluster panels on the left, Actions on the right
   :width: 720

The Main Screen
---------------
The left side shows the state of the server, refreshed every time you return to the main screen:

.. list-table:: Status panels
   :widths: 25 75
   :header-rows: 1
   :align: center

   * - Panel
     - Shows
   * - System
     - Hostname, IP addresses, gateway, DNS, the external IP, OS and kernel, uptime, CPU, RAM, disk, MD RAID state and time zone
   * - ViciDial
     - Whether ViciDial is installed, this server's roles, its server IP, the database it uses, the ViciDial SVN revision and database schema, the Asterisk version, on telephony servers the SIP stack and archive server, and on a slave database its replication
   * - Cluster
     - Every server in the cluster with its roles and SVN revision, and whether each one matches the database's revision; the last few cluster changes
   * - Services
     - Whether MariaDB, Apache, ViciDial, cron, the firewall and the FTP server are running and enabled at boot
   * - Security
     - Firewall state and lists, SSL certificate and its expiry, the dynamic portal
   * - Updates
     - Waiting package updates, patches and new recommended packages, and how far behind the latest ViciDial SVN revision this server is (needs internet access; it fills in a few seconds after the rest)

The right side is the **Actions** menu, in four groups: **Setup**, **Updates**, **Configuration** and **Maintenance**. Actions that don't apply to this server are greyed out and say why, for example **Install Cluster** once ViciDial is installed, or **SIP stack** on a server without the telephony role.

.. list-table:: Actions
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Action
     - Purpose
   * - Network setup
     - IP addresses, bonds, VLANs, hostname, DNS, gateway and firewall zones (:ref:`network-setup`)
   * - Install Cluster
     - Install ViciDial with the roles you pick (:ref:`cluster`)
   * - Install Express
     - Install every ViciDial role on this server (:ref:`express`)
   * - Restore Server
     - Rebuild a lost server (:ref:`restore`)
   * - Adopt cluster
     - Register a server installed with an older ViciBox so the manager can track it (:ref:`adopt-cluster`)
   * - System updates (zypper)
     - Install openSUSE package updates (:ref:`updates`)
   * - ViciDial update (SVN)
     - Update ViciDial to a newer SVN revision (:ref:`updates`)
   * - Archive server
     - Send this dialer's recordings to an archive server (:ref:`archive-server`)
   * - External IP
     - Set the public IP Asterisk uses (:ref:`external-ip`)
   * - Time zone
     - Change the server's time zone (:ref:`change-timezone`)
   * - SIP stack
     - Choose PJSIP or chan_sip on port 5060 (:ref:`sip-stack`)
   * - PJSIP and ConfBridge
     - Move a telephony server's conferences to ConfBridge and its phones and carriers to PJSIP (:ref:`convert-pjsip`)
   * - Firewall
     - Turn the firewall on or off and pick its block or allow lists (:ref:`firewall`)
   * - Dynamic portal
     - Enable the remote-agent portal (:ref:`dynamic-portal`)
   * - SSL certificate
     - Get a Let's Encrypt certificate (:ref:`ssl`)
   * - Server scrub
     - Delete the conferences, remote agents, carriers and phones of servers that are no longer in the cluster (master database only)
   * - Schema diff
     - Compare the database schema with the one ViciDial's SVN revision expects (master database only)
   * - Resync slave database
     - Copy the primary database again and restart replication, for example after the primary was restored from a backup (slave databases only, :ref:`resync-slave`)
   * - Promote to master
     - Turn a slave database into the master when the master has failed (slave databases only, :ref:`promote-slave`)
   * - Software RAID
     - The mirror's state; add the second drive or a spare, replace a failed drive, reinstall the boot loader (:ref:`mdraid-setup`). Only on servers installed from the :ref:`media-md`
   * - Backups
     - Set up vicibox-backup: backup server, encryption, nightly schedule, test and run backups, list them (:ref:`backups`)
   * - SELinux log
     - The SELinux denials from the audit log, with a search box and ``audit2why`` explanations (:ref:`selinux-log`)
   * - View logs
     - The manager's log, ViciDial's install.pl log, the SSL renewal log and the last schema diff

Keys
----
The function keys work as in YaST. The bar at the bottom of every screen lists the ones that apply there.

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Key
     - Action
   * - Arrow keys
     - Move through the Actions menu and lists. In a form, :kbd:`Down` and :kbd:`Right` move to the next field or button and :kbd:`Up` and :kbd:`Left` to the previous one, like :kbd:`Tab` and :kbd:`Shift+Tab`. In a set of choices they move between the choices first; in a text field :kbd:`Left` and :kbd:`Right` move the cursor, and :kbd:`Right` at the end of the text accepts a suggestion
   * - :kbd:`Tab`, :kbd:`Shift+Tab`
     - Move between fields, checkboxes and buttons; on the main screen, switch between the status panels (to scroll them) and the Actions menu
   * - :kbd:`Enter`
     - Run the highlighted action, press the highlighted button
   * - :kbd:`Space`
     - Tick or untick the highlighted checkbox
   * - :kbd:`F10`
     - The main button of a form: **Next**, **Apply**, **Install** and so on; **Go** in a confirmation
   * - :kbd:`F8`, :kbd:`Esc`
     - Go back one screen
   * - :kbd:`F9`
     - Abort: leave the form and go back to the main menu; **Cancel** in a confirmation. On the main menu, quit
   * - :kbd:`q`
     - Quit (main menu)
   * - :kbd:`r`
     - Refresh the main screen
   * - :kbd:`l`
     - View logs

:kbd:`Esc` never quits the manager: on the main menu it does nothing, so pressing it a few times to get back to the menu is safe.

How Tasks Work
--------------
Every action opens a form with the current settings filled in. Nothing changes until you press the button at the bottom right (**Apply**, **Install**, **Get certificate** and so on) and confirm (**Go**).

.. image:: /images/vicibox13/task-confirm.png
   :alt: The SIP stack form with its Cancel or Go confirmation
   :width: 720

The work then runs in a log window that shows every command as it runs; when it finishes, press **Back to the menu**. After installing ViciDial the log window also has **Quit**, since the next step is a reboot.

Everything the manager does is also written to ``/var/log/vicibox.log``. Changes to the server are recorded in the ViciDial database as well, so the **Cluster** panel and the cluster's history show which server was changed, when, and how.

Command Line Options
--------------------
``vicibox`` on its own opens the main screen. These options are mostly for scripting and troubleshooting:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Option
     - Effect
   * - ``--firstboot``
     - The first login setup of a new server (root's ``.bash_profile`` runs it); once it has finished, it opens the main screen
   * - ``--install``
     - Go straight to the installer
   * - ``--vicibox-express``
     - Go straight to the Express installer
   * - ``--restore``
     - Go straight to Restore Server
   * - ``--backup-dir=DIR``
     - Where Restore Server looks for database backups (default ``/root/mysql``)
   * - ``--dry-run``
     - Show what the manager would do without changing anything
   * - ``--skipexternal``
     - Don't look up the external IP while installing; the installer treats the server as offline
   * - ``--debug``
     - Show extra details, and offer legacy mode: entering the cluster details by hand, for clusters set up before ViciBox 4.0 that have no ViciBox settings in their database
   * - ``--legacy``
     - Force legacy install mode (normally detected automatically)
   * - ``--version``
     - Show the manager's version
