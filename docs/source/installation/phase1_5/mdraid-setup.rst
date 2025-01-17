.. _phase1_5-mdraid-setup:

==============
MD RAID Setup
==============

These instructions only apply if the :ref:`media-md` installation media was used. If the two drives are not the exact same size then the smaller drive must be the drive selected during installation. There is no way to add a second drive to a RAID array if it's not at least the same size or bigger then the first drive.

.. warning:: MD RAID setup can be temperamental. If there are any problems during the installation it's recommended to wipe all drives and start over. That can be done by running ``wipefs -fa /dev/sda`` and ``wipefs -fa /dev/sdb`` prior to reinstalling.

Setup Instructions
------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-mdraid1`` and press ``ENTER`` to start the setup process.
#. A summary of what will be done is shown. Type ``Y`` and press ``ENTER`` start setting up the RAID array.
#. If any old RAID arrays are found the script will prompt if you want to remove them. Type ``Y`` and press ``ENTER`` to remove the old arrays.
#. When done, it's recommended to return to the command prompt instead of watching the arrays rebuild. Type ``N`` and press ``ENTER`` to exit to the **#** command prompt
#. To check the status of the MD RAID arrays, type ``cat /proc/mdstat`` and press ``ENTER``. md1 is the swap array and md2 is the root array.
#. While not strictly necessary, it's advised to reboot the server at this time. Type ``reboot`` and press ``ENTER`` to reboot the server.

Screenshots
-----------
Run vicibox-mdraid1
   .. figure:: mdraid-1.png
      :alt: Add second drive and setup RAID 1
      :width: 665

If old RAID detected, clear it out
   .. figure:: mdraid-2.png 
      :alt: If old RAID arrays are found, try to remove them  
      :width: 665
   
Verify RAID array is setup
   .. figure:: mdraid-3.png
      :alt: Reboot for good measure for any system updates
      :width: 665

WipeFS
   .. figure:: mdraid-wipefs.png
      :alt: Wipe all drives and reinstall
      :width: 665
