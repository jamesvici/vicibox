Change Timezone
===============
   The timezone of the server should match the timezone for it's physical location. These instructions will modify the timezone settings of the underlying operating system. If these instructions are followed after ViciDial has been installed then you will still need to modify the GMT Offset of the server in the admin interface. This can be found under the Admin --> Servers section of ViciDial.

vicibox-timezone
----------------
   #. If not already, login as the 'root' user to get to the command prompt.
   #. Type ``vicibox-timezone`` to start the timezone configuration.
   #. Using the Up and Down arrow keys, select the appropriate region for the server.
   #. Press the ``TAB`` key to move to the 'Time Zone' selection window.
   #. Using the Up and Down arrow keys, select the appropriate time zone for the server.
   #. Press ``ALT``-``O`` or ``TAB`` to select the 'OK' button and apply changes.
   #. The select time zone should appear on the output. Type ``reboot`` to reboot the server.

Screenshots
^^^^^^^^^^^
   Run vicibox-timezone
      .. image:: change-timezone-1.png
         :alt: Run vicibox-timezone
         :width: 665
    
   Select Region and time zone
      .. image:: change-timezone-2.png
         :alt: Select the appropriate region and time zone
         :width: 665

   Verify output
      .. image:: change-timezone-3.png
         :alt: Verify the output shows the correct time zone
         :width: 665