.. _white-list:

==================
ViciDial Whitelist
==================

The ViciDial White List mode is designed to only allow known good IP addresses to connect to the server. This is accomplished by integrating with the ViciDial Remote Agent interface to dynamically allow connections from agents as they connect. This mode also allows for static entries to be added for things like SIP carriers and other trusted sources.

Configuration Steps
-------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt
#. Type ``vicibox-firewall`` and press ``ENTER``
#. Using the arrow keys, select **ViciDial White List** and press ``ENTER``
#. Type ``Y`` and press ``ENTER`` to confirm the change
#. Review the output to ensure the change was successful

Static Entries
--------------
Static entries can be added to the white list by editing the ``/etc/firewalld/whitelist.conf`` file. Each entry should be on its own line and can be either an IP address or a network in CIDR notation.

Example whitelist.conf:
* 192.168.1.0/24
* 10.0.0.0/8
* 1.2.3.4

Setup
=====
   The White List is only compatible with the Dynamic Portal. Below are the changes you would make to the ViciBox crontab entry. The recommendation is to just delete the old entries and copy-paste these in. The crontab entries shown are for White List Only and White List with Dynamic Portal.

   .. code-block:: none
      :caption: White List only crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --white --quiet
      * * * * * /usr/bin/VB-firewall --white --quiet

   .. code-block:: none
      :caption: White List with Dynamic Portal crontab

      ### ViciBox integrated firewall, using whitelist and dynamic portal, and check once every minute
      @reboot /usr/bin/VB-firewall --white --dynamic --quiet
      * * * * * /usr/bin/VB-firewall --white --dynamic --quiet

   The IP List feature must be enabled under :menuselection:`Admin --> Settings`.

   All services under the **Public** zone should be removed except **dhcpv6-client** and **rtp**.

   Any IP address on the White List will be handled through the **External** zone in ``yast firewall``. By default all the services needed for ViciDial are already listed in this zone.

Control
=======
   The White List can be controlled through the ``ViciWhite`` IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple with one IP or CIDR network per line. Any changes made may take up to 2-minutes to apply.

   .. code-block:: none
      :caption: Sample White List entries

      157.240.14.35
      142.250.217.206
      64.233.160.0/19
      66.102.0.0/20
