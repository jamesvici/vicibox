VoIP Black List
***************
   This mode of operation downloads the `VoIP Black List <https://voipbl.org/>`_ and loads it into the firewall. This is a community submitted list that contains over 55K IP entries of known SIP abusers.

The Default
===========
   This mode of operation is the ViciBox default for new server installations. It is enabled through the the root's crontab.

   .. code-block:: none
      :caption: Default crontab entry

      ### ViciBox integrated firewall, by default just load the VoIP Black list and reload it every 4 hours
      ### You can lock everyone out of your server if you set this wrong, so understand what you are doing!!!
      @reboot /usr/bin/VB-firewall --voipbl --noblack --quiet
      0 */6 * * * /usr/bin/VB-firewall --voipbl --noblack --quiet

   To disable the VoIP Black List just comment out the last two lines above in the crontab.

   .. code-block:: none
      :caption: Commented crontab entry

      ### ViciBox integrated firewall, by default just load the VoIP Black list and reload it every 4 hours
      ### You can lock everyone out of your server if you set this wrong, so understand what you are doing!!!
      #@reboot /usr/bin/VB-firewall --voipbl --noblack --quiet
      #0 */6 * * * /usr/bin/VB-firewall --voipbl --noblack --quiet
