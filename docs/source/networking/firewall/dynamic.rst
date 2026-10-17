.. _dynamic-portal:

Dynamic Portal
==============
   The dynamic portal allows for remote or work-from-home agents to authenticate with their ViciDial logins on a separate web portal. This portal is standalone outside the framework of ViciDial and restricts how fast authentication attempts can be made. It allows agents to dynamically add their IP to the firewall for ViciDial.

Setup
-----
   The dynamic portal can be used alone or together with the :ref:`white-list`. It needs a Fully Qualified Domain Name and a valid SSL certificate for HTTPS; see :ref:`ssl`.

   #. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
   #. Select **Dynamic portal** and press :kbd:`Enter`.
   #. Tick **HTTPS portal on port 446**. The plain HTTP portal on port 81 is also available, but not recommended: agents' passwords would cross the internet unencrypted.
   #. In **Portal host name**, type in the server's FQDN, I.E. ``vicidocs.vicibox.com``.

      .. image:: /images/vicibox13/dynportal.png
         :alt: The Dynamic portal screen with the HTTPS and plain HTTP portals and the portal host name
         :width: 720

   #. Press **Apply** and confirm. The portal's port is opened in the **public** zone.
   #. Select **Firewall**, tick **Dynamic portal logins only** (and **ViciWhite list only** if the White List is used too), press **Apply** and confirm.
   #. Remove every service from the **public** zone except **rtp**, **dhcpv6-client** and the portal (**dynportal-ssl**), so that only agents who logged in reach anything else (see :ref:`firewall-zones`).

   The portal should now be reachable by going to https://your.server.com:446/valid8.php

   Any IP address from the Dynamic Portal is handled through the **external** zone. By default all the services needed for ViciDial are already listed in this zone. Agent logins are remembered for 14 days. An agent who logs in to the portal gets through the firewall within a minute.

Obscurity
---------
   Since security by obscurity can be a good thing, it's also possible to change the dynamic portal to run on another port besides 446. To do that two files will need to be modified as well as the above firewall rule. References to port '446' will need to be changed to your own random port of choice.

   .. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}
   .. list-table:: Dynamic Portal Config Files
      :name: dynamic-portal-portchng
      :widths: 60 170
      :class: longtable
      :header-rows: 1
      :align: center

      * - File
        - Modification to make
      * - /etc/apache2/vhosts.d/dynportal-ssl.conf
        - First line, change 446 to preferred port
      * - /etc/apache2/listen.conf
        - Change all references of 446 to preferred port

   Apache will need to be restarted after making those changes, and the firewall told about the new port (in its saved configuration and the running one, see :ref:`firewall-zones`). That can also be accomplished through a quick ``reboot``. Under SELinux, Apache may only listen on ports labelled for web servers, so the new port must be labelled too (see :ref:`selinux`).

   .. code-block:: bash
      :caption: Restart apache and firewalld

      semanage port -a -t http_port_t -p tcp <preferred-port>
      systemctl restart apache2
      firewall-cmd --permanent --zone=public --add-port=<preferred-port>/tcp
      firewall-cmd --zone=public --add-port=<preferred-port>/tcp
   