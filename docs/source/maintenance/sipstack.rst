.. _sip-stack:

SIP Stack
=========

Asterisk has two SIP stacks: PJSIP, the current one, and chan_sip, the older one that earlier ViciBox releases used. ViciDial supports both, and both run at the same time: one answers on the standard SIP port, UDP 5060, and the other on UDP 5061. New ViciBox |release| telephony servers use PJSIP on 5060.

Phones and carriers are set up in ViciDial for one stack or the other. The one on 5060 is the one carriers and phones reach without specifying a port.

Changing the SIP Stack
----------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`. The **ViciDial** panel shows the current SIP stack.
#. Select **SIP stack** and press :kbd:`Enter`.
#. Pick **PJSIP on 5060 (recommended)** or **chan_sip on 5060**.
#. Leave **Restart Asterisk when calls finish** ticked. Asterisk needs a restart to move the stacks to their new ports; it waits until no calls are active.

   .. image:: /images/vicibox13/sipstack.png
      :alt: The SIP stack screen with the PJSIP and chan_sip choices
      :width: 720

#. Press **Apply** and confirm.

Update the port on carriers and phones that should keep using the other stack.

.. _convert-pjsip:

Moving to PJSIP and ConfBridge
------------------------------
Servers installed with ViciBox 12 or older usually run their phones and carriers on chan_sip and their conferences on MeetMe. ViciDial prefers PJSIP and ConfBridge, and **PJSIP and ConfBridge** in the :ref:`manager` moves a telephony server over:

* **ConfBridge conferences instead of MeetMe**: the server's conference engine and its 300 ConfBridge rooms.
* **Phones on this server to PJSIP**: the phones keep their extension and password; ViciDial writes their PJSIP accounts from the same settings. Phones with a **Conf Override** or a template, and webphones, are left on SIP and listed, to change by hand in ViciDial.
* **SIP carriers to PJSIP**: each active SIP carrier of this server (or of all servers) is copied to a new PJSIP carrier named after it with ``_PJ`` added, I.E. ``MYTRUNK_PJ``. Its account entry, registration, globals and dialplan are rewritten for PJSIP, the copy is made active and the SIP original inactive. Going back is making the original active again in ViciDial. A carrier that can't be converted with certainty is copied inactive, with the parts to check listed.

When phones or carriers move to PJSIP, it also makes PJSIP the stack on port 5060 and lets ViciDial's **Allowed SIP Stacks** include PJSIP. ConfBridge on its own leaves the SIP stack as it is.

#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **PJSIP and ConfBridge** and press :kbd:`Enter`. The screen reads the server's phones and carriers and lists what will change.
#. Tick what to convert. Carriers are left unticked: check the list first.

   .. image:: /images/vicibox13/convert.png
      :alt: The PJSIP and ConfBridge screen with a MeetMe server, one SIP phone and one SIP carrier that converts cleanly
      :width: 720

#. Leave **Restart Asterisk when calls finish** ticked and press **Convert**, then confirm.

ViciDial rewrites the Asterisk configuration within a minute. Phones register on port 5060 as before. Carriers that sent calls to the server's port 5060 keep working; a carrier that was set up to reach chan_sip on 5061 needs its provider told about the change.

