=================
11.0.0 AGI module
=================
   The res_speech.so module is needed for the res_agi.so module to load which ViciDial requires. An old modules.conf was inadvertently packaged with ViciBox v.11.0.0 which prevents res_speech.so from loading which further prevents res_agi.so from loading as well. Removing the ``noload => res_speech.so`` from ``/etc/asterisk/modules.conf`` and rebooting will fix things.

   The fix should only be ran on servers that have already been installed. If ``zypper up`` was ran before ``vicibox-install`` was there should be no need to run the below fix.

Symptoms
--------
   Telephony servers with this issue will have log output stating that no application can be found for the AGI extension.

   .. code-block:: none
      :caption: Example Log Output

      [Jun 28 12:47:30] == Using SIP RTP CoS mark 5
      [Jun 28 12:47:30] > 0x7fd550024340 -- Strict RTP learning after remote address set to: 192.168.1.106:12722
      [Jun 28 12:47:30] WARNING[25228][C-00000006]: pbx.c:2928 pbx_extension_helper: No application 'AGI' for extension (defaultlog, 9684, 1)
      [Jun 28 12:47:30] == Spawn extension (defaultlog, 9684, 1) exited non-zero on 'SIP/145-00000008'
      [Jun 28 12:47:30] WARNING[25228][C-00000006]: pbx.c:2928 pbx_extension_helper: No application 'AGI' for extension (defaultlog, h, 1)
      [Jun 28 12:47:30] == Spawn extension (defaultlog, h, 1) exited non-zero on 'SIP/145-00000008'

The Fix
-------
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type the command ``sed -i 's/^noload => res_speech.so/;noload => res_speech.so/' /etc/asterisk/modules.conf`` and press ``ENTER``.
   #. Reboot the server by typing ``reboot`` and pressing ``ENTER`` or restart asterisk by running ``asterisk -rx "core restart now"``.


