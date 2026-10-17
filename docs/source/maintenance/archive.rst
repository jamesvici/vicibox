.. _archive-server:

Archive Server
==============

An archive server stores call recordings away from the telephony servers. Recordings are mixed on the telephony server and then moved to the archive server by FTP every few minutes, and ViciDial's recording links point to the archive server's web address.

The archive server itself is installed with **Install Cluster** by ticking the **Archive server** role, usually before the telephony servers (see :ref:`cluster`). Telephony servers installed afterwards find it in the database and use it automatically.

Pointing a Telephony Server at an Archive Server
------------------------------------------------
For a telephony server that was installed before the archive server existed, or to move to another archive server:

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Archive server** and press :kbd:`Enter`. If the cluster has an archive server, its settings are filled in.
#. Check or fill in **Archive server IP**, **FTP username**, **FTP password**, **FTP port**, **FTP directory** and **Archive URL** (the web address the recordings are served from, I.E. ``http://192.168.122.46/archive``).
#. Leave **Test the FTP login first** ticked.

   .. image:: /images/vicibox13/archive-server.png
      :alt: The Archive server screen filled in from the cluster's archive server
      :width: 720

#. Press **Apply** and confirm.

Repeat on every telephony server that should use the archive server.
