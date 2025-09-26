ViciBox 12.0.2 FirewallD Crashing
=================================

It appears that in preparation for OpenSuSE 16.0 and the long overdue update of some of it's core components that SuSE has pushed out some firewallD updates that break. The solution seems to be to reinstall firewallD to fix it.

Symptoms
--------
When running `yast firewall` it will either not load or give an error.


The Fix
-------
To resolve this issue simply reinstall firewallD

   .. code-block:: bash
      :caption: Required fix and restart

      zypper in --force firewalld
      reboot #optional, but recommended

This also applies to all releases of ViciBox12 since the update is for the OpenSuSE 15.6 distro.
