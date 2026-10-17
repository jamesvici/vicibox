.. _geo-block:

Geo Blocking
============

Geo blocking drops all traffic from whole countries. If your call center and carriers are all in a few countries, blocking the countries that most attacks come from cuts down on SIP scanning and brute-force attempts considerably. The country address ranges come from the APNIC delegation list and are loaded at boot.

Setup
-----
#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Firewall** and press :kbd:`Enter`.
#. Tick **Firewall on** and **Geo blocking by country**.
#. In **Blocked countries**, type the two-letter country codes to block, separated by spaces, I.E. ``CN RU``. The list is prefilled with the current setting.

   .. image:: /images/vicibox13/firewall-geoblock.png
      :alt: The Firewall screen with Geo blocking ticked and CN RU in Blocked countries
      :width: 720

#. Press **Apply** and confirm.

The countries are saved in ``/etc/vicibox-geoblock.conf`` as the ``BADCN`` setting.

.. warning::
   Don't block a country your agents, carriers or customers' phones connect from. Calls to and from numbers in a blocked country still work as long as the carrier is not in it, but a remote agent or a SIP carrier's server in a blocked country is cut off.
