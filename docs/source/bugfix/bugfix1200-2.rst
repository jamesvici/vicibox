ViciBox 12.0.0 Firewall Disabled Bug
====================================

In ViciBox v.12.0.0, the firewall (firewalld) is not started by default. This is a security policy issue: by default, the network should be assumed hostile and must be firewalled until configured otherwise. This prevents accidentally attaching an open host to the internet.
   
Symptoms
--------

   You will see tons of noise in the logs about all sort of random IPs hitting you. You'll see them showing up in mysql logs and in places they never should be. For the low hanging fruit that is the 'script kiddie', you are now their new best friend.


The Fix
-------
To resolve this issue, simply enable the firewall. You can do this through YaST or with the following commands. It is recommended to reboot after enabling the firewall to cleanly load the firewall and the default VoIP block lists.

   .. code-block:: bash
      :caption: Enable the firewall

      systemctl enable firewalld.service
      reboot



