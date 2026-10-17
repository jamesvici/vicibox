
.. _phase2:

Phase 2
=======

ViciDial is installed from the :ref:`manager`. Type ``vicibox`` at the **#** command prompt and pick one of the Setup actions:

* **Install Express** installs every ViciDial role on this one server, with almost no questions asked. It is the easiest option and the recommended starting point. See :ref:`express`.
* **Install Cluster** asks which roles this server will have, so the roles can be spread across several servers. See :ref:`cluster`.
* **Restore Server** rebuilds a server that was lost, from its saved settings or a database backup. See :ref:`restore`.

These actions are only available until ViciDial is installed; after that they are greyed out.

ViciDial is broken down into three main server roles with an optional fourth role:

* Database server with MariaDB
* Web server with Apache
* Telephony server with Asterisk
* Archive server with VSFTPd (Optional)

Once installed, ViciDial and the server's configuration will be tied to the current LAN and WAN IP. If the network environment changes, then those changes will need to be made in ViciDial and the server to match. This usually happens when migrating to a new ISP or moving to a different location; see :ref:`network-setup`.

Every server the manager installs records its roles, settings and ViciDial SVN revision in the database. The **Cluster** panel of the manager shows them, and **Restore Server** uses them to rebuild a server.

Dimensioning, specifications, and clustering examples can be found in the :ref:`hardware` section.

.. attention::
   It is highly recommended to set up the network (:ref:`network-setup`) and :ref:`phase1_5-install-updates` before continuing.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   phase2/express
   phase2/cluster
   phase2/restore
