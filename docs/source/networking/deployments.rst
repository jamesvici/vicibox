
Deployments
===========

This section describes common network deployment scenarios for ViciBox and their typical considerations.

LAN and WAN
-----------
In this deployment, the ViciDial Web and Telephony server is directly connected to both the LAN for agents and the WAN/ISP. This eliminates potential issues with routers not handling SIP properly. The only limit to scaling is how many static IPs can be obtained.

**Common Drawbacks:**

- Multiple static IPs may be expensive or hard to get from your ISP
- Requires two separate switches or one that can do VLANs
- Firewall must be managed on the server itself
- Might not be allowed under corporate network security policy

WAN Only
--------
Mostly used by remote or work-from-home contact centers, this deployment is commonly done in a data center or colocation provider. Here, the servers are only connected to the Internet. This deployment is the most complicated with a cluster, as firewall rules need to be created to allow the cluster to communicate. If the IP addresses are not contiguous, then each server will need individual firewall rules to every other server. It is also much more likely that any network changes or issues can easily result in the server being unreachable. This is a more advanced network deployment than any of the others and is not recommended if you are not experienced with Linux and networking.

**Common Drawbacks:**

- Multiple static IPs may be expensive or hard to get from your ISP
- Using a data center or colocation provider can be quite costly
- Firewall configuration in a cluster can get burdensome if the static IPs aren't contiguous
- Requires a bit of networking and Linux experience to handle
