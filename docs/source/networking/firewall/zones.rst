
Zones
=====

This section explains the concept of zones in firewalld, the underlying firewall in ViciBox, and how they apply to network interfaces and traffic.

The concept of zones in firewalld is applied globally to all connections. Any network traffic received on any network interface can be moved to a specific zone if it matches a rule. The default zone assigned to the network interface is only used when no other matching rule is found.

For example, even though ``eth0`` on the server has IP ``192.168.50.4/24`` and is in the **Trusted** zone by default, it's possible to have IP ``192.168.50.40`` be sent to the **External** zone if it's included on the :ref:`white-list`. Haphazardly adding IP addresses to things without understanding this concept is the biggest cause of "The whitelist/portal isn't working", "I can't access the server anymore", and other timeless classics.

Public
------
This is the public zone, also known as the Internet. Anything attached or in the public zone will be available to anyone. In general, the RTP ports will be publicly available along with potentially the HTTPS web server.

Trusted
-------
This zone is where the LAN network interface should be placed. Everything in this zone is allowed to connect to anything on the server. There is no need to add or remove services from this zone as it allows everything by default. It is functionally equivalent to turning the firewall completely off.

External
--------
This zone is for allowed or authenticated access. The :ref:`white-list` and :ref:`dynamic-portal` will assign IP addresses to this zone. Any services you want remote or work-from-home agents to have access to will need to be listed in this zone. By default, all needed services for ViciDial are already added.