.. _external-ip:

Change External IP
==================

The external IP is the public internet address Asterisk puts in its SIP and SDP messages, so that phones and carriers outside the local network can reach it. It's set automatically when a telephony server is installed. When the external IP changes, for example after moving to a new ISP, it needs to be updated.

Using the Manager
-----------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **External IP** and press :kbd:`Enter`. The screen shows the external IP Asterisk uses now and the one detected for this server.
#. In **New external IP**, check the detected address or type in the IP address to use, I.E. ``203.0.113.5``.
#. Leave **Reload Asterisk SIP settings now** ticked so the change takes effect straight away.

   .. image:: /images/vicibox13/externalip.png
      :alt: The External IP screen with the chan_sip and PJSIP addresses, the detected external IP and the new IP field
      :width: 720

#. Press **Apply** and confirm.

This updates Asterisk's chan_sip and PJSIP configuration and the **External Server IP** of this server under :menuselection:`Admin --> Servers` in ViciDial.

Additional Changes
------------------
In addition to the above, the following items will also need to be checked and possibly adjusted:

- DNS entries that pointed to the old server IP
- **Sounds Web Server** under :menuselection:`Admin --> System Settings`
- Carriers and remote phones that connect to the old IP
