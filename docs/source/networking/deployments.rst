Deployments
###########
   Vicidial, or more specifically Asterisk, does not support a Multi-Homed ISP deployment. If true network redundancy is needed then a BGP router with some IP space or a data center is the solution. Asterisk can be setup to work in a sort of warm-failover with a second ISP but it can only ever user 1 ISP at a time.

LAN with NAT/firewall
*********************
   By far the most common deployment, a single IP from the ISP is used by a firewall to do Network Address Translation (NAT) for a LAN. The ViciDial servers will all be configured with only a LAN IP while using the Firewall IP as the default gateway. This network is fine for smaller call centers with limited inbound. While larger ViciDial installs can be ran behind a firewall just fine, care must be taken to make sure all the port forwards are setup correctly.

   Common Drawbacks
      * Only one server can receive inbound SIP calls
      * Only one server can provide web connections for remote agents
      * Each telephony server needs a unique 5000 port UDP range
      * If the Firewall has a bad day, everything has a bad day

   .. blockdiag::
      :align: center

      blockdiag {
         WAN <-> Firewall <-> LAN;
      }
   
   