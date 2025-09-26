
Change External IP
==================

When the external IP is changed, a few settings need to be updated in ViciBox to match. To help facilitate this, the ``vicibox-externip`` script was added. This script will attempt to auto-detect the correct external IP and insert it into Asterisk. Alternatively, you can provide the new IP to the script when you run it.

Using vicibox-externip

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-externip`` and press ``ENTER``. Alternatively, type in the IP address to use as well, e.g. ``vicibox-externip 1.2.3.4``.
#. Review the IP summary information, and press ``Y`` and press ``ENTER`` to make the change and update Asterisk.

Additional Changes

In addition to modifying the Asterisk configuration, the following items will also need to be checked and possibly adjusted:

- **External Server IP** under :menuselection:`Admin --> Servers`
- DNS entries that pointed to the old server IP
- **Sounds Web Server** under :menuselection:`Admin --> System Settings`

Screenshots
-----------

Run vicibox-externip
   .. image:: externalip-1.png
      :alt: Run vicibox-externip
      :width: 640
