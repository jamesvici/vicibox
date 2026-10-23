

.. _media-md:

MultiDevice ISO
===============

:download:`MD RAID1 Installation Image <https://download.vicidial.com/iso/vicibox/server/ViciBox_V13.x86_64-13.0.0-md-beta4.iso>`
    The 'MD' or MultiDevice RAID media installs the OS into a software RAID-1. This allows two plain drives to be used together for failure redundancy without any special hardware or server support. For best results, the two drives should be a matched pair in terms of size and connection type (SATA/NVMe). If one drive is slightly smaller or faster it should be installed as the first drive in the system. The smaller or faster drive also needs to be the selected target drive during the Phase 1 installation. If you install to a larger drive you won't be able to add the smaller one to the RAID array. Unfortunately, drives don't let you put 2TB of stuff into a 1TB bucket.

    **Software RAID** in the :ref:`manager` (see :ref:`mdraid-setup`) adds the second drive, a hot spare, or a replacement for a failed drive, and takes a failed drive out of the mirror. It supports mixing SATA and NVMe drives. It does not convert the array to any other type (RAID 0/5/6/10/50/60/etc). With a hot-swap drive chassis a failed drive can be replaced while the server keeps running.

    MD5 checksum: `ViciBox_V13.x86_64-13.0.0-md-beta4.md5 <https://download.vicidial.com/iso/vicibox/server/ViciBox_V13.x86_64-13.0.0-md-beta4.md5>`__ (see :ref:`media-verify`)
