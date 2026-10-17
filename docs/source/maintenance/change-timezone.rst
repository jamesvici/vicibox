.. _change-timezone:

Change Time Zone
================

The timezone of the server should match the timezone for its physical location. These instructions modify the time zone of the operating system and PHP. If they are followed after ViciDial has been installed, you will still need to modify the GMT Offset of the server in the admin interface. This can be found under :menuselection:`Admin --> Servers` in ViciDial.

Change Time Zone Steps
----------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`. The current time zone is shown in the **System** panel.
#. Select **Time zone** and press :kbd:`Enter`.
#. In **Time zone**, type the name of the new time zone, I.E. ``America/Chicago``. Matching names are suggested as you type; press :kbd:`Right` to accept a suggestion.

   .. image:: /images/vicibox13/timezone.png
      :alt: The Time zone screen suggesting America/Chicago while typing
      :width: 720

#. Press **Apply** and confirm. The system clock zone, PHP's ``date.timezone`` and ``/etc/sysconfig/clock`` are updated.
#. Quit the manager with :kbd:`q` and reboot so Asterisk and the ViciDial processes pick up the new time zone: type ``reboot`` and press :kbd:`Enter`.
