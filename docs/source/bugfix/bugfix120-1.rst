ViciBox 12.0 php.ini overwritten
================================

It appears that in preparation for OpenSuSE 16.0 and the long overdue update of some of it's core components that SuSE has pushed out some PHP updates which overwrite the vicidial specific options in php.ini. This also applies to all releases of ViciBox12 since the update is for the OpenSuSE 15.6 distro itself and not any specific ViciBox release. The solution is to re-enable these settings in php.ini. 

Symptoms
--------
The primary tell-tale sign of this is extremely large error and optionally access logs from apache with PHP warnings as well as slow or increased web server load.

The Fix
-------
To resolve this issue simply reinstall firewallD

   .. code-block:: bash
      :caption: Required fix and restart

      sed -i 's/^error_reporting = E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT/error_reporting = E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT & ~E_WARNING/' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.enable=1/opcache.enable=1/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.memory_consumption=128/opcache.memory_consumption=128/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=16/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.max_accelerated_files=10000/opcache.max_accelerated_files=20000/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.max_wasted_percentage=5/opcache.max_wasted_percentage=5/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.validate_timestamps=1/opcache.validate_timestamps=1/g' /etc/php8/apache2/php.ini
      sed -i 's/;opcache.revalidate_freq=2/opcache.revalidate_freq=10/g' /etc/php8/apache2/php.ini
      service apache2 restart

