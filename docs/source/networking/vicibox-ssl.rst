

.. _ssl:

SSL
===

ViciBox supports SSL out of the box with a self-signed certificate. While functional, it is not recommended to use this certificate at all. It is merely a placeholder for a real SSL certificate.

For clusters, it is recommended to use a wildcard SSL certificate. These are available from several Certificate Authorities, including free providers. Commercial SSL providers tend to be less problematic and require yearly renewals. Free SSL providers generally require that the certificate be renewed every 30 to 90 days through an automated process. This automated process, in conjunction with firewalls, tends to be an issue.

.. attention::
   Before SSL can be set up, the server needs a Fully Qualified Domain Name (FQDN). For example, if ``your.domain.com`` is the FQDN for the server, then the ViciDial web interface should be accessible at ``http://your.domain.com`` in a web browser. Until this is correctly working, no SSL certificate will ever work.

Common Files
------------
To help SSL certificates work across a cluster without requiring multiple webRTC templates, there is a common file location that Apache and Asterisk are configured to use. By default, the self-signed certificate is located there. To install your own certificates, a symlink should be created from the actual SSL certificate to the common one.

.. list-table:: Common SSL files
   :widths: 60 170
   :header-rows: 1
   :align: center

   * - File Location
     - Purpose
   * - /etc/apache2/ssl.crt/vicibox.crt
     - SSL Certificate
   * - /etc/apache2/ssl.key/vicibox.key
     - SSL Private Key
   * - /etc/apache2/ssl.crt/vicibox-chain.crt
     - SSL Certificate Chain

ViciBox SSL Script
------------------
The ``vicibox-ssl`` script automates the process of requesting and installing an SSL certificate from Let's Encrypt. This includes setting up automated renewal and configuring both Apache and Asterisk to use the certificate.

.. list-table:: Example SSL settings
   :widths: 60 80
   :header-rows: 1
   :align: center

   * - Setting
     - Value
   * - Fully Qualified Domain Name (FQDN)
     - vicidocs.vicibox.com
   * - EMail Alert Address
     - vicidocs@vicibox.com

Setup Instructions
------------------

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-ssl`` and press ``ENTER`` to start the setup process.
#. Type in the EMail address to use for the SSL certificate, e.g. ``vicidocs@vicibox.com``
#. Type in the FQDN to use for the SSL certificate, e.g. ``vicidocs.vicibox.com``
#. After reviewing the typed in information, press ``Y`` and then ``ENTER`` to start the automated setup process.
#. After an SSL certificate is generated, press ``Y`` and press ``ENTER`` to enable the new certificate.
#. Press ``Y`` and ``ENTER`` to set up the needed crontab entry for cert renewal.
#. Verify Asterisk loaded the SSL certs: ``asterisk -rx "http show status"``
#. Test by visiting ``https://your.domain.com`` in a browser.

Screenshots
-----------

Run vicibox-ssl
   .. figure:: vicibox-ssl/vicibox-ssl-1.png
      :alt: Run vicibox-ssl and setup SSL certificate
      :width: 640