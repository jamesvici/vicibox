
.. _media:

Media
=====

ViciBox supports installation from a USB flash drive as well as a CD/DVD drive. This is accomplished through a hybrid ISO file that can be used for either media type. A simple ISO to USB writer like imageUSB, Rufus (in DD Image mode) or ``dd`` can be used to create the installation thumb drive; see :ref:`media-usb`. There are two different installation media available for ViciBox |release|. Both install openSUSE Leap 16.0 with ViciBox on top and need a 64-bit x86 (x86_64) server, booting in UEFI or legacy BIOS mode.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   media/media-std
   media/media-md
   media/media-usb


.. _media-verify:

Verifying the Download
----------------------
Each ISO has an ``.md5`` file next to it with its checksum. Download both into the same folder and check the ISO before writing it to a USB flash drive or DVD; a damaged download can fail partway through the installation.

* **Linux**: ``md5sum -c ViciBox_V13.x86_64-13.0.0-beta3.md5`` prints ``OK`` when the ISO matches.
* **macOS**: ``md5 ViciBox_V13.x86_64-13.0.0-beta3.iso`` in the Terminal, then compare it to the checksum in the ``.md5`` file.
* **Windows**: ``certutil -hashfile ViciBox_V13.x86_64-13.0.0-beta3.iso MD5`` in a Command Prompt, then compare it to the checksum in the ``.md5`` file.

Use the MD file names (``-md-beta3``) for the :ref:`media-md`. If the checksum doesn't match, download the ISO again.
