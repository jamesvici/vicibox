11.0.1 MariaDB Limits
*********************
   The MariaDB limits config file was erroneously put in /etc/security instead of /etc/security/limits.d. The fix is to simply move the file to the right directory. This issue primarily effects larger cluster setups but it's possible for a single ViciBox Express setup to also have this issue.

Symptoms
========
   There will be MariaDB logs statings that they cannot open a table, tmp file, can't spawn process, limit reached, etc.

The Fix
=======
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type in ``mv /etc/security/mysql.conf /etc/security/limits.d/mysql.conf`` and press ``ENTER``
   #. When ready, type ``reboot`` and press ``ENTER`` to reboot and load new settings