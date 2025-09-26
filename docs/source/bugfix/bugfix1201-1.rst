ViciBox 12.0.1 YaST Error Bug
=============================

In ``/etc/firewalld/zones/external.xml``, the 'ssh' service is listed twice. While FirewallD ignores this, YaST will hang or error when opening the firewall module. This is a bug in the YaST firewall module, not in ViciBox. The fix is to remove the duplicate 'ssh' service from the external zone so YaST doesn't get confused.

Symptoms
--------
The general symptom is that when you launch ``yast firewall`` or enter the firewall module, it hangs for a while before eventually presenting the error shown below.

.. figure:: ./bugfix1201-1a.png
   :alt: YaST error with external.xml
   :width: 665

   YaST firewall issue

The Fix
-------

If you apply updates with ``zypper up`` and do not have customized firewall settings, you can simply copy the new external.xml zone file over the old one. If you have custom firewall settings, manually edit the external.xml file to remove the duplicate 'ssh' service, or update the new file as needed.

   .. code-block:: bash
      :caption: Copy replacement file over old one

      zypper ref && zypper up
      cp /etc/firewalld/zones/external.xml.rpmnew /etc/firewalld/zones/external.xml


