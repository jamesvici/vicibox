Installation
============

.. _installation:

Media
-----

ViciBox supports installation from a USB drive as well as a CD/DVD drive. This is provided through an ISO file that can be used for either installation method. An ISO to USB writer like Rufus can be used to create the installation thumb drive. There are two different installation medias currently available for ViciBox.

`Standard Installation Image <http://download.vicidial.com/iso/vicibox/server/ViciBox_v10.x86_64-10.0.2.iso>`_:
The 'standard' version is for installation into a system with a single drive. If you have a hardware RAID card then this is the image to use. When in doubt this is likely the easiest to install.

`MD RAID1 Installation Image <http://download.vicidial.com/iso/vicibox/server/ViciBox_v10.x86_64-10.0.2-md.iso>`_:
The 'MD' or MultiDevice media installs in a software RAID-1. This allows two drives to be used for failure redundancy. This does requires two drives to be present in the system. For best results the two drives should be a matched pair. If one drive is slightly smaller it should be installed as the first drive in the system.

