===========
Deployments
===========

Vicidial, or more specifically Asterisk, does not support a Multi-Homed ISP deployment. If true multi-network redundancy is needed then a BGP router connected to a couple ISPs with some IP space is the solution. Most colocation providers have this network redundancy built in. Asterisk can be setup to work in a sort of warm-failover with a second ISP but it can only ever use 1 ISP at a time.

LAN with NAT/firewall
---------------------
By far the most common deployment, a single IP from the ISP is used by a firewall to do Network Address Translation (NAT) for an internal LAN. The ViciDial servers will all be configured with only a LAN IP while using the Firewall IP as the default gateway. This network is fine for smaller call centers with limited inbound. While larger ViciDial installs can be ran behind a firewall just fine, care must be taken to make sure all the port forwards are setup correctly.

Common Drawbacks:

* Only one server can receive inbound SIP calls
* Only one server can provide web connections for remote agents
* Each telephony server needs a unique 5000 port UDP range
* If the Firewall has a bad day, everything has a bad day
* At best can only have 12 ViciDial telephony servers behind a NAT
* SIP is often problematic for a lot of NAT routers

LAN and WAN
-----------
In this deployment the ViciDial Web and Telephony server will be directly connected to both the LAN for agents as well as the WAN/ISP. This eliminates any potential issues with routers not handling SIP properly. The only limit to scaling is how many static IPs can be obtained.

Common Drawbacks:

* Multiple static IP's may be expensive or hard to get from your ISP
* Requires two separate switches or one that can do VLANs
* Firewall must be managed on the server itself
* Might not be allowed under corporate network security policy

WAN Only
--------
Mostly used by remote or work from home contact centers, this deployment is commonly done in a data center or colocation provider. Here the servers are only connected to the Internet. This deployment is the most complicated with a cluster as firewall rules need to be created to allow the cluster to communicate. If the IP address' are not contiguous then each server will need individual firewall rules to every other server. It's also way more likely any network changes or issue can easily result in the server being unreachable. This is a more advanced network deployment then any of the others and is not recommended if you are not experienced with Linux and networking.

Common Drawbacks:

* Multiple static IP's may be expensive or hard to get from your ISP
* Using a Data Center or Colocation Provider can be quite costly
* Firewall configuration in a cluster can get burdensome if the static IPs aren't contiguous
* Requires a bit of networking and Linux experience to handle
