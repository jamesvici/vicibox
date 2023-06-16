Zones
*****
   There are three zones used in the ViciBox Firewall. The services available in each zone will control access to ViciDial. It's important to remember that the concept of zones in firewalld can be applied to a network interface or a specific IP.

Public
======
   The public zone is the 'Default' zone for all interfaces. By default this zone restricts access to everything on the server except what's needed to use ViciDial.

Trusted
=======
   This zone is where the LAN network interface will need to be placed. Everything in this zone is allowed to connect to anything on the server.

External
========
   This zone is used by the White List and Dynamic Portal. All services needed to access ViciDial are in this zone.