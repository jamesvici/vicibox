.. _media-md:

MultiDevice ISO
===============
:download:`MD RAID1 Installation Image <https://download.vicidial.com/iso/vicibox/server/ViciBox_v12.x86_64-12.0.0-md.iso>`
    The 'MD' or MultiDevice software RAID media installs into a software RAID-1. This allows two drives to be used together for failure redundancy. For best results the two drives should be a matched pair. If one drive is slightly smaller it should be installed as the first drive in the system. The smaller drive also needs to be the selected target drive during the Phase 1 installation.

    The RAID setup tool, ``vicibox-mdraid1``, supports mixing between SATA and NVMe drives. You can add new drives to the array as well either as spares or to replace a failed drive. Unfortunately the tool does not support removing drives from the array or converting the array to any other type (RAID 0/5/6/10/50/60). Fortunately if you have a hot-swap drive chassis you can just safely yank the drive and Linux will carry on as if nothing happened.