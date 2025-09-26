
Web Server Setup
================

Follow these steps to install and configure the web server for a ViciDial cluster:

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-install`` and press ``ENTER`` to start the ViciBox installer.
#. Type ``Y`` and press ``ENTER`` at the **ViciBox install** prompt.
#. Type ``Y`` and press ``ENTER`` at the **expert installation** prompt.
#. The installer will attempt to find a LAN IP address to use for the cluster. If the IP shown is correct, type ``Y`` and press ``ENTER``. If not, type ``N`` and press ``ENTER`` and follow the prompts.
#. Type ``N`` and press ``ENTER`` at the **the Database** prompt.
#. Type in the Database IP address and press ``ENTER``, e.g. ``192.168.50.4``. If the installer is unable to connect to the Database server it will error out. Correct any issues and run the installer again.
#. Type ``Y`` and press ``ENTER`` at the **Web server** prompt.
#. Type ``Y`` and press ``ENTER`` at the **Redirect Page** prompt.
#. Type ``N`` and press ``ENTER`` at the **Telephony server** prompt.
#. Type ``N`` and press ``ENTER`` at the **Archive server** prompt.
#. Type ``N`` and press ``ENTER`` at the **built-in firewall** prompt.
#. A summary will be listed of all selected options. Type in ``Y`` and press ``ENTER`` to accept and install.
#. Type ``reboot`` and press ``ENTER`` to reboot and cleanly load vicidial.
#. Once the server has rebooted, verify you can reach the web interface by going to the server's IP address in a browser, e.g. ``192.168.50.6``, and press ``ENTER``.
#. Click on **Administration** and log in with **Username** ``6666`` and **Password** ``1234`` to continue with the ViciDial Initial Setup.

It is recommended to give the **6666** user all Admin permissions before continuing. If there are multiple web servers in the cluster, these instructions can be repeated on any additional servers.

Screenshots
-----------

Install Web
   .. image:: cluster-web-1.png
      :alt: Login as root user, run 'vicibox-install'
      :width: 665

Reboot
   .. image:: cluster-web-2.png
      :alt: Reboot server after installation
      :width: 665

Verify web interface
   .. image:: cluster-web-3.png
      :alt: Verify the web interface comes up
      :width: 665

Login with default user
   .. image:: cluster-web-4.png
      :alt: Login as the default user to continue
      :width: 665

Continue to ViciDial Initial Setup
   .. image:: cluster-web-5.png
      :alt: Continue on with the ViciDial Initial Setup
      :width: 665

