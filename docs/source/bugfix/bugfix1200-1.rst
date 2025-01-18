================
12.0.0 RAID tool
================

   If you applied updates before running the RAID setup during the first login then you likely do not have this issue.

   The ViciBox MDRAID1 tool, ``vicibox-mdraid1``, had an issue where previous MD RAID arrays were causing issues with the expected partioning layout. The underlying issue is the linux kernel autoassembles any MD RAID arrays it finds from metadata left over on the drives. This results in orphaned arrays like /dev/md126, /dev/md127, etc. The fix is to temporarily stop all orphaned RAID arrays on the system during RAID setup.

   A second issue relates to reinstalling the OS. In this scenario if you don't wipe the metadata from the drives you will get zombie arrays. This is where you have the previous OS' arrays mounted under the newly installed OS. For example, when you first install ViciBox12 only /dev/md2, the root array with /dev/sda4, should exist under ``/proc/mdstat``. With a zombie array, for example from a previous ViciBox 11 install, you would see /dev/md1 also listed in ``/proc/mdstat`` as read-only with /dev/sdb3 as the listed device. This has been mitigated in the above example by checking to see if /dev/sdb3, our target swap partition, already exists in /dev/md1, our swap array. If it does, the swap array is stopped and the normal execution of the script will properly create it.
   
Symptoms
--------
   With the version of vicibox-mdraid1 that was included with the ViciBox v.12.0.0 image you can potentially end up with an improperly setup swap array. If you look at the output of /proc/mdstat and see /dev/md1 listed as (auto-read-only) then that is a good indication you have this issue. You can see an example of this in the below screenshot. On this newly installed ViciBox v.12.0.0 system without updates the root array contains /dev/sda4 and the swap array contains /dev/sdb3.

   Zombie RAID from previous ViciBox install
      .. image:: ./bugfix1200-1a.png
         :alt: RAID successfully setup according to /proc/mdstat
         :width: 665

The Fix
-------

   It is important to determine the correct partitions to be used for the swap array. In the above screenshot, /dev/sda3 and /dev/sdb3 are the swap partitions. This will depend on your install and drives used. In the above screenshot, here are the commands used to fix the swap array.


   .. code-block:: bash
      :caption: Create proper swap partition

      swapoff -a
      mdadm --stop /dev/md1
      mdadm --create --force /dev/md1 --level=1 --raid-devices=2 --metadata=1.2 /dev/sda3 /dev/sdb3
      mkswap /dev/md1
      sed -i '/swap/ s/^/#/' /etc/fstab
      echo "UUID=$(blkid -s UUID -o value /dev/md2) swap swap defaults 0 0" >> /etc/fstab
      swapon -a
      cat /proc/mdstat




