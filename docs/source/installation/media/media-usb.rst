

.. _media-usb:

Create USB Install Media
========================

This guide will walk you through creating a USB flash install media. The USB flash drive needs to be at least the size of the downloaded ISO; a 4 GB or larger drive works for either ViciBox |release| image. Any data that exists on the USB flash drive will be lost if you follow the below instructions.

The ISO has to be written to the flash drive as an exact copy of the image, not as files copied onto it. Every method below does that.

Windows
-------
There are many different programs available to write an ISO image to a USB flash drive. Rufus was used in this example since it's well known. Other options that have worked well are imageUSB from PassMark and balenaEtcher (see Mac below). If you run into problems with any of these you may need to run them as Administrator.

#. Download the appropriate install image: :ref:`media-std` or :ref:`media-md`
#. Download `Rufus <https://rufus.ie/>`__
#. Run the downloaded Rufus executable from the previous step, I.E. 'rufus-4.x.exe' (the version number changes with each release)
#. Under 'Device' make sure it lists the correct USB flash drive to use
#. Boot selection should say "Disk or ISO image"
#. Click the 'SELECT' button and select the downloaded ISO from step 1
#. Leaving all the rest of the settings at their defaults, click the 'START' button at the bottom
#. A pop-up says the image is an ISOHybrid image. Select **Write in DD Image mode** and click the 'OK' button. Don't use the ISO Image mode that Rufus recommends: it copies the files instead of the image and replaces the image's boot loader with its own
#. In the warning pop-up explaining that the flash drive is about to be erased, click the 'OK' button
#. When the status bar says 'READY', click the 'CLOSE' button and remove your USB flash drive. It's now ready to install ViciBox.

Windows can't read the finished flash drive, so it may offer to format it. Click 'Cancel': formatting would erase the install image.


Mac
---
`balenaEtcher <https://etcher.balena.io/>`__ is a cross-platform tool that makes it easy to write ISO images to USB drives.

#. Download the appropriate install image: :ref:`media-std` or :ref:`media-md`
#. Download and install `balenaEtcher <https://etcher.balena.io/>`__
#. Open balenaEtcher from your Applications folder
#. Click "Flash from file" and select the downloaded ISO
#. Click "Select target" and choose your USB drive
#. Click "Flash!" to begin writing the image
#. Enter your administrator password when prompted
#. Wait for verification to complete
#. Once complete, safely eject the USB drive. It's now ready to install ViciBox.

macOS can't read the finished flash drive either. If it says "The disk you attached was not readable by this computer", click 'Ignore' or 'Eject', not 'Initialize'.

Without installing anything, the same can be done in the Terminal with ``dd``. Plug in the flash drive and type ``diskutil list external`` to find it, I.E. ``/dev/disk4``; replace ``diskN`` below with that number. Writing to ``rdiskN`` instead of ``diskN`` is much faster.

.. code-block:: bash

   diskutil unmountDisk /dev/diskN
   sudo dd if=ViciBox_V13.x86_64-13.0.0-beta3.iso of=/dev/rdiskN bs=4m
   diskutil eject /dev/diskN

``dd`` shows no progress on macOS; press :kbd:`Ctrl+T` to see how far it is.


Linux
-----
They're only reading this part to complain about how I didn't use the right utility with the right flags in some superior form of shell. I win.

Everyone else can use ``dd``, which every Linux distribution already has. All commands are run as ``root``, or with ``sudo`` in front.

.. warning::
   ``dd`` overwrites whatever device it is pointed at without asking. Pointing it at the wrong device, like the computer's own drive, destroys it. Check the device name twice.

#. Download the appropriate install image: :ref:`media-std` or :ref:`media-md`
#. Without the USB flash drive plugged in, type ``lsblk -d -o NAME,SIZE,MODEL,TRAN`` and press :kbd:`Enter` to list the drives already in the computer.
#. Plug in the USB flash drive and run ``lsblk -d -o NAME,SIZE,MODEL,TRAN`` again. The new entry, with ``usb`` under **TRAN** and the size of the flash drive, is the one to use, I.E. ``sdb``. In the steps below, replace ``sdX`` with that name.
#. If the desktop mounted the flash drive automatically, unmount it: type ``umount /dev/sdX?*`` and press :kbd:`Enter`. An error saying it is not mounted is fine.
#. Write the image to the whole drive, not to a partition on it (``/dev/sdX``, not ``/dev/sdX1``). Replace the ISO file name with the one you downloaded:

   .. code-block:: bash

      dd if=ViciBox_V13.x86_64-13.0.0-beta3.iso of=/dev/sdX bs=4M status=progress oflag=direct conv=fsync

#. Wait for ``dd`` to return to the prompt. It prints how much was copied when it is done; the progress can pause near the end while the last of the data is written to the drive.
#. Type ``sync`` and press :kbd:`Enter`, then remove the USB flash drive. It's now ready to install ViciBox.

To check the copy, run ``cmp -n $(stat -c %s ViciBox_V13.x86_64-13.0.0-beta3.iso) ViciBox_V13.x86_64-13.0.0-beta3.iso /dev/sdX`` before removing the drive. It prints nothing if the flash drive matches the ISO.

Graphical tools such as GNOME Disks (**Restore Disk Image**), KDE ISO Image Writer or balenaEtcher (see Mac above) do the same thing.
