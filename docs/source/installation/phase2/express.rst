
.. _express:

Express Box
===========

With **Install Express** all three ViciDial roles will be installed onto a single server. This is best suited for contact centers with fewer than 20 agents or as a proof of concept. It is the recommended starting point for first-time users of ViciBox as it's the easiest option.

Different roles can later be split off and moved to different servers. After all, an express box is just all three roles running on a single server. These roles can be moved to different servers on the network as needs change.

Installation Steps
------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Install Express** and press :kbd:`Enter`. The manager checks the server for a few seconds.
#. The first screen shows what was detected: hostname, IP addresses, Asterisk and ViciDial versions. If the network is not set up yet, press **Network setup first...**; otherwise press **Continue**.

   .. image:: /images/vicibox13/express-intro.png
      :alt: The Express installer first screen with what was detected
      :width: 720

#. Review the summary. **Enable the built-in firewall** is ticked by default; leave it on unless the server sits behind another firewall you manage. See :ref:`firewall`.

   .. image:: /images/vicibox13/express-summary.png
      :alt: The Express summary with the firewall checkbox
      :width: 720

#. Press **Install** and confirm with **Install**. The installation runs in the log window and takes several minutes.

   .. image:: /images/vicibox13/express-done.png
      :alt: The finished Express install in the log window
      :width: 720

#. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter`.
#. Once the reboot is complete, log back in as root and type ``vicibox`` to start the manager again. The **Services** panel should show **vicidial** as active. It can take up to 5 minutes after boot for ViciDial to start everything.

   .. image:: /images/vicibox13/express-main.png
      :alt: The main screen of an Express server after the reboot, with all services active
      :width: 720

#. Quit the manager with :kbd:`q`. Type ``asterisk -r`` and press :kbd:`Enter` to connect to the Asterisk console. There should be different processes like **sendcron** logging on and off.
#. Type ``quit`` and press :kbd:`Enter` to exit back to the **#** command prompt.
#. In a web browser, type in the server's IP address, I.E. ``192.168.122.47``, and press :kbd:`Enter`. The redirect page sends you on to the ViciDial welcome page.

   .. image:: /images/vicibox13/browser-welcome.png
      :alt: The ViciDial welcome page with Agent Login, Timeclock and Administration
      :width: 480

#. Click on **Administration** and log in. The default **Username** is ``6666`` with **Password** ``1234``. The first page after logging in is the copyright and license page; click **Continue on to the Initial Setup**.

   .. image:: /images/vicibox13/browser-admin-license.png
      :alt: The first administration page with Continue on to the Initial Setup
      :width: 720

#. The Initial Setup asks for a **new password** for the ``6666`` user, which ViciDial requires before going any further, and the default phone and server passwords, local GMT and voicemail zone. Fill them in and press **SUBMIT**, then log in again with the new password.

   .. image:: /images/vicibox13/browser-initial-setup.png
      :alt: The ViciDial initial setup screen
      :width: 720


ViciDial is now successfully installed and running. It's recommended to continue with the initial ViciDial setup and then give the **6666** user all Admin permissions.

What the Express Install Sets Up
--------------------------------
* MariaDB with the ViciDial database, the default ``cron`` / ``1234`` login and the phone codes and time zone data
* Apache with the ViciDial web interface, the audio store, and the redirect page on the server's address
* Asterisk with PJSIP as the main SIP stack on port 5060 (see :ref:`sip-stack`), ConfBridge conferences instead of MeetMe, the G729 and G723 codecs, the IAX2 loopback relays, and the self-signed certificate for WebRTC (see :ref:`ssl`)
* The external IP, if the server can detect it (see :ref:`external-ip`)
* The ViciDial crontab, and the firewall with the VoIP Black List (see :ref:`firewall`)
* SELinux labels for everything ViciDial writes (see :ref:`selinux`)


