
Database
========

Follow these steps to install and configure the database server for a ViciDial cluster:

   #. If not already, log in as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox-install`` and press ``ENTER`` to start the ViciBox installer.
   #. Type ``Y`` and press ``ENTER`` at the **ViciBox install** prompt.
   #. Type ``Y`` and press ``ENTER`` at the **expert installation** prompt.
   #. The installer will attempt to find a LAN IP address to use for the cluster. If the IP shown is correct, type ``Y`` and press ``ENTER``. If not, type ``N`` and press ``ENTER`` and follow the prompts.
   #. Type ``Y`` and press ``ENTER`` at the **the Database** prompt.
   #. Type ``N`` and press ``ENTER`` at the **Slave Database** prompt.
   #. Type ``Y`` and press ``ENTER`` at the **DB settings** prompt. If you want to use different database settings, type ``N`` and press ``ENTER`` to follow those prompts.
   #. Type ``N`` and press ``ENTER`` at the **Web server** prompt.
   #. Type ``N`` and press ``ENTER`` at the **Telephony server** prompt.
   #. Type ``N`` and press ``ENTER`` at the **Archive server** prompt.
   #. Type ``N`` and press ``ENTER`` at the **built-in firewall** prompt.
   #. A summary will be listed of all selected options. Type in ``Y`` and press ``ENTER`` to accept and install.
   #. Type ``reboot`` and press ``ENTER`` to reboot and cleanly load vicidial.
   #. Log in as the ``root`` user to get to the **#** command prompt.
   #. Type ``screen -ls`` and press ``ENTER`` to show running screen sessions. There should be three listed like in the screenshot.

   This will create an entry under :menuselection:`Admin --> Servers` called **DB1**. Do not delete this entry as it's needed for ViciDial to function properly.

Screenshots
-----------

   Install Database
      .. image:: cluster-db-1.png
         :alt: Login as root user, run 'vicibox-install'
         :width: 665

   Verify screen sessions
      .. image:: cluster-db-2.png
         :alt: Verify the three screen sessions are running
         :width: 665

