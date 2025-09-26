.. _dynamic-portal:

Dynamic Portal
==============
   The dynamic portal allows for remote or work-from-home agents to authenticate with their ViciDial logins on a separate web portal. This portal is standalone outside the framework of ViciDial and restricts how fast authentication attempts can be made. It allows agents to dynamically add their IP to the firewall for ViciDial.

Setup
-----
   The dynamic portal is only compatible with the White List and is often ran in conjunction with it.

   .. code-block:: none
      :caption: Dynamic Portal only crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --dynamic --quiet
      * * * * * /usr/bin/VB-firewall --dynamic --quiet

   .. code-block:: none
      :caption: White List with Dynamic Portal crontab

      ### ViciBox integrated firewall, using whitelist only, and check once every minute
      @reboot /usr/bin/VB-firewall --white --dynamic --quiet
      * * * * * /usr/bin/VB-firewall --white --dynamic --quiet

   All services under the **Public** zone should be removed except **dhcpv6-client** and **rtp**.

   Any IP address from the Dynamic Portal will be handled through the **External** zone in ``yast firewall``. By default all the services needed for ViciDial are already listed in this zone.

   
Enable Portal
-------------
   The dynamic portal needs to be exposed to the Public zone. While the portal works with standard HTTP it's recommended to only use HTTPS. This will require a properly setup DNS and SSL certificate. If the SSL certificate is handled outside of ``vicibox-ssl`` then /etc/apache2/vhosts.d/dynportal-ssl.conf needs to be updated to point to the correct SSL certs.

   .. code-block:: bash
      :caption: Enable SSL Dynamic Portal

      firewall-cmd --permanent --zone=public --add-port=446/tcp
      firewall-cmd --reload
   
   The portal should now be reachable by going to https://your.server.com:446/valid8.php

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

   Apache and firewalld will need to be restarted after making those changes. That can also be accomplished through a quick ``reboot``.

   .. code-block:: bash
      :caption: Restart apache and firewalld

      service apache2 restart
      firewall-cmd --permanent --zone=public --add-port=<preferred-port>/tcp
      firewall-cmd --reload
   