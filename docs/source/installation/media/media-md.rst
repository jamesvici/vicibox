.. _media-md:

===============
MultiDevice ISO
===============
:download:`MD RAID1 Installation Image <https://download.vicidial.com/iso/vicibox/server/ViciBox_V12.x86_64-12.0.2-md.iso>`
    The 'MD' or MultiDevice RAID media installs the OS into a software RAID-1. This allows two plain drives to be used together for failure redundancy without any special hardware or server support. For best results the two drives should be a matched pair in terms of size and connection type (SATA/NVMe). If one drive is slightly smaller or faster it should be installed as the first drive in the system. The smaller or faster drive also needs to be the selected target drive during the Phase 1 installation. If you install to a larger drive you won't be able to add the smaller one to the RAID array. Unfortunately drives don't let you put 2TB of stuff into a 1TB bucket.

    The RAID setup tool, ``vicibox-mdraid1``, supports mixing between SATA and NVMe drives. You can add new drives to the array as well as spares or to replace a failed drive. Unfortunately the tool does not support removing drives from the array or converting the array to any other type (RAID 0/5/6/10/50/60/etc). Fortunately if you have a hot-swap drive chassis you can just safely yank the drive and Linux will carry on as if nothing happened.