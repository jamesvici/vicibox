.. _phase1_5-mdraid-setup:

==============
MD RAID Setup
==============

These instructions only apply if the :ref:`media-md` installation media was used. If the two drives are not the exact same size then the smaller drive must be the drive selected during installation. There is no way to add a second drive to a RAID array if it's not at least the same size or bigger then the first drive.

.. warning:: MD RAID setup can be temperamental. If there are any problems during the installation it's recommended to wipe all drives and start over. That can be done with wipefs, I.E. ``wipefs -fa /dev/sda`` or ``wipefs -fa /dev/nvme0``, prior to installing.

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

You can refer to the :ref:`Phase 1 RAID Screenshots <raid-install-screenshots>` for examples of the above steps.