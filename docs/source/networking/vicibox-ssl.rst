.. _ssl:

SSL
###
   ViciBox supports SSL out of the box with a self-signed certificate. While functional, it is not recommended to use this certificate at all. It's merely a place-holder for a real SSL certificate.

   For clusters it's recommended to use a wildcard SSL certificate. These are available from several Certificate Authorities including the free providers. Commercial SSL providers tend to be less problematic and require yearly renewals. The free SSL providers generally require that the certificate be renewed every 30 to 90 days through an automated process. It's this automated process in conjunction with firewalls that tends to be an issue.

   .. attention:: Before SSL can be setup the server needs a Fully Qualified Domain Name aka 'FQDN'. For example, if 'your.domain.com' is the FQDN for the server then the ViciDial web interface should be accessible at 'http://your.domain.com' in a web browser. Until this is correctly working no SSL certificate ever will.

Common Files
************
   To help SSL certificates work across a cluster without requiring multiple webRTC templates there is a common file location that Apache and Asterisk is configured to use. By default the self-signed certificate is located there. To install your own certificates a symlink should be created from the actual SSL certificate to the common one.

   .. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}
   .. list-table:: Common SSL files
      :name: common-ssl-files
      :widths: 60 170
      :class: longtable
      :header-rows: 1
      :align: center

      * - File Location
        - Purpose
      * - /etc/apache2/ssl.crt/vicibox.crt
        - Public Certificate
      * - /etc/apache2/ssl.key/vicibox.key
        - Certificate Key
      * - /etc/apache2/ssl.crt/CAchain.crt
        - Optional Certificate Authority Chain

   .. note:: If vicibox-ssl is used then no common configuration is needed. The common config is handled as part of it.

Setup
=====
   The SSL certificates can be symlinked to the common vicibox certificates to help simplify setup.

   .. code-block:: bash
      :caption: Configure common SSL

      cd /etc/apache2/ssl.crt
      mv vicibox.crt vicibox.crt.old
      ln -s /file/path/to/ssl.crt vicibox.crt
      cd /etc/apache2/ssl.key
      mv vicibox.key vicibox.key.old
      ln -s /file/path/to/ssl.key vicibox.key
      service apache2 restart
      asterisk -rx "core restart now"

   Verify that SSL is working by going to https://your.domain.com in a web browser. If there are no SSL warnings then it's installed correctly.
   
ViciBox SSL
***********
   To help secure the web interface on the internet ViciBox comes with ``vicibox-ssl``. This script sets up free SSL certificates through the `Let's Encrypt <https://letsencrypt.org>`_ certificate authority and the `acme.sh <https://github.com/acmesh-official/acme.sh>`_ client. There is also an included acme-renew.sh script designed to help renew SSL certs when the local firewall is running. This is all handled automatically during the setup.

   .. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
   .. list-table:: Example SSL settings
      :name: ssl-example
      :widths: 60 80
      :class: longtable
      :header-rows: 1
      :align: center

      * - Setting
        - Value
      * - Fully Qualified Domain Name (FQDN)
        - vicidocs.vicibox.com
      * - EMail Alert Address
        - vicidocs@vicibox.com

vicibox-ssl
===========
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox-ssl`` and press ``ENTER`` to start the setup process.
   #. Type in the EMail address to use for the SSL certificate, I.E. ``vicidocs@vicibox.com``
   #. Type in the FQDN to use for the SSL certificate, I.E. ``vicidocs.vicibox.com``
   #. After reviewing the typed in information, press ``Y`` and then ``ENTER`` to start the automated setup process. If the SSL setup fails for whatever reason an error message will be displayed.
   #. After an SSL certificate is generated, press ``Y`` and press ``ENTER`` to enable the new certificate in Apache and Asterisk
   #. Press ``Y`` and ``ENTER`` to setup the needed crontab entry for cert renewal
   #. Once back at the **#** command prompt, verify that Asterisk has loaded the SSL certs by running ``asterisk -rx "http show status"``. It should say **HTTPS Server Enabled**.
   #. The last test is to go to https://your.domain.com and verify that the browser is secure.

Screenshots
-----------
   Run vicibox-ssl
      .. figure:: vicibox-ssl/vicibox-ssl-1.png
         :alt: Run vicibox-ssl and setup SSL certificate
         :width: 665
   
   Setup new SSL cert
      .. figure:: vicibox-ssl/vicibox-ssl-2.png
         :alt: Setup new SSL cert and crontab
         :width: 665

   Verify Asterisk loaded new cert
      .. figure:: vicibox-ssl/vicibox-ssl-3.png
         :alt: Verify new SSL certificate is loaded in Asterisk
         :width: 665

   Verify https in web browser
      .. figure:: vicibox-ssl/vicibox-ssl-4.png
         :alt: Verify the web browser connects via SSL
         :width: 665