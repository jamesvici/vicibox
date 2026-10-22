11.0 PHP remote code execution (php2shell)
******************************************
   On October 21st, 2026 the PHP project released a security advisory for two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that can allow unauthenticated remote code execution on any server running PHP for a website. Apache with mod_php, which is what ViciBox uses, is considered the highest risk since the attack can happen before any ViciDial code runs. This applies to all releases of ViciBox v.11.0.

   .. warning::

      This fix is experimental. Parts of the OpenSuSE Leap 15.5 build infrastructure that ViciBox v.11.0 depends on are now gone, most notably the Asterisk 16 repository no longer exists. You can apply this fix, but our recommendation is to upgrade to ViciBox v.13.0.

   ViciBox v.11.0 uses PHP 7.4 on OpenSuSE Leap 15.5. Both are end of life and the PHP project did not release a fixed PHP 7.4, so a PHP 7.4 package built from the PHP security team's backported fix is provided in the ViciBox sandbox repository.

Symptoms
========
   There are no symptoms. Every ViciBox v.11.0 server is vulnerable until the fix below is applied. Check the installed PHP version with ``php -v``.

The Fix
=======
   The below commands add the ViciBox sandbox repository, switch the installed PHP 7 packages over to the fixed ones from it, and restart apache to load the new PHP. The ``zypper mr -f`` line turns on automatic refresh for the repository so future PHP fixes are picked up by a normal ``zypper up``.

   .. code-block:: bash
      :caption: Required fix and restart

      zypper ar https://download.opensuse.org/repositories/home:/vicidial:/sandbox/openSUSE_Leap_15.5/home:vicidial:sandbox.repo
      zypper mr -f home_vicidial_sandbox
      zypper --gpg-auto-import-keys ref
      zypper dup --from home_vicidial_sandbox --allow-vendor-change
      systemctl restart apache2

   Afterwards ``php -v`` should show **PHP 7.4.34-dev**. In a cluster, do this on every server that has apache running including archive servers.
