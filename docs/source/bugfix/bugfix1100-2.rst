
ViciBox 11.0.0 MD Image Bug
===========================

This bug affects ViciBox v.11.0.0 installations using the MD image, where the /boot directory is only 200 MB. This prevents newer kernel updates from installing. The fix is to remove the separate /boot partition and use the root filesystem for /boot. This was corrected in ViciBox v.11.0.1. Only follow these instructions if you have already run vicibox-mdraid1 on a ViciBox v.11.0.0 system.

Symptoms
--------
   When attempting to update the system using ``zypper up`` you will get an error when a new kernel attempts to install. This results in no new kernel updates being installed.

   .. code-block:: none
      :caption: Example zypper Output

      (167/212) Installing: kernel-firmware-amdgpu-20230724-150500.3.3.1.noarch [done]
      (168/212) Installing: kernel-firmware-all-20230724-150500.3.3.1.noarch ...[done]
        installing package kernel-default-5.14.21-150500.55.12.1.x86_64 needs 26MB on the /boot filesystem
      (169/212) Installing: kernel-default-5.14.21-150500.55.12.1.x86_64 ......[error]
      Installation of kernel-default-5.14.21-150500.55.12.1.x86_64 failed:
      Error: Subprocess failed. Error: RPM failed: Command exited with status 1.
      Abort, retry, ignore? [a/r/i] (a):


The Fix
-------
To resolve this issue, follow these steps:

   #. Log in as the ``root`` user to access the ``#`` command prompt.
   #. Copy and paste the following commands to remove the separate /boot partition:

      .. code-block:: bash
         :caption: Remove /boot partition

         cd /
         umount /boot/efi
         mkdir boot-orig
         rsync -ravv /boot/ /boot-orig/
         umount /boot
         rsync -ravv /boot-orig/ /boot/
         mount /boot/efi
         cp /etc/fstab /etc/fstab.orig
         sed -i '/boot ext4/c\' /etc/fstab
