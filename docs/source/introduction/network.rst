
Network
=======

The network quality needed for VoIP is very different than what is needed for things like streaming or general productivity. It's most similar to the network quality needed for FPS gaming. In order of importance, you will want to monitor the Packet Loss, Jitter, and Latency between you and various endpoints like your SIP Carrier. Rarely is bandwidth solely the issue, and any sort of internet 'Speed Test' will generally not help.

All checks should be done from the servers themselves or from a host on the same physical network as the servers. Unfortunately, the quality of the internet varies with every hop, which can be problematic with work-from-home agents and SIP carriers. It's not uncommon to end up with an agent or carrier in New York who can connect to your server in Tampa just fine, while another agent or carrier in Los Angeles might be having issues. The internet is a fickle beast kept running with zip ties and extension cords while a chunk of pallet is used to keep the door shut and a trash bag for weather-proofing. Those from the telco world will get that joke. The rest of you will just have to learn it the hard way.

`PingPlotter <https://www.pingplotter.com/products/standard/>`__ is recommended to check for network issues. For Linux and Mac users, you can also use the MyTraceRoute aka 'mtr' console application. Any examples or screenshots given in the following sections will be from PingPlotter.

And it pains me to write this, but WiFi should never ever be used for anything. All network connections should be wired. This is usually only a problem for work-from-home agents. My suggestion is to just buy them a very long cable.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   network/packetloss
   network/jitter
   network/latency
