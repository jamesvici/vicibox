.. _whats-new:

What's New
==========

What's New in 13.1
------------------
ViciBox v.13.1.0 Beta 6 is the current test release. ViciBox has moved to openSUSE Leap 16.1, so v.13.1.0 replaces v.13.0.0, which will not be released as a final version. Servers installed from a ViciBox 13.0.0 Beta can be upgraded in place; see :ref:`upgrade-13-1`.

* **openSUSE Leap 16.1** with kernel 6.12 replaces Leap 16.0.
* **MariaDB 12.3** replaces MariaDB 11.8.
* **PHP stays on 8.4**. Leap 16.1 moves to PHP 8.5, so ViciBox pins PHP 8.4 from its own repository. It starts at 8.4.27, which has the php2shell fix.
* **Package repositories** now point at Leap 16.1, including the Asterisk, DAHDI and ViciBox packages.
* **SELinux Perl helper labels**: Perl scripts in the web root (such as ``sheet2tab.pl`` for spreadsheet lead loading and ``bp.pl`` for password hashing) are labeled ``bin_t`` so Apache can execute them under enforcing SELinux.

What's New in 13.0
------------------
ViciBox v.13.0 moves to openSUSE Leap 16.0. Leap 16.0 is a big change from the 15.x releases ViciBox 11 and 12 were built on, and ViciBox changed with it. If you have installed an earlier ViciBox, read this page first: several familiar commands are gone.

YaST is gone: meet the ViciBox Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
openSUSE Leap 16.0 no longer ships YaST, so ``yast lan``, ``yast firewall`` and the other YaST modules are not available. In their place ViciBox comes with the :ref:`manager`, a full-screen administration program you start by typing ``vicibox``. It shows the state of the server and the ViciDial cluster at a glance and runs every ViciBox task from one menu:

.. list-table:: Old commands and their replacement
   :widths: 40 60
   :header-rows: 1
   :align: center

   * - ViciBox 12 and older
     - ViciBox |release|
   * - ``yast lan``
     - **Network setup** (:ref:`network-setup`)
   * - ``vicibox-install``
     - **Install Cluster** (:ref:`cluster`)
   * - ``vicibox-express``
     - **Install Express** (:ref:`express`)
   * - ``yast firewall``, editing the VB-firewall crontab
     - **Firewall** (:ref:`firewall`)
   * - ``vicibox-ssl``
     - **SSL certificate** (:ref:`ssl`)
   * - ``vicibox-timezone``
     - **Time zone** (:ref:`change-timezone`)
   * - ``vicibox-externip``
     - **External IP** (:ref:`external-ip`)
   * - ``vicibox-mdraid1``
     - **Software RAID** (:ref:`mdraid-setup`), which also replaces failed drives
   * - ``zypper up``, ``vici-getsvn``
     - **System updates** and **ViciDial update** (:ref:`updates`)

New in the manager, with no equivalent before:

* **Restore Server** rebuilds a lost server, either a cluster member from its saved settings or the database from a backup. See :ref:`restore`.
* **Cluster tracking**: every server records its roles, settings and ViciDial SVN revision in the database, so the manager can show the whole cluster and warn when a server is not on the same revision as the database.
* **Network setup** handles bonds, VLANs, static routes and firewall zones, and rolls a change back automatically if it cuts off your connection.
* **First boot setup**: the first root login asks for language, keyboard, time zone and root password, then the manager's **Welcome to ViciBox** screen sets up the network, installs updates and mirrors the system onto the second drive in one go. See :ref:`phase1`.

The manager looks and works like the YaST text mode it replaces: the same colours, and the same function keys (:kbd:`F10` Next, :kbd:`F8` Back, :kbd:`F9` Abort).

SELinux
~~~~~~~
SELinux is enabled and enforcing by default on Leap 16.0, replacing AppArmor. ViciBox sets up the SELinux labels ViciDial needs, but anything you add by hand, such as files in a new directory served by Apache or a service on a non-standard port, may need a label too. See :ref:`selinux`.

Other changes
~~~~~~~~~~~~~
* **NetworkManager** replaces wicked for network configuration.
* **PJSIP** is the default SIP stack on new telephony servers. chan_sip is still available; see :ref:`sip-stack`.
* **ConfBridge** replaces MeetMe as the conferencing engine on new telephony servers, using Asterisk's DAHDI timing. Restored servers keep the engine they had; it can be changed per server under :menuselection:`Admin --> Servers` (**Conferencing Engine**).
* **ip_relay** is replaced by three small ``ip-relay@`` system services built on socat, set up automatically on telephony servers.
* The **G729 and G723 codecs** are installed automatically on telephony servers.
* **Backups** are made with ``vicibox-backup``, and the manager can restore them. See :ref:`backups`.
* **Geo blocking**: the firewall can block whole countries. See :ref:`geo-block`.
* **Swap is a file**: the Standard and MD RAID images have no swap partition. A 4 GB ``/swapfile`` is created at the first boot; on MD RAID it lives on the mirror, so swap is mirrored too.
* **Cockpit**, the web console, is included but off by default. See :ref:`cockpit`.
