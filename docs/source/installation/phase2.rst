Phase 2
*******
   ViciDial is installed through the ``vicibox-install`` command. This command will ask a series of questions in order to determine how to install. A ViciDial cluster will use this command when setting up new servers.
   
   An alternative is the ``vicibox-express`` command. This actually runs the same program as above but with pre-defined settings. It is an all-in-one approach to ViciDial that can later be turned into a cluster if need be. These all-in-on servers are referred to as an Express box.
   
   ViciDial is broken down into three main server roles, with an optional fourth role.
      * Database server with MariaDB
      * Web server with Apache
      * Telephony server with Asterisk
      * Archive server with VSFTPd (Optional)

   Dimensioning, specifications, and clustering examples can be found in the :ref:`hardware` section.

   Once the installation is complete the server's configuration will be tied to it's current LAN IP and WAN IP. If you decide to change either of these then ViciDial will also need to be configured to match.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   phase2/express.rst