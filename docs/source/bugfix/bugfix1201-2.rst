=============================
12.0.1 server_updater.db_time
=============================

At some point the MySQL_AST_CREATE_tables.sql file in SVN inadvertently had the ON UPDATE CURRENT_TIMESTAMP from the db_time field removed. This caused the db_time field to not update when the row was updated. Not sure when this was introduced but the fix is to simply add the ON UPDATE CURRENT_TIMESTAMP back.

Symptoms
--------
Symptoms vary, but it's safe to run the below command to fix the issue regardless of if you are affected or not. Worst case scenario the DB just silently ignores it cause it's already setup.

The Fix
-------
If you don't have a root password set for MariaDB you can just hit ``ENTER`` when prompted for it.

.. code-block:: bash
   :caption: Create ON UPDATE CURRENT_TIMESTAMP for db_time

   mysql -uroot -p asterisk -e "ALTER TABLE server_updater MODIFY db_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;"
   


