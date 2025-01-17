.. _media-usb:

======================
Create USB Install Media
======================

This guide will walk you through creating a USB flash install media. The USB flash drive needs to be at least the size of the downloaded ISO. Any data that exists on the USB flash drive will be lost if you follow the below instructions.

Windows
-------
There are many different programs available to write an ISO image to a USB flash drive. Rufus was used in this example since it's well known. Other options that have worked well is imageUSB from OS Forensics. If you run into problems with either of these you may need to run them as Administrator.

#. Download the appropriate install image: :ref:`media-std` or :ref:`media-md`
#. Download `Rufus <https://github.com/pbatard/rufus/releases>`__
#. Run the downloaded Rufus executable from the previous step, I.E. 'rufus-4.0.exe'
#. Under 'Device' make sure it lists the correct USB flash drive to use
#. Boot selection should say "Disk or ISO image"
#. Click the Select button and select the downloaded ISO from step 1
#. Leaving all the rest of the settings at their defaults, click the 'Start' button at the bottom
#. In the pop-up window, click the 'OK' button to start writing the image to the USB flash drive
#. Sometimes there is a warning pop-up about searching for grub. If that happens, just click "OK" to continue
#. In the warning pop-up explaining that the flash drive is about to be erased, click the 'OK' button
#. When it's done, just click the 'close' button and remove your USB flash drive. It's now ready to install ViciBox.


Mac
---
`balenaEtcher <https://www.balena.io/etcher>`__ is a cross-platform tool that makes it easy to write ISO images to USB drives.

#. Download the appropriate install image: :ref:`media-std` or :ref:`media-md`
#. Download and install `balenaEtcher <https://www.balena.io/etcher>`__
#. Open balenaEtcher from your Applications folder
#. Click "Flash from file" and select the downloaded ISO
#. Click "Select target" and choose your USB drive
#. Click "Flash!" to begin writing the image
#. Enter your administrator password when prompted
#. Wait for verification to complete
#. Once complete, safely eject the USB drive. It's now ready to install ViciBox.


Linux
-----
They're only reading this part to complain about how I didn't use the right utility with the right flags in some superior form of shell. I win.

#. Install Linux
#. ???
#. Profit, err, successfully written install media
