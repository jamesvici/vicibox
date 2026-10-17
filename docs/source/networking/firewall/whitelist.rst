.. _white-list:

ViciDial White List
===================

The ViciDial White List mode is designed to only allow known good IP addresses to connect to the server. The addresses come from the **ViciWhite** IP list in ViciDial, so static entries for things like SIP carriers, offices and other trusted sources can be managed from the ViciDial admin interface. The White List can be combined with the :ref:`dynamic-portal`, which adds remote agents as they log in.

.. warning::
   With the White List on, every address that is not on it, and not on a network in the **internal** or **trusted** zone, is locked out, including SSH. Add your own address to **ViciWhite** first.

Setup
-----
#. In ViciDial, enable the IP List feature under :menuselection:`Admin --> System Settings`.
#. Add the addresses that must always get in to the **ViciWhite** list under :menuselection:`Admin --> IP Lists` (see Control below).
#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Firewall** and press :kbd:`Enter`.
#. Tick **Firewall on** and **ViciWhite list only**. Tick **Dynamic portal logins only** as well to also allow agents who log in through the portal. The block lists are turned off, since everything not on the list is blocked anyway.

   .. image:: /images/vicibox13/firewall-whitelist.png
      :alt: The Firewall screen with the allow-only lists ticked, the block lists greyed out and the lockout warning
      :width: 720

#. Press **Apply** and confirm.
#. Remove every service from the **public** zone except **rtp** and **dhcpv6-client** (see :ref:`firewall-zones`), so that only White List addresses reach anything else.

Any IP address on the White List is handled through the **external** zone. By default, all the services needed for ViciDial are already listed in this zone.

To also allow the private address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) without listing them, add ``--addrfc1918`` to the ``VB-firewall`` lines in root's crontab (``crontab -e``).

Control
-------
The White List is controlled through the **ViciWhite** IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple, with one IP or CIDR network per line. Changes are loaded the next time ``VB-firewall`` runs, within a minute; see :ref:`firewall`.

.. code-block:: none
   :caption: Sample White List entries

   157.240.14.35
   142.250.217.206
   64.233.160.0/19
   66.102.0.0/20
