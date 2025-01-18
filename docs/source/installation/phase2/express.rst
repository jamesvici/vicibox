.. _`express`:

===========
Express Box
===========

With ``vicibox-express`` all three ViciDial roles will be installed onto a single server. This is best suited for contact centers with less then 20 agents or as a proof of concept. It is the recommend starting point for first time users of ViciBox as it's the easiest option.
    
Different roles can later be split off and moved to different servers. After all, an express box is just all three roles running on a single server. These roles can be moved to different servers on the network as needs changes.

Installation Steps
------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-express`` and press ``ENTER``.
#. Type ``Y`` and press ``ENTER`` to start the installation.
#. Once you are back at the **#** command prompt, the installation is complete. Type ``reboot`` and press ``ENTER``.
#. Once the reboot is complete, log back in as root to get to the **#** command prompt.
#. Type ``screen -ls`` and press ``ENTER``. While it might take upwards of 5 minutes, eventually there should be **11 Sockets in /run/screens/S-root** shown before returning to the **#** command prompt
#. Type ``asterisk -r`` and press ``ENTER`` to connect to the Asterisk console. There should be different processes like **sendcron** logging on and off.
#. Type ``quit`` and press ``ENTER`` to exit back to the **#** command prompt.
#. In a web browser, type in the servers IP address, I.E. ``192.168.50.4``, and press ``ENTER``
#. Click on **Administration** and login. The default **Username** is ``6666`` with **Password** ``1234``. Upon login you should see the ViciDial Initial Setup screen.

ViciDial is now successfully installed and running. It's recommended to continue with the initial ViciDial setup and then give the **6666** user all Admin permissions.

Screenshots
-----------
Run vicibox-express and reboot
   .. image:: express-1.png
      :alt: Run vicibox-express then reboot
      :width: 665

Verify that ViciDial started (may take up to 5 minutes)
   .. image:: express-2.png
      :alt: Verify screen and asterisk sessions running
      :width: 665

Verify that the web interface is working
   .. image:: express-3.png
      :alt: Go to the servers IP in a browser
      :width: 665

Login as default user (password is 1234)
   .. image:: express-4.png
      :alt: Login as user 6666 with password 1234
      :width: 665

Continue with the ViciDial setup
   .. image:: express-5.png
      :alt: Continue with the normal ViciDial setup
      :width: 665
