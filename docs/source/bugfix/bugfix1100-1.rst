
ViciBox 11.0.0 AGI Module Bug
=============================

This bug affects ViciBox v.11.0.0 installations where the res_agi.so module fails to load due to an outdated modules.conf file. The ``res_speech.so`` module is required for ``res_agi.so`` to load, but the packaged configuration prevents this, causing ViciDial to malfunction. Removing the ``noload => res_speech.so`` line from ``/etc/asterisk/modules.conf`` and rebooting resolves the issue.

.. note::
   This fix is only needed for servers already installed with ViciBox v.11.0.0. If you ran ``zypper up`` before ``vicibox-install``, you do not need to apply this fix.

Symptoms
--------

Telephony servers with this issue will show log output stating that no application can be found for the AGI extension.

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

To resolve this issue, follow these steps:

   #. Log in as the ``root`` user to access the ``#`` command prompt.
   #. Run the following command to comment out the problematic line:

      .. code-block:: bash

         sed -i 's/^noload => res_speech.so/;noload => res_speech.so/' /etc/asterisk/modules.conf

   #. Reboot the server:

      .. code-block:: bash

         reboot

      Alternatively, you can restart Asterisk without rebooting:

      .. code-block:: bash

         asterisk -rx "core restart now"


