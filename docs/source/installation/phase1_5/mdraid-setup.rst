
.. _mdraid-setup:

RAID Setup
==========

These instructions only apply if the :ref:`media-md` installation media was used. That media installs the system onto a RAID 1 (mirror) that starts out with a single drive; adding a second drive makes it a real mirror, so the server keeps running, and can boot, if either drive fails.

The first root login already offers to add the second drive (see :ref:`phase1`). Use **Software RAID** in the :ref:`manager` if that was skipped, to check on the mirror, to replace a failed drive, or to add a hot spare.

If the drives are not the exact same size, the smaller drive must be the one selected during installation: a drive can only join the mirror if it is at least as big as the drive the system is on.

.. warning::
   Adding a drive erases everything on it. If a drive was used before, the manager also stops and wipes any old RAID array on it.

The Software RAID Screen
------------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`. The **System** panel shows the RAID state under **Storage**: mirrored, rebuilding, degraded, or which drive failed.
#. Select **Software RAID** and press :kbd:`Enter`.

The screen lists the arrays with the state of each drive in them, and every drive in the server: **member**, **free**, or in use by something else. While a mirror is copying, the progress is updated every few seconds. Below the list are the actions that apply right now.

.. image:: /images/vicibox13/raid-copying.png
   :alt: The Software RAID screen while the mirror copies (rebuilding 19%)
   :width: 720

Once both drives are in sync, the server can run and boot from either one:

.. image:: /images/vicibox13/raid-mirrored.png
   :alt: The Software RAID screen with both drives in sync
   :width: 720


Adding the Second Drive
-----------------------
#. On the Software RAID screen, select **Add a drive**.
#. In **Drive to add**, pick the new drive. Check the size and model shown; everything on it is erased.

   .. image:: /images/vicibox13/raid-add.png
      :alt: Add a drive with a free drive selected
      :width: 720

#. Press **Apply**, check the drive named in the confirmation, and press **Go**.

   .. image:: /images/vicibox13/raid-add-confirm.png
      :alt: The confirmation before the new drive is erased and added
      :width: 720


The manager copies the partition layout to the new drive, adds it to the mirror, copies the boot partition and installs the boot loader on it, and updates ``/etc/mdadm.conf`` and the initrd. The mirror is then copied in the background (a resync), which takes a while for a large drive; the server can be used, and rebooted, meanwhile.

If both slots of the mirror are already in use, a third drive is added as a **hot spare**: it stays idle and takes over automatically when a drive fails.

Replacing a Failed Drive
------------------------
When a drive fails, the server keeps running on the other one. The **Storage** line shows which drive failed, and the system sends a mail to ``root`` (see Alerts below).

.. image:: /images/vicibox13/raid-failed-main.png
   :alt: The main screen with Storage showing failed: sdb
   :width: 720


#. On the Software RAID screen, select **Remove a drive**, pick the failed drive (marked **failed**), press **Apply** and **Go**. This also works for a drive that is still running but reporting errors: it's marked failed and taken out of the mirror.

   .. image:: /images/vicibox13/raid-remove.png
      :alt: Remove a drive with the failed drive selected
      :width: 720


   .. image:: /images/vicibox13/raid-remove-confirm.png
      :alt: The confirmation before the drive is taken out of the mirror
      :width: 720

#. Replace the drive. With hot-swap bays this can be done while the server runs; otherwise shut it down first.
#. On the Software RAID screen, select **Add a drive**, pick the new drive, press **Apply** and **Go**.

The drive holding the last working copy of the system can't be removed.

Boot Loader
-----------
Each drive in the mirror carries its own copy of the boot partition and boot loader, so the server boots from whichever drive is left. When a system update installs a new boot loader, only the drive the server booted from gets it. Select **Reinstall the boot loader on all drives** on the Software RAID screen after such updates to copy it to every drive.

Alerts
------
The manager sets ``MAILADDR root`` in ``/etc/mdadm.conf``, so ``mdmonitor`` mails ``root`` when a drive fails or an array degrades. Forward root's mail to an address someone reads, or set ``MAILADDR`` to that address.

To check the arrays from the command prompt, type ``cat /proc/mdstat`` and press :kbd:`Enter`.

Filesystem Layout
-----------------
.. list-table:: System Mounts
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Mount
     - Location
   * - / (root)
     - /dev/md0
   * - swap
     - /swapfile, a file on the root filesystem (so it is mirrored too)
   * - /boot/efi
     - The EFI partition of the first drive; every drive in the mirror carries a copy

.. list-table:: Drive Layout
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Partition
     - Use
   * - 1
     - BIOS boot loader
   * - 2
     - EFI system partition
   * - 3
     - Member of /dev/md0

.. note::
   Servers installed with ViciBox 12 or older have the root array on /dev/md2 and swap as its own array, /dev/md1. The Software RAID screen handles that layout too.

Screenshots
-----------
   Use wipefs to clear target drives
      .. image:: mdraid-wipefs.png
         :alt: wipefs to clean drives
         :width: 640


