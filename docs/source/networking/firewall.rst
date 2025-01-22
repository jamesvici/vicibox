=========
Firewall
=========

ViciBox uses firewalld for its firewall. The firewall is configured through different operational modes that can be combined together. Each mode is designed to handle specific use cases that come up in a VoIP environment.

By default ViciBox is configured to use the VoIP Black List mode of operation. This mode downloads and maintains a list of known SIP abusers. While effective, it's important to understand what the firewall is doing and how to configure it properly.

SIP and RTP Traffic
-------------------
Signalling on UDP Port 5060 will only come from a few Carrier IPs, the RTP audio port can and often does come from IP's outside of the carrier's normal footprint. This is done to minimize any delay between the audio endpoints aka the agent and the caller.

.. attention:: 
   There is a known issue between the default VoIP Black List mode of operation and firewalld. The problem is that the size (50K+ entries) of the list can cause firewalld to enter a race condition. This most commonly happens after making network changes in ``yast lan``. The recommended action is to stop firewalld with ``service firewalld stop``, make any needed network changes, then ``reboot`` to cleanly load the list back in. If the VoIP Black List is not needed then just disable it. While this is not ideal it is better then nothing at all.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   firewall/zones
   firewall/whitelist
   firewall/blacklist
   firewall/dynamic
   firewall/voipbl