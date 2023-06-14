Firewall
########
   The ViciBox Firewall is an integration with firewalld in the underlying OS. It offers multiple modes of operation with some modes integrated directly within ViciDial as well.

   ViciBox Firewall modes
      * VoIP Black List (default)
      * ViciDial White List
      * ViciDial Black List
      * Dynamic Portal integration
      * Geo Blocking

   If the ViciDial servers are already behind a network firewall then it's recommended to disable the built-in firewalld through ``yast firewall``.

   Since there is no way to acoomodate all networks enviroments the default firewall configuration allows all connections needed for ViciDial. These would be the SIP telephony port, the HTTP and HTTPS web ports, the RTP audio ports, and the SSH port. With the exception of the RTP audio ports, It is recommended to limit accessibility to these ports where possible.
   
   The RTP audio ports should remain accessible from all networks, including the public Internet. While the SIP Signalling on UDP Port 5060 will only come from a few Carrier IPs, the RTP audio port can and often does come from IP's outside of the carrier's normal footprint. This is done to minimize any delay between the audio endpoints aka the agent and the caller.

   .. attention:: There is a known issue between the default VoIP Black List mode of operation and firewalld. The problem is that the size (50K+ entries) of the list can cause firewalld to enter a race condition. This most commonly happens after making network changes changes in ``yast lan``. The recommended action is to stop firewalld through ``service firewalld stop``, make any needed network changes, then ``reboot`` to cleanly load the list back in. If the VoIP Black List is not needed then just disable it. While this is not ideal it is better then nothing at all.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   firewall/voipbl
   firewall/whitelist
   firewall/howto
   