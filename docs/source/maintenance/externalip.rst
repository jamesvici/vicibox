Change External IP
******************
   Whenever the external IP is changed a few settings need to be changed in ViciBox to match. To help facilitate that the ``vicibox-externip`` script was added. This script will attempt to auto-detect the correct external IP and insert that into Asterisk. Alternatively, you can provide the new IP to the script when you run it.

vicibox-externip
================
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox-externip`` and press ``ENTER``. Alternatively, type in the IP address to use as well, I.E. ``vicibox-externip 1.2.3.4``
   #. Review the IP summary information, and press ``Y`` and press ``ENTER`` to make the change and update asterisk.

Other Change
============
   In addition to modifying the asterisk configuration, the following items will also need to be checked and possibly adjusted.

   Items to check
      * **External Server IP** under :menuselection:`Admin --> Servers`
      * DNS entries that pointed to the old server IP
      * **Sounds Web Server** under :menuselection:`Admin --> System Settings`
