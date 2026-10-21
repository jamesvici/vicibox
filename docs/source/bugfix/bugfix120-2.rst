ViciBox 12.0 PHP remote code execution (php2shell)
==================================================

On October 21st, 2026 the PHP project released a security advisory for two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that can allow unauthenticated remote code execution on any server running PHP for a website. Apache with mod_php, which is what ViciBox uses, is considered the highest risk since the attack can happen before any ViciDial code runs.

The fix is to upgrade to php 8.2.35 or later.

Symptoms
--------
There are no symptoms. All versions of PHP are vulnerable.

   .. code-block:: bash
      :caption: Check the installed PHP version

      php -v

The Fix
-------
The below commands will add the openSUSE PHP 8.2 repository, switch the installed PHP packages over to it, and restart apache to load the new PHP. The ``zypper mr -f`` line turns on automatic refresh for the repository so future PHP updates are picked up by a normal ``zypper up``.

   .. code-block:: bash
      :caption: Required fix and restart

      zypper ar https://download.opensuse.org/repositories/devel:/languages:/php:/php82/openSUSE_Leap_15.6/devel:languages:php:php82.repo
      zypper mr -f devel_languages_php_php82
      zypper --gpg-auto-import-keys ref
      zypper dup --from devel_languages_php_php82 --allow-vendor-change
      systemctl restart apache2

Afterwards ``php -v`` should show **PHP 8.2.35** or newer. In a cluster, do this on every server that has apache running including archive servers.
