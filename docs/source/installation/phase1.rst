Phase 1
#######
   The installation of ViciBox is pretty straight forward. There have been some issues reported when installing over previous installations of Linux. The best way to insure a smooth installation is to wipe the drives before hand.

Install ViciBox
***************

   #. Boot from the install :ref:`media`.
   #. By default the install media will boot from the servers local drive. Select **Install ViciBox** and press ``ENTER`` to start the ViciBox install.
   #. If there are multiple disks present in the system you will need to select the boot disk. Typically the first disk in the list is the first boot disk. Using the up and down arrow keys select the installation disk and press ``ENTER``
   #. A confirmation dialog box will open to confirm the destruction of all data on the installation disk. If you proceed past this point there will be permanent data loss on the installation disk. Press ``ENTER`` to select **YES** and start the installation process.
   #. You will see a couple of progress indicators as the installer copies ViciBox to the installation disk. After that the system will boot from the installation disk and continue installing. After a short wait a **login:** prompt will be displayed along with the current network configuration. At this point the rest of the instruction can be carried out through either the console or SSH.
   #. At the **login:** prompt type ``root`` and press ``ENTER``
   #. The first root login to the system will start a configuration wizard. Press ``ENTER`` to continue.
   #. Using the up and down arrow keys, select the system's localisation and press ``ENTER``.
   #. Using the up and down arrow keys, select the system's keyboard layout and press ``ENTER``.
   #. Using the up and down arrow keys, read through the license until satisfied. Press ``ENTER`` to continue.
   #. Using the ``TAB`` key, select **Yes** and press ``Enter`` to accept the license.
   #. Using the up and down arrow keys, select the system's local timezone and press ``ENTER``.
   #. Type in the new root password you want to use and press ``ENTER``. To keep the old root password type in ``vicidial``.
   #. Type in the new root password again from the above step to confirm it and press ``ENTER``.
   #. At this point the system will apply the settings before finally giving a **vicibox11\:~ #** command prompt.
   
   Congrats, ViciBox has been installed.

Screenshots
===========
   Select Install ViciBox
      .. image:: ./phase1/boot-installer.png
         :alt: Select ViciBox installer
         :width: 665

   Select Installation Disk
      .. image:: ./phase1/select-target.png
         :alt: Select installation disk if multiple drives
         :width: 665

   Confirm data destruction
      .. image:: ./phase1/confirm-target.png
         :alt: Confirm erasure of installation disk
         :width: 665
   
   Installing to disk
      .. image:: ./phase1/install-to-disk.png
         :alt: ViciBox is being installed to the installation disk
         :width: 665

   Login as root
      .. image:: ./phase1/login-prompt.png
         :alt: Login Prompt
         :width: 665

   Select system locale
      .. image:: ./phase1/select-locale.png
         :alt: Select systems local
         :width: 665

   Select keyboard layout
      .. image:: ./phase1/select-keyboard.png
         :alt: Select the systems keyboard layout
         :width: 665

   Read through license
      .. image:: ./phase1/show-license.png
         :alt: Read through the systems licenses
         :width: 665

   Accept the license
      .. image:: ./phase1/accept-license.png
         :alt: Accept the licenses
         :width: 665

   Select timezone
      .. image:: ./phase1/select-timezone.png
         :alt: Select systems timezone
         :width: 665

   Type in new root password
      .. image:: ./phase1/enter-root-password.png
         :alt: Enter the systems new root password
         :width: 665

   Confirm the new root password
      .. image:: ./phase1/confirm-root-password.png
         :alt: Confirm the new root password
         :width: 665

   Command prompt, installation complete.
      .. image:: ./phase1/installation-complete.png
         :alt: Installation is complete when you have a command prompt
         :width: 665