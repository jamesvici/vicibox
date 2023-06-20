.. _white-list:

White List
**********
   The white list allows certain IP address' through the build-in firewall. This is controlled through an IP List inside ViciDial called **ViciWhite**. This allows for easy administration as the firewall can be controlled from the Admin interface.

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

   Any IP address on the White List will be handled through the **External** zone in ``yast firewall``.


Control
=======
   The White List can be controlled through the ``ViciWhite`` IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple with one IP or CIDR network per line. Any changes made may take up to 2-minutes to apply.

   .. code-block:: none
      :caption: Sample White List entries

      157.240.14.35
      142.250.217.206
      64.233.160.0/19
      66.102.0.0/20
