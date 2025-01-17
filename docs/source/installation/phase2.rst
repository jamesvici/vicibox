Phase 2
=======
   ViciDial is installed through the ``vicibox-install`` command. This command will ask a series of questions in order to determine how to install. A ViciDial cluster will use this command when setting up new servers.
   
   An alternative to this is the mostly automated :ref:`express` install. This actually runs the same program but with pre-defined settings. It is an all-in-one approach to ViciDial that can later be turned into a cluster if need be.
   
   ViciDial is broken down into three main server roles with an optional fourth role.
      * Database server with MariaDB
      * Web server with Apache
      * Telephony server with Asterisk
      * Archive server with VSFTPd (Optional)

   Once installed ViciDial and the server's configuration will be tied to the current LAN and WAN IP. If the network environment changes then those changes will need to be made in ViciDial and the server to match. This usually happens when migrating to a new ISP or moving to a different location.

   Dimensioning, specifications, and clustering examples can be found in the :ref:`hardware` section.

   .. attention:: It highly recommended to :ref:`phase1_5-install-updates` before continuing.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   phase2/express
   phase2/cluster