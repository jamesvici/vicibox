ViciBox 12.0.2 dynamic portal inaccessible
==========================================

It appears that in preparation for OpenSuSE 16.0 and the long overdue update of some of it's core components that SuSE has pushed out some Apache updates which overwrote listen.conf. This prevents the dynamic portal from properly being accessible

Symptoms
--------
The dynamic portal will be inaccessible even after enabling it in the firewall


The Fix
-------
To resolve this issue re-enable the listen ports in Apache

   .. code-block:: bash
      :caption: Required fix and restart

      sed -i 's/^Listen 80/Listen 80\nListen 81/' /etc/apache2/listen.conf
      sed -i 's/^\t\tListen 443/\t\tListen 443\n\t\tListen 446/' /etc/apache2/listen.conf
      service apache2 restart

This also applies to all releases of ViciBox12 since the update is for the OpenSuSE 15.6 distro.
