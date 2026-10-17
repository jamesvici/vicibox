.. _voip-bl:

VoIP Black List
===============

This mode of operation downloads the `VoIP Black List <https://voipbl.org/>`_ and loads it into the firewall. This is a community-submitted list that contains over 55,000 IP entries of known SIP abusers.

Default Operation
-----------------
The VoIP Black List is on by default on new telephony servers. It is reloaded at boot and every 6 hours.

To turn it on or off:

#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Firewall** and press :kbd:`Enter`.
#. Tick or untick **VoIP Blacklist (voipbl.org)**.
#. Press **Apply** and confirm.

.. note::
   The list is large. Loading it takes a little while after boot, and firewalld can take noticeably longer to restart while it is loaded.
