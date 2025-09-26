.. _black-list:

Black List
==========
   The Black List blocks specific IP address' from accessing the server. This is controlled through an IP List inside ViciDial called **ViciBlack**. This allows for easy administration as the firewall can be controlled from the Admin interface.

Setup
-----
   The Black List needs to be setup in the crontab first.

   .. code-block:: none
      :caption: Black List only crontab

      ### ViciBox integrated firewall, using blacklist only, check once every minute
      @reboot /usr/bin/VB-firewall --black --quiet
      * * * * * /usr/bin/VB-firewall --black --quiet

   .. code-block:: none
      :caption: Black List with VoIP BL

      ### ViciBox integrated firewall, using blacklist and VoIPBL, check VoIPBL every 6 hours and blacklist every minute
      @reboot /usr/bin/VB-firewall --black --voipbl --quiet
      0 */6 * * * /usr/bin/VB-firewall --voipbl --quiet
      * * * * * /usr/bin/VB-firewall --black --dynamic --quiet

   The IP List feature must be enabled under :menuselection:`Admin --> Settings`.

Control
-------
   The White List can be controlled through the ``ViciWhite`` IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple with one IP or CIDR network per line. Any changes made may take up to 2-minutes to apply.

   .. code-block:: none
      :caption: Sample White List entries

      157.240.14.35
      142.250.217.206
      64.233.160.0/19
      66.102.0.0/20
