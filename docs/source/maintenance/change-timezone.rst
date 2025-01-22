==================
Change Time Zone
==================

The timezone of the server should match the timezone for its physical location. These instructions will modify the timezone settings of the underlying operating system. If these instructions are followed after ViciDial has been installed then you will still need to modify the GMT Offset of the server in the admin interface. This can be found under the Admin --> Servers section of ViciDial.

Change Time Zone Steps
--------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt
#. Type ``vicibox-timezone`` and press ``ENTER`` to start the time zone setup
#. Using the up and down arrow keys, select the appropriate region and press ``ENTER``
#. Using the up and down arrow keys, select the appropriate time zone and press ``ENTER``
#. The selected time zone should be shown on the output. Type ``reboot`` at the **#** command prompt to reboot the server.

Screenshots
----------
Run vicibox-timezone
   .. image:: change-timezone-1.png
      :alt: Run vicibox-timezone
      :width: 640

Select Region and time zone
   .. image:: change-timezone-2.png
      :alt: Select the appropriate region and time zone
      :width: 640

Verify output
   .. image:: change-timezone-3.png
      :alt: Verify the output shows the correct time zone
      :width: 640