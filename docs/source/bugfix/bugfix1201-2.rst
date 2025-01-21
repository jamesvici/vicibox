=============================
12.0.1 server_updater.db_time
=============================

So MariaDB/MySQL finally changed a deprecated behavior that affects all TIMESTAMP fields in the database. The old behavior was to add default ON UPDATE CURRENT_TIMESTAMP clauses to all timestamps unless defined otherwise. Since this allowed for SQL code to have hidden functionality, it was deprecated and finally turned off by default somewhere between MariaDB 10.6 (ViciBox 11) and 10.11 (ViciBox 12). The new behavior is that all behaviors must be explicitly defined.

There are portions of the ViciDial schema that existed before a TIMESTAMP field type was even available. These sections will need the SQL code updated to handle this new behavior.

The official MariaDB documentation for this is `here <https://mariadb.com/docs/server/ref/mdb/system-variables/explicit_defaults_for_timestamp/>`_.

ViciBox v.12.0.2 will be released once the schemas are updated to handle this new behavior. In the meantime, you can apply the fix below to your ViciBox system.

Symptoms
--------
Symptoms vary, but basically all sorts of weird behavior will happen and ViciDial won't work right. The good news is that there's a setting to enable the old deprecated behavior.

The bad news is that all databases will need to be exported and reimported to fix this.

The Fix
-------
The fix involves creating a backup of the old database, dropping it, and then re-importing the database with the expected behavior. This is not a trivial task and if anything goes wrong with the backup you can lose all your data. An optional step is to rename the old database to something else instead of just dropping it. This way you always have the old database if something goes horribly wrong.

Depending upon the size of your database, this process could take hours to complete. It's recommended to start this in a screen session. If you don't have production data or precious data on the server yet you can just add the configuration line to /etc/my.cnf.d/general.cnf and restart MariaDB. From there you would import or setup your ViciBox system normally.

.. code-block:: bash
   :caption: Create ON UPDATE CURRENT_TIMESTAMP for db_time
   
   screen -s "DBFIX" # Optional, but recommended
   echo "explicit_defaults_for_timestamp = Off" >> /etc/my.cnf.d/general.cnf
   systemctl restart mariadb.service
   cd /root # Go somewhere safe with lots of storage space
   mysqldump -B asterisk | gzip > asterisk-notimestamps.sql.gz
   #mysql -u root -p -e "RENAME DATABASE asterisk TO asterisk_old;" # Uncomment to rename the database instead of dropping it
   mysql -u root -p -e "DROP DATABASE asterisk;" # If you renamed the database, you can skip this line
   mysql -u root -p -e "create database asterisk default character set utf8 collate utf8_unicode_ci;"
   pv asterisk-notimestamps.sql.gz | gunzip | mysql -u root -p asterisk

