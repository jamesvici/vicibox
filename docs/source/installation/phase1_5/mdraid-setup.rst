.. _phase1_5-mdraid-setup:

MD RAID Setup
*************
   These instructions only apply if the :ref:`media-md` installation media was used. If the two drives are not the exact same size then the smaller drive must be the one used to install to. There is no way to add a second drive to the MD RAID array if it's not the same size or bigger then the first drive.

   .. warning:: MD RAID setup can be temperamental. If there are any problems during the installation it's recommended to wipe all drives and start over. That can be done by running ``wipefs -fa /dev/sda`` and ``wipefs -fa /dev/sdb`` prior to reinstalling.


vicibox-mdraid1
===============
   #. If not already, login as the ``root`` user to get to the **#** command prompt.
   #. Type ``vicibox-mdraid1`` and press ``ENTER`` to start the setup process.
   #. A list of updates and a summary of them will be shown. Type ``Y`` and press ``ENTER`` to start downloading and installing updates.
   #. Occasionally an update will ask if you want to view it's update notice. Press ``ENTER`` to continue if this happens.
   #. While not strictly necessary, it's advised to reboot the server at this time. Type ``reboot`` and press ``ENTER`` to reboot the server.



Screenshots
-----------
   Run vicibox-mdraid1
      .. figure:: mdraid-1.png
         :alt: Add second drive and setup RAID 1
         :width: 665
      
   Verify RAID array is setup
      .. figure:: mdraid-2.png
         :alt: Reboot for good measure for any system updates
         :width: 665

   WipeFS
      .. figure:: mdraid-wipefs.png
         :alt: Wipe all drives and reinstall
         :width: 665
