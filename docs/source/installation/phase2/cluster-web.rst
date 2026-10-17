
Web Server Setup
================

Follow these steps to install and configure the web server for a ViciDial cluster. The database server must already be installed and reachable from this server.

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Install Cluster** and press :kbd:`Enter`, check what was detected and press **Continue**.
#. On **Server setup**, check that **IP address for ViciDial** is this server's LAN address, I.E. ``192.168.122.43``.
#. Under **Server roles**, tick **Web server**. The note next to it shows whether the redirect page is installed; it is by default.
#. Under **Master database**, type in the database server's IP address in **Master database IP**, I.E. ``192.168.122.41``. **Default logins** below it means the default ViciDial database settings are used; if the database was installed with custom settings, enter them under **Connection settings...**.

   .. image:: /images/vicibox13/install-setup-web.png
      :alt: Server setup with the Web server role ticked and the master database IP filled in
      :width: 720

#. Press **Next**. The installer connects to the database and tests the logins; if it can't, it shows the error. Correct the problem and press **Next** again.
#. Review the summary, press **Install** and confirm with **Install**.
#. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter`.
#. Once the server has rebooted, verify you can reach the web interface by going to the server's IP address in a browser, I.E. ``192.168.122.43``.
#. Click on **Administration** and log in with **Username** ``6666`` and **Password** ``1234``. Click **Continue on to the Initial Setup**: ViciDial asks for a new password for the ``6666`` user first, then the default phone and server passwords. Log in again with the new password afterwards.

.. image:: /images/vicibox13/browser-initial-setup.png
   :alt: The ViciDial initial setup screen
   :width: 720


It is recommended to give the **6666** user all Admin permissions before continuing. If there are multiple web servers in the cluster, these instructions can be repeated on any additional servers. The first web server installed holds the audio store, which the telephony servers copy their sound files to; it starts out with Asterisk's standard sounds.

Web Server Settings
-------------------
**Settings...** next to **Web server** has one option: **Install the redirect page**, which sends visitors of the server's address to the ViciDial welcome page.

.. image:: /images/vicibox13/install-settings-web.png
   :alt: The Web server settings page
   :width: 720

**Connection settings...** next to the master database IP holds the database logins this server uses to reach the primary database. They must match the primary's settings.

.. image:: /images/vicibox13/install-settings-connection.png
   :alt: The Master database connection settings page
   :width: 720
