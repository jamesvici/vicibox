=======
Phase 1
=======

The following section uses the MD or MultiDevice software RAID version of ViciBox. If you run into issues with RAID setup it is recommended to wipe the drives with ``wipefs -fa /dev/sdX`` (replace sdX with device ID) and start over. The installation of the non-MD version is similar but with fewer steps.

.. note::
   The installation process will destroy all data on the installation target disk. Make sure to backup any data you want to keep before proceeding.

Installation Steps
------------------
#. Boot from the install :ref:`media`.
#. By default the install media will boot from the server's local drive. Select **Install ViciBox** and press :kbd:`Enter` to start the ViciBox install.
#. If there are multiple disks present in the system you will need to select the boot disk. Typically the first disk in the list is the first boot disk. Using the up and down arrow keys select the installation disk and press :kbd:`Enter`.
#. A confirmation dialog box will open to confirm the destruction of all data on the installation disk. If you proceed past this point there will be permanent data loss on the installation disk. Press :kbd:`Enter` to select **Yes** and start the installation process.
#. You will see a couple of progress indicators as the installer copies ViciBox to the installation disk. After that the system will boot from the installation disk and continue installing. After a short wait a **login:** prompt will be displayed along with the current network configuration. At this point the rest of the instruction can be carried out through either the console or SSH.
#. At the **login:** prompt type ``root`` and press :kbd:`Enter`.
#. The first root login to the system will start a configuration wizard. Press :kbd:`Enter` to continue.
#. Using the up and down arrow keys, select the system's localisation and press :kbd:`Enter`.
#. Using the up and down arrow keys, select the system's keyboard layout and press :kbd:`Enter`.
#. Using the up and down arrow keys, read through the license until satisfied. Press :kbd:`Enter` to continue.
#. Using the :kbd:`Tab` key, select **Yes** and press :kbd:`Enter` to accept the license.
#. Using the up and down arrow keys, select the system's local timezone and press :kbd:`Enter`.
#. Type in the new root password you want to use and press :kbd:`Enter`. To keep the old root password type in ``vicidial``.
#. Type in the new root password again from the above step to confirm it and press ``ENTER``.
#. If internet connectivity is available, the system will ask to install updates. Press ``ENTER`` to continue and install updates.
#. If the MD RAID installation image was used, the system will ask to setup the RAID array if appropriate target drives are present. Select the appropriate drive number from the shown list and press ``ENTER``.
#. The RAID setup tool will ask to confirm the destruction of the target drive. Press ``ENTER`` to confirm the target drive.
#. The RAID setup is complicated with all the various states that old drives can be in. If you run into any issues with RAID setup it is recommended to wipe the drives with ``wipefs -fa /dev/sdX`` (replace sdX with device ID) and restart the installation from step 1.
#. Once the **vicibox12\:~ #** command prompt is displayed with a cursor, the installation is complete. It is highly recommended to remove the installation media and reboot. To reboot, type ``reboot`` and press ``ENTER``.
   
Congrats, ViciBox has been installed. Please remember the password you used as it will be needed in the next phase.

.. _installation-video:

Installation Video
------------------
Watch the `ViciBox v.12.0 Phase 1 Installation Video <https://www.youtube.com/watch?v=zPnjHD88Ohk>`__.

Screenshots
-----------
   Select Install ViciBox
      .. image:: ./phase1/boot-installer.png
         :alt: Select ViciBox installer
         :width: 640

   Select Installation Disk
      .. image:: ./phase1/select-target.png
         :alt: Select installation disk if multiple drives
         :width: 640

   Confirm data destruction
      .. image:: ./phase1/confirm-target.png
         :alt: Confirm erasure of installation disk
         :width: 640
   
   Installing to disk
      .. image:: ./phase1/install-to-disk.png
         :alt: ViciBox is being installed to the installation disk
         :width: 640

   Login as root
      .. image:: ./phase1/login-prompt.png
         :alt: Login Prompt
         :width: 640

   First Login
      .. image:: ./phase1/first-login.png
         :alt: First Login notice
         :width: 640

   Select system locale
      .. image:: ./phase1/select-locale.png
         :alt: Select systems locale
         :width: 640

   Select keyboard layout
      .. image:: ./phase1/select-keyboard.png
         :alt: Select the systems keyboard layout
         :width: 640

   Read through license
      .. image:: ./phase1/show-license.png
         :alt: Read through the systems licenses
         :width: 640

   Accept the license
      .. image:: ./phase1/accept-license.png
         :alt: Accept the licenses
         :width: 640

   Select timezone
      .. image:: ./phase1/select-timezone.png
         :alt: Select systems timezone
         :width: 640

   Type in new root password
      .. image:: ./phase1/enter-root-password.png
         :alt: Enter the systems new root password
         :width: 640

   Confirm the new root password
      .. image:: ./phase1/confirm-root-password.png
         :alt: Confirm the new root password
         :width: 640

   Install updates over internet
      .. image:: ./phase1/install-updates.png
         :alt: Install updates over the internet
         :width: 640

   Installation complete without RAID
      .. image:: ./phase1/installation-complete.png
         :alt: Installation is complete when you have a command prompt
         :width: 640

.. _raid-install-screenshots:

RAID Specific
-------------

   The following screenshots show installation sections related to the MD RAID image. This is only ran when multiple-drives are detected in the system and /dev/md2 is being used for root.

   Select target drive to add
      .. image:: ./phase1/raid-select-drive.png
         :alt: Select RAID target drive
         :width: 640

   Verify successful setup then reboot   
      .. image:: ./phase1/raid-install-complete.png
         :alt: RAID successful according to cat /proc/mdstat
         :width: 640

   Add a new or spare drive to the array
      .. image:: ./phase1/raid-add-drive.png
         :alt: Add a new or spare drive to the array
         :width: 640

   Verify spare (S) drive is added to array
      .. image:: ./phase1/raid-add-drive-complete.png
         :alt: Verify spare drive is added to array
         :width: 640