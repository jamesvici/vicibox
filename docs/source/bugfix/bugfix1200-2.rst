========================
12.0.0 Firewall Disabled
========================

   The firewall, firewalld, is not started by default in ViciBox v.12.0.0. This is a security policy issue. By default, the network is assumed to be hostile and must be firewalled until configured otherwise. This is to prevent people from accidentally attaching an open host to the internet.
   
Symptoms
--------

   You will see tons of noise in the logs about all sort of random IPs hitting you. You'll see them showing up in mysql logs and in places they never should be. For the low hanging fruit that is the 'script kiddie', you are now their new best friend.

The Fix
-------

   The fix is simple. Enable the firewall. You can do that through yast or sysctl. It's recommended to reboot after doing this to cleanly load the firewall and the default VoIP block lists.


   .. code-block:: bash
      :caption: Enable the firewall
      
      systemctl enable firewalld.service
      reboot



