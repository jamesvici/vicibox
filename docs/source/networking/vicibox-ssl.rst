

.. _ssl:

SSL
===

ViciBox supports SSL out of the box with a self-signed certificate. While functional, it is not recommended to use this certificate at all. It is merely a placeholder for a real SSL certificate.

For clusters, it is recommended to use a wildcard SSL certificate. These are available from several Certificate Authorities, including free providers. Commercial SSL providers tend to be less problematic and require yearly renewals. Free SSL providers generally require that the certificate be renewed every 30 to 90 days through an automated process. This automated process, in conjunction with firewalls, tends to be an issue.

.. attention::
   Before SSL can be set up, the server needs a Fully Qualified Domain Name (FQDN). For example, if ``your.domain.com`` is the FQDN for the server, then the ViciDial web interface should be accessible at ``http://your.domain.com`` in a web browser. Until this is correctly working, no SSL certificate will ever work.

Common Files
------------
Apache, the dynamic portal and Asterisk all use one certificate, kept in ``/etc/pki/ssl``. A new server has a self-signed placeholder certificate there; **SSL certificate** in the :ref:`manager` replaces it with a Let's Encrypt certificate, and every renewal is copied there too. SELinux allows Apache and Asterisk to read this directory.

.. list-table:: Common SSL files
   :widths: 60 170
   :header-rows: 1
   :align: center

   * - File Location
     - Purpose
   * - /etc/pki/ssl/vicibox.crt
     - SSL certificate, with the full chain
   * - /etc/pki/ssl/vicibox.key
     - SSL private key

The locations used by ViciBox 12 and older, ``/etc/apache2/ssl.crt/vicibox.crt`` and ``/etc/apache2/ssl.key/vicibox.key``, are links to these files. The ViciPhone WebRTC templates in the ViciDial database still name the old locations, so the same templates work on servers of every ViciBox release in a cluster.

To use a certificate from another provider, copy the certificate (with its chain) and the key over the two files in ``/etc/pki/ssl``, run ``restorecon -R /etc/pki/ssl``, then ``systemctl reload apache2`` and ``asterisk -rx "core restart when convenient"``.

Let's Encrypt Certificate
-------------------------
The **SSL certificate** action in the :ref:`manager` requests a free certificate from Let's Encrypt and installs it everywhere ViciBox uses one: Apache, the dynamic portal, and Asterisk's HTTPS/WebSocket server and PJSIP TLS transport for ViciPhone (WebRTC). It also sets the server's WebSocket URL in ViciDial and sets up automatic renewal. It replaces the ``vicibox-ssl`` script from earlier releases.

The server's FQDN must already point at this server in DNS, and the server must be reachable from the internet on port 80 so Let's Encrypt can verify the name. The firewall is handled automatically: if port 80 isn't open in the firewall zone of the internet-facing network (for example with the :ref:`white-list` or :ref:`dynamic-portal`), it is opened for the few seconds of each validation and closed again. Countries blocked by :ref:`geo-block` can still stop Let's Encrypt, which checks from several places in the world.

.. list-table:: Example SSL settings
   :widths: 60 80
   :header-rows: 1
   :align: center

   * - Setting
     - Value
   * - Fully Qualified Domain Name (FQDN)
     - test.vicibox.com
   * - EMail Alert Address
     - vicidocs@vicibox.com

Setup Instructions
------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`. The **Security** panel shows the current certificate and how many days it has left.
#. Select **SSL certificate** and press :kbd:`Enter`.
#. In **Server DNS name (FQDN)**, type in the FQDN, I.E. ``test.vicibox.com``.
#. In **Email for Let's Encrypt**, type in the address for expiry notices, I.E. ``vicidocs@vicibox.com``.
#. Tick **Redirect all HTTP traffic to HTTPS** to send every visitor to the HTTPS site (recommended once the certificate works).

   .. image:: /images/vicibox13/ssl.png
      :alt: The SSL certificate screen with the current Let's Encrypt certificate, the DNS name, the email and the HTTPS redirect
      :width: 720

#. Press **Get certificate** and confirm. The manager checks the name first and warns if it doesn't point at this server.

   .. image:: /images/vicibox13/ssl-confirm.png
      :alt: The confirmation warning that the name does not resolve in DNS yet
      :width: 720

   .. image:: /images/vicibox13/ssl-done.png
      :alt: The log window after a successful certificate: installed in Apache and Asterisk, with the daily renewal in the crontab
      :width: 720

#. Verify Asterisk loaded the certificate: quit the manager with :kbd:`q`, type ``asterisk -rx "http show status"`` and press :kbd:`Enter`.
#. Test by visiting ``https://test.vicibox.com`` in a browser.

Renewal
-------
Let's Encrypt certificates are valid for 90 days. ``acme.sh`` checks every night (from root's crontab) and renews a certificate about 30 days before it expires, opening port 80 the same way if needed. Let's Encrypt's check is answered by Apache, so if Apache isn't running at that moment it is started for the check and stopped again afterwards. After a renewal Apache is reloaded, and Asterisk restarts as soon as no calls are up, so the phones and the WebRTC phone get the new certificate. The firewall stays up the whole time. Renewals are logged to ``/var/log/acme-renew.log``, which can be viewed from **View logs** in the manager.

Certificates set up with the ``vicibox-ssl`` script of earlier releases move to this renewal the next time **SSL certificate** is run for them.
