=============================
12.0.1 server_updater.db_time
=============================

If you are migrating a database from an older server to Vicibox v.12.0 you are not affected by this issue. This only applies to newly created databases loaded from the MySQL_AST_CREATE_tables.sql or through updates.

So MariaDB/MySQL finally changed a deprecated behavior that affects all TIMESTAMP fields in the database. The old behavior was to add default ON UPDATE CURRENT_TIMESTAMP clauses to all timestamps unless defined otherwise. Since this allowed for SQL to have hidden functionality not apparent in the source, it was deprecated and finally turned off by default somewhere between MariaDB 10.6 (ViciBox 11) and 10.11 (ViciBox 12). The new behavior is that all clauses must be explicitly defined. This means that all TIMESTAMP fields in the database that don't have an ON UPDATE CURRENT_TIMESTAMP clause will no longer update the timestamp when the row is updated. This is a problem for ViciDial because it relies on this behavior for the db_time field in the server_updater table amongst others.

There are portions of the ViciDial schema that existed before a TIMESTAMP field type was even available. These sections will need the SQL code updated to handle this new behavior. Once the schema is updated in SVN and the ViciBox ISO is updated, this will no longer be an issue. Until then, you'll need to manually fix this issue.

The official MariaDB documentation for this is `here <https://mariadb.com/docs/server/ref/mdb/system-variables/explicit_defaults_for_timestamp/>`_.

Symptoms
--------
Symptoms vary, but basically all sorts of weird behavior will happen and ViciDial won't work right. The good news is that there's a setting to enable the old deprecated behavior.


The Fix
-------
Since this primarily only affects a new database (I.E. running vicibox-express), or when applying updates, it is generally not a problem when migrating a database from an older server. In this scenario you just need to run the following commands to fix the issue.

.. code-block:: bash
   :caption: Required fix and restart
   
   echo "explicit_defaults_for_timestamp = Off" >> /etc/my.cnf.d/general.cnf
   systemctl restart mariadb.service


If you setup a new database in ViciBox v.12.0 or have applied updates you will need to export and re-import the database. Depending upon the size of your database, this process could take hours to complete. It's recommended to start this in a screen session. If you don't have production data or precious data on the server yet you can just add the configuration line to /etc/my.cnf.d/general.cnf and restart MariaDB. From there you would import or setup your ViciBox system normally.

.. code-block:: bash
   :caption: Optional export and import to fix fields
   
   screen -s "DBFIX" # Optional, but recommended
   cd /root # Go somewhere safe with lots of storage space
   mysqldump -B asterisk | gzip > asterisk-notimestamps.sql.gz
   #mysql -u root -p -e "RENAME DATABASE asterisk TO asterisk_old;" # Uncomment to rename the database instead of dropping it
   mysql -u root -p -e "DROP DATABASE asterisk;" # If you renamed the database, you can skip this line
   mysql -u root -p -e "create database asterisk default character set utf8 collate utf8_unicode_ci;"
   pv asterisk-notimestamps.sql.gz | gunzip | mysql -u root -p asterisk

