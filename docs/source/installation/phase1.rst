Phase 1
*******
   The installation of ViciBox is pretty straight forward. There have been some issues reported when installing over previous installations of Linux. The best way to insure a smooth installation is to wipe the drives before hand.

   #. Boot from your install :ref:`media` of choice.
   #. By default the install media will boot from the hard drive. Select 'Install ViciBox' and press enter.
   #. If there are multiple drives present in the system you will need to select the appropriate install drive and press enter.
   #. You will be asked if you are sure you want to destroy all data on the install disk. Select Yes and press enter.
   #. You will see a couple of progress indicators are the installer loads the image to the drive and verifies it's integrity.
   #. The server will reboot into the newly installed OS to a login prompt. You can login with user 'root' with the password 'vicidial'.
   #. The first time you login a short configuration wizard is launched. Press enter to start the initial configuration.
   #. Using the up and down arrow keys, select your system's locale.
   #. Using the up and down arrow keys, select your system's keyboard layout.
   #. You can use the up and down arrow keys to red through the license. Press the enter key to exit when you are done.
   #. Select Yes and press Enter to accept the license.
   #. Using the up and down arrow keys, select your system's local timezone.
   #. Lastly, type in the new root password you want to use. If you want to keep the old root password simply type in 'vicidial'.
   #. You will need to confirm the password you chose in the previous step by entering it again.
   #. You will see some output where housekeeping is being done and the network is being restarted before getting to the command prompt.
   
   At this point the installation of ViciBox is complete.

Screenshots
===========

   Select Install ViciBox
      .. image:: ./phase1/boot-installer.png
         :alt: Select ViciBox installer
         :width: 665

   Select installation Disk if multiple drives in system
      .. image:: ./phase1/select-target.png
         :alt: Select installation disk
         :width: 665

   Confirm data destruction on installation disk
      .. image:: ./phase1/confirm-target.png
         :alt: Confirm erasure of installation disk
         :width: 665

   Login prompt upon successful ViciBox installation
      .. image:: ./phase1/login-prompt.png
         :alt: Login Prompt
         :width: 665


.. toctree::
   :maxdepth: 2
   :titlesonly:


