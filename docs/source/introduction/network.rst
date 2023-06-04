Network
#######

   The network quality needed for VoIP is very different then what is needed for things like streaming or general productivity. It's most similar to the network quality needed for FPS gaming. In order of importance you will want to monitor the Packet Loss, Jitter, and Latency between you and various endpoints like your SIP Carrier. Rarely is bandwidth an issue and any sort of internet 'Speed Test' is mostly irrelevant.

   All checks should be done from where the ViciDial servers are. For the web server it's only really necessary to measure packet loss to the agents. For the telephony servers you will want to measure packet loss, jitter, and latency to your SIP Carriers. For remote work or work from home agents you will occasionally need to check their network connection as well. It's recommended to have the remote agents to run PingPlotter to check their connection to you if problems persist. Lastly, all endpoints to be monitored should respond to basic ping requests for any of this to work. If you can't ping them then you can't effectively monitor them.

   `PingPlotter <https://www.pingplotter.com/products/standard/>`__ is recommended to check for network issues. For Linux and Mac users you can also use the MyTraceRoute aka 'mtr' console application. Any examples or screenshots given in the following sections will be from PingPlotter.

   And it pains me to write this, but WiFi should never ever be used. All network connections should be wired for best results. This is usually only a problem for work at home agents.

.. toctree::
   :maxdepth: 2
    
   network/packetloss
   network/jitter
   network/latency
