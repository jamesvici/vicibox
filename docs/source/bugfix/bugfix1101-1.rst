
ViciBox 11.0.1 MariaDB Limits Bug
=================================

This bug affects ViciBox v.11.0.1 installations where the MariaDB limits config file was mistakenly placed in ``/etc/security`` instead of ``/etc/security/limits.d``. The fix is to move the file to the correct directory. This issue primarily affects larger cluster setups, but single ViciBox Express setups may also be impacted.

Symptoms
--------
You may see MariaDB logs stating that they cannot open a table, create a tmp file, can't spawn a process, or that a limit has been reached.

The Fix
-------
To resolve this issue, follow these steps:

   #. Log in as the ``root`` user to access the ``#`` command prompt.
   #. Move the MariaDB limits config file to the correct directory:

      .. code-block:: bash

         mv /etc/security/mysql.conf /etc/security/limits.d/mysql.conf

   #. Reboot the server to load the new settings:

      .. code-block:: bash

         reboot