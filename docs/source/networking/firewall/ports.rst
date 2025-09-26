
Ports
=====

This section describes the collection of ports that need to be exposed to agents and the internet depending on your installation.

SIP and RTP Traffic
-------------------
SIP signalling is on UDP port 5060. This is the control port and should primarily be limited to the networks, carriers, and agents that need it. If you have multiple dialers behind a firewall, this can only be forwarded to one dialer behind the firewall and that dialer will be responsible for all inbound calls. When a carrier gives you a list of IPs for their network, you want to ask them what the 'signalling' or 'SIP' IPs are. This is what you specifically want to allow in on a firewall.

RTP traffic is an ephemeral pool of ports as defined in ``/etc/asterisk/rtp.conf``. By default, this port range is UDP 10000-20000. These ports are used for audio only and should generally be open to all of the public internet. Since there is no control protocol, there is no attack vector on these ports. That, coupled with the inevitable fact that carriers, despite their best efforts, will inevitably send audio from an IP outside of their published ranges due to adding new peers and aggregates.

With multiple dialers behind a firewall, you will need to assign a unique port range to each one. The recommendation is to break up the port pool into 5000 port chunks, starting with port 10000. For example:

.. list-table:: Example RTP Port Ranges
   :widths: 15 30
   :header-rows: 1

   * - Dialer
     - UDP Port Range
   * - dialer1
     - 10000-14999
   * - dialer2
     - 15000-19999
   * - dialer3
     - 20000-24999

HTTP and HTTPS
--------------
The standard ports for HTTP is TCP 80 and for HTTPS is TCP 443. The recommendation is to set up a valid SSL certificate and force all HTTP connections to HTTPS. See the :ref:`ssl` section for more information. If you are using the web phone, then it is required that a valid SSL certificate be set up on the server.

Web Sockets
-----------
The standard port for Web Sockets (WSS) is TCP 8089. This requires a valid SSL certificate that matches the server's FQDN. Please see the :ref:`ssl` section for more information on how to install an SSL certificate. This port is a control port, so some care should be taken to restrict who has access to it. While it does not currently have the same level of vulnerability as an exposed SIP port, it will eventually.