.. _phase1_5-mdraid-setup:

===========
RAID Setup
===========

These instructions only apply if the :ref:`media-md` installation media was used. If the two drives are not the exact same size then the smaller drive must be the drive selected during installation. There is no way to add a second drive to a RAID array if it's not at least the same size or bigger then the first drive.

.. warning::
   MD RAID setup can be temperamental. If there are any problems during the installation it's recommended to wipe all drives and start over. That can be done with wipefs, I.E. ``wipefs -fa /dev/sda`` or ``wipefs -fa /dev/nvme0``, prior to installing.

Setup Instructions
------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox-mdraid1`` and press ``ENTER`` to start the setup process.
#. If there are any orphaned RAID arrays, they will be shown. To remove them press ``Y`` and then ``ENTER``. This will destroy the data on these drives.
#. If this is not the first time running the script, a summary of the current RAID arrays will be shown.
#. If there are any suitable target drives in the system, they will be shown. Select the appropriate drive number from the list and press ``ENTER``.
#. A confirmation prompt will be shown to confirm the destruction of the target drive. Press ``ENTER`` to confirm the target drive.
#. The drive will be partitioned and added to the RAID arrays. A summary of the arrays will be shown when complete.
#. To check the status of the MD RAID arrays, type ``cat /proc/mdstat`` and press ``ENTER``. md1 is the swap array and md2 is the root array.
#. While not strictly necessary, it's advised to reboot the server at this time. Type ``reboot`` and press ``ENTER`` to reboot the server.

For more screenshots of these steps, see :ref:`raid-install-screenshots`.

Filesystem Layout
-----------------
.. list-table:: System Mounts
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Mount
     - MD Array
   * - / (root)
     - /dev/md2
   * - swap
     - /dev/md1

.. list-table:: Drive Layout
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - MD Array
     - Partition
   * - /dev/md2
     - /dev/sda4 or /dev/nvme0n1p4
   * - /dev/md1
     - /dev/sda3 or /dev/nvme0n1p3

.. note::
   When initially installed, the swap MD array is not setup. The drive layout shows only a single drive, but you can replace sda with sdb or nvme0 with nvme1 for the second drive that gets added to the array. /dev/md0 is not used by ViciBox and available for end users to use as they see fit.

Screenshots
-----------
   Use wipefs to clear target drives
      .. image:: mdraid-wipefs.png
         :alt: wipefs to clean drives
         :width: 640