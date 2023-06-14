White List
**********
   The white list allows certain IP address' through the build-in firewall. This is controlled through an IP List inside ViciDial called **ViciWhite**. This allows for easy administration as the firewall can be controlled from the Admin interface.

Deployment
==========
   The White List is only compatible with the Dynamic Portal. Below is the changes you would make to the crontab entry. The recommendation is to just delete the old entries and copy-paste these in. The crontab entries shown are for White List Only and White List with Dynamic Portal.

   .. code-block:: none
      :caption: White List only crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --white --quiet
      * * * * * /usr/bin/VB-firewall --white --quiet

   .. code-block:: none
      :caption: White List with Dynamic Portal crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --white --quiet
      * * * * * /usr/bin/VB-firewall --white --quiet