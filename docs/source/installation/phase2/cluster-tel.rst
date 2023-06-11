Telephony
---------
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox-install`` and press ``ENTER`` to start the ViciBox installer.
   #. Type ``Y`` and press ``ENTER`` at the **ViciBox install** prompt.
   #. Type ``Y`` and press ``ENTER`` at the **expert installation** prompt.
   #. The installer will attempt to find a LAN IP address to use for the cluster. If the IP shown is correct type ``Y`` and press ``ENTER``. If not type ``N`` and press ``ENTER`` and follow the prompts.
   #. Type ``N`` and press ``ENTER`` at the **the Database** prompt.
   #. Type in the Database IP address and press ``ENTER``, I.E. ``192.168.50.4``. If the installer is unable to connect to the Database server it will error out. Correct any issues and run the installer again.
   #. Type ``N`` and press ``ENTER`` at the **Web server** prompt.
   #. Type ``Y`` and press ``ENTER`` at the **Telephony server** prompt.
   #. Do stuff here?
   #. Type ``N`` and press ``ENTER`` at the **Archive server** prompt.
   #. Type ``N`` and press ``ENTER`` at the **built-in firewall** prompt.
   #. A summary will be listed of all selected options. Type in ``Y`` and press ``ENTER`` to accept and install.
   #. Type ``reboot`` and press ``ENTER`` to reboot and cleanly load ViciDial.
   #. Once the reboot is complete, log back in as root to get to the **#** command prompt.
   #. Type ``screen -ls`` and press ``ENTER``. While it might take upwards of 5 minutes, eventually there should be **8 Sockets in /run/screens/S-root**
   #. Type ``asterisk -r`` and press ``ENTER`` to connect to the Asterisk console. There should be different processes like **sendcron** logging on and off.
   #. Type ``quit`` and press ``ENTER`` to exit back to the **#** command prompt.
   
   The Telephony server is now installed. If there are multiple telephony servers in the cluster these instructions can be repeated on any additional servers.

Screenshots
^^^^^^^^^^^
   Install Telephony server
      .. image:: cluster-tel-1.png
         :alt: Login as root user, run 'vicibox-install'
         :width: 665

   Reboot and verify Asterisk running
      .. image:: cluster-tel-2.png
         :alt: Verify the three Database screen sessions are running
         :width: 665
