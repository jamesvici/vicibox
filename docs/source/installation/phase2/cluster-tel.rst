
Telephony
=========

Follow these steps to install and configure the telephony server for a ViciDial cluster. The database and web servers must already be installed.

   #. If not already, log in as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
   #. Select **Install Cluster** and press :kbd:`Enter`, check what was detected and press **Continue**.
   #. On **Server setup**, check that **IP address for ViciDial** is this server's LAN address, I.E. ``192.168.122.44``.
   #. Under **Server roles**, tick **Telephony server**. The note next to it shows the SIP stack on port 5060: **PJSIP** by default.
   #. Under **Master database**, type in the database server's IP address in **Master database IP**, I.E. ``192.168.122.41``.

      .. image:: /images/vicibox13/install-setup-telephony.png
         :alt: Server setup with the Telephony server role ticked and the master database IP filled in
         :width: 720

   #. To use chan_sip on port 5060 instead of PJSIP, press **Settings...** next to **Telephony server**, pick **chan_sip on port 5060** and press **OK**; see :ref:`sip-stack`. Otherwise skip this step.

      .. image:: /images/vicibox13/install-settings-telephony.png
         :alt: The Telephony server settings page with the PJSIP and chan_sip choices
         :width: 720

   #. Press **Next**. The installer reads the rest of the cluster from the database: whether this is the first telephony server, and the archive server if there is one.
   #. Review the summary, press **Install** and confirm with **Install**. The external IP is detected and set automatically; see :ref:`external-ip` to change it.

      .. image:: /images/vicibox13/install-summary-telephony.png
         :alt: The Review and install summary for a telephony server, with the cluster's archive server
         :width: 720

   #. When it says **Finished**, press **Quit**, then type ``reboot`` and press :kbd:`Enter`.
   #. Once the reboot is complete, log back in as root and type ``vicibox``. The **Services** panel should show **vicidial** as active. It can take up to 5 minutes after boot for ViciDial to start everything.
   #. Quit the manager with :kbd:`q`. Type ``asterisk -r`` and press :kbd:`Enter` to connect to the Asterisk console. There should be different processes like **sendcron** logging on and off.
   #. Type ``quit`` and press :kbd:`Enter` to exit back to the **#** command prompt.

   The Telephony server is now installed. If there are multiple telephony servers in the cluster, these instructions can be repeated on any additional servers. The first telephony server uploads its sound files to the audio store on the web server; the others download them from there. The G729 and G723 codecs are installed on every telephony server. A telephony server installed after the archive server uses it automatically; one installed before it is pointed at the archive with **Archive server** in the manager (see :ref:`archive-server`).

   The main screen of a server with the telephony role, here an Express server, which has every role:

   .. image:: /images/vicibox13/dashboard-dial1-main.png
      :alt: The main screen of a server with the telephony role, with its SIP stack and archive server in the ViciDial panel
      :width: 720

.. _archive-install:

Archive Server
==============

The archive server stores the call recordings: the telephony servers move them there by FTP, and ViciDial plays them back from it over HTTP. A cluster has one archive server. Install it after the database server:

#. Start **Install Cluster** on the archive server and press **Continue**.
#. On **Server setup**, tick **Archive server**, and enter the database server's IP address in **Master database IP**.
#. **Settings...** next to **Archive server** holds the FTP login the telephony servers use and the archive URL. The address fills in with this server's IP; the defaults are fine for most clusters.

   .. image:: /images/vicibox13/install-settings-archive.png
      :alt: The Archive server settings page with the FTP login and the archive URL
      :width: 720

#. Press **Next**, review the summary, press **Install** and confirm with **Install**, then reboot.

.. important::
   The ViciBox firewall allows FTP only in the **internal** zone. Put the archive server's network card in the **internal** zone (**Network setup**, **Firewall zone**, see :ref:`firewall-zones`), or the telephony servers can't upload recordings. The installer warns if no zone allows FTP.

Telephony servers installed after the archive server use it automatically. To point a telephony server that was installed before it at the archive, use **Archive server** in the manager on that telephony server (see :ref:`archive-server`).
