.. _media-usb:

Create USB install media
************************
    This guide will walk you through creating a USB flash install media. The USB flash drive needs to be at least the size of the downloaded ISO. Any data that exists on the USB flash drive will be lost if you follow the below instructions.

Windows
=======
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
===
    Whoever wants to write these instructions please submit them


Linux
=====
    They're only reading this part to complain about how I didn't use the right utility with the right flags in some superior form of shell. I win.

    #. Install Linux
    #. ???
    #. Profit, err, successfully written install media
