.. _firewall-zones:

Zones
=====

This section explains the concept of zones in firewalld, the underlying firewall in ViciBox, and how they apply to network interfaces and traffic.

The concept of zones in firewalld is applied globally to all connections. Any network traffic received on any network interface can be moved to a specific zone if it matches a rule. The zone assigned to the network interface is only used when no other matching rule is found.

For example, even though ``eth0`` on the server has IP ``192.168.122.41/24`` and is in the **internal** zone, it's possible to have IP ``192.168.122.40`` be sent to the **external** zone if it's included on the :ref:`white-list`. Haphazardly adding IP addresses to things without understanding this concept is the biggest cause of "The whitelist/portal isn't working", "I can't access the server anymore", and other timeless classics.

The zone of each network interface, bond and VLAN is set in **Network setup** in the :ref:`manager` (see :ref:`network-setup`). New installs put the first network interface in the **public** zone.

.. list-table:: ViciBox zones
   :widths: 15 85
   :header-rows: 1
   :align: center

   * - Zone
     - Use
   * - public
     - The Internet. Anything in the public zone is available to anyone: by default SSH, the web server, Asterisk and RTP. When using the White List or Dynamic Portal, remove everything except **rtp** and **dhcpv6-client** from this zone.
   * - internal
     - A private LAN. Allows the ViciDial services plus MariaDB and FTP, which cluster servers use to talk to each other.
   * - trusted
     - A LAN where everything is allowed. Functionally equivalent to turning the firewall off for that network; there is no need to add or remove services from it.
   * - external
     - Allowed or authenticated access. The :ref:`white-list` and :ref:`dynamic-portal` add addresses to this zone. Any services you want remote or work-from-home agents to have access to need to be listed here. By default, all the services ViciDial needs are already added.
   * - drop
     - Blocked. The :ref:`black-list`, :ref:`voip-bl` and :ref:`geo-block` add addresses to this zone, and their traffic is dropped silently.

Changing Zone Services
----------------------
The services allowed in each zone are changed with ``firewall-cmd``. For example, to remove SSH from the public zone:

.. code-block:: bash

   firewall-cmd --permanent --zone=public --remove-service=ssh
   firewall-cmd --zone=public --remove-service=ssh

The first command changes the saved configuration, which applies from the next boot; the second changes the running firewall now.

.. warning::
   Don't use ``firewall-cmd --reload`` to apply a change on a telephony server. A reload rebuilds the IP block lists, and the :ref:`voip-bl` alone holds about 100,000 addresses: firewalld can take several minutes, and meanwhile it drops every connection, SSH included.

``firewall-cmd --zone=public --list-all`` shows what a zone currently allows, and ``firewall-cmd --get-active-zones`` which interfaces and sources are in which zone.
