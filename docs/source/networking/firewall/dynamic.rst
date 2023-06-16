Dynamic Portal
**************
   The dynamic portal allows for remote or work-from-home agents to authenticate with their ViciDial logins on a separate web portal. This portal is standalone outside the framework of ViciDial and restricts how fast authentication attempts can be made. It allows agents to dynamically add their IP to the firewall for ViciDial.

Setup
=====
   The dynamic portal is only compatible with the White List and is often ran in conjunction with it.

   .. code-block:: none
      :caption: Dynamic Portal only crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --dynamic --quiet
      * * * * * /usr/bin/VB-firewall --white --quiet

   .. code-block:: none
      :caption: White List with Dynamic Portal crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --white --dynamic --quiet
      * * * * * /usr/bin/VB-firewall --white --dynamic --quiet

   

Control
=======
   The White List can be controlled through the ``ViciWhite`` IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple with one IP or CIDR network per line. Any changes made may take up to 2-minutes to apply.
