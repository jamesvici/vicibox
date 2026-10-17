

.. _phase1:

Phase 1
=======

The following section uses the MD (MultiDevice) software RAID version of ViciBox. If you run into issues with RAID setup, it is recommended to wipe the drives with ``wipefs -fa /dev/sdX`` (replace sdX with device ID) from the install media's :ref:`rescue-shell` and start over. The installation of the non-MD version is the same, without the RAID mirror at the first login.

.. note::
   The installation process will destroy all data on the installation target disk. Make sure to back up any data you want to keep before proceeding.

Installation Steps
------------------
#. Boot from the install :ref:`media`. For a USB flash drive, this usually means pressing the server's boot menu key during power-on (often :kbd:`F11`, :kbd:`F12` or :kbd:`Esc`) and picking the flash drive.
#. The boot menu starts on **Boot from Hard Disk** and boots the server's local drive after 10 seconds. Before then, press the down arrow key to select **Install ViciBox_V13** and press :kbd:`Enter` to start the ViciBox install. If the installer doesn't start or the screen stays blank, boot the media again and pick **Failsafe -- Install ViciBox_V13** instead.

   .. image:: /images/vicibox13/install-bootmenu.png
      :alt: The install media boot menu with Install ViciBox_V13 selected
      :width: 560

#. If there are multiple disks present in the system you will need to select the installation disk. The list shows each disk by its model and serial number with its size; it is sorted by name, not by boot order. Using the up and down arrow keys select the installation disk and press :kbd:`Enter`. With the :ref:`media-md`, pick the smaller of the two drives if they differ in size.

   .. image:: /images/vicibox13/install-select-disk.png
      :alt: Select Installation Disk with two disks listed
      :width: 560

#. A confirmation dialog box asks **Destroying ALL data on** the selected disk, **continue?** If you proceed past this point there will be permanent data loss on the installation disk. Press :kbd:`Enter` to select **Yes** and start the installation process.

   .. image:: /images/vicibox13/install-confirm-erase.png
      :alt: The confirmation before the installation disk is erased
      :width: 560

#. Two progress bars follow: one while the installer copies ViciBox to the installation disk, and one while it verifies the copy.

   .. image:: /images/vicibox13/install-copying.png
      :alt: Copying ViciBox to the installation disk
      :width: 560


   .. image:: /images/vicibox13/install-verifying.png
      :alt: Verifying the copy on the installation disk
      :width: 560

#. :ref:`media-md` only: if another drive in the server still holds the RAID mirror of an earlier install of this ViciBox release, the installer asks whether to wipe it. Select **Yes**: if it is kept, the new install stalls at boot and may start the old one instead. Drives with anything else on them are not touched.

   .. image:: /images/vicibox13/install-wipe-old-mirror.png
      :alt: The installer asking whether to wipe the old RAID mirror on another drive
      :width: 560

#. The installer then starts the newly installed system directly, without a reboot. Its first boot grows the system to fill the disk, which can take a moment.
#. After a short wait a **login:** prompt is displayed with the server's SSH keys and network configuration. The IP address shown there can be used to continue over SSH instead of the console.

   .. image:: /images/vicibox13/install-login-prompt.png
      :alt: The login prompt with the SSH keys, the network configuration and the system resources
      :width: 560

#. At the **login:** prompt type ``root`` and press :kbd:`Enter`, then type the default password ``vicidial`` and press :kbd:`Enter`.
#. The first root login starts the **JeOS Firstboot** setup. Press :kbd:`Enter` on **Start**.

   .. image:: /images/vicibox13/jeos-start.png
      :alt: JeOS Firstboot: Welcome to ViciBox v.13.0
      :width: 560

#. Using the up and down arrow keys, select the system locale (language), I.E. ``en_US``, and press :kbd:`Enter`.

   .. image:: /images/vicibox13/jeos-locale.png
      :alt: Select system locale
      :width: 560

#. Using the up and down arrow keys, select the system's keyboard layout, I.E. ``us``, and press :kbd:`Enter`.
#. Read through the license with the up and down arrow keys until satisfied, then press :kbd:`Enter` on **Continue**.

   .. image:: /images/vicibox13/jeos-license.png
      :alt: The ViciBox license
      :width: 560

#. **Yes** is already selected: press :kbd:`Enter` to accept the license.

   .. image:: /images/vicibox13/jeos-license-agree.png
      :alt: Do you agree with the terms of the license?
      :width: 560

#. Using the up and down arrow keys, select the system's local time zone and press :kbd:`Enter`. The time zone can be changed later, see :ref:`change-timezone`.

   .. image:: /images/vicibox13/jeos-timezone.png
      :alt: Select time zone
      :width: 560

#. Type in the new root password you want to use and press :kbd:`Enter`. To keep the old root password type in ``vicidial``.

   .. image:: /images/vicibox13/jeos-root-password.png
      :alt: Enter root password
      :width: 560

#. Type in the new root password again from the above step to confirm it and press :kbd:`Enter`.
#. **SSH Key Enrollment** asks whether to add SSH keys for logging in. Select **No** unless you have a key to add now; keys can be added later in ``/root/.ssh/authorized_keys``.

   .. image:: /images/vicibox13/jeos-ssh-keys.png
      :alt: SSH Key Enrollment: Do you want to enroll keys for SSH access?
      :width: 560

#. **User Creation** offers an additional user account. ViciBox doesn't need one, since root can log in over SSH with its password: press :kbd:`Tab` twice to reach **Skip** and press :kbd:`Enter`.

   .. image:: /images/vicibox13/jeos-user.png
      :alt: User Creation with the Skip button
      :width: 560

#. The **Welcome to ViciBox** screen of the :ref:`manager` opens. It shows the hostname, IP addresses, time zone and drives, and offers:

   * **Install updates**: runs ``zypper up`` and then installs new recommended packages. Ticked by default. The screen says whether the update servers can be reached; if they still can't be reached after the network setup, the updates are skipped.
   * **Mirror the system onto a second drive (MD RAID 1)**: only on servers installed from the :ref:`media-md` that have a second, unused drive at least as big as the first. Ticked by default. Check **Drive to add**: everything on that drive is erased.
   * **Enable Cockpit (web console on port 9090)**: not ticked by default. See :ref:`cockpit`.

   .. image:: /images/vicibox13/firstboot-console-welcome.png
      :alt: The Welcome to ViciBox screen on the console, with the updates, RAID mirror and Cockpit options
      :width: 560

#. Press **Start** (:kbd:`F10`). If the RAID mirror is ticked, confirm the drive to erase with **Erase and mirror**.

   .. image:: /images/vicibox13/firstboot-console-erase.png
      :alt: Confirming the drive the mirror erases
      :width: 560

#. The network setup opens next. ViciDial is tied to the IP it is installed with, so give the server its final, static IP, hostname, DNS servers and gateway now; see :ref:`network-setup` for the steps. To keep the network as it is, press **Continue** (:kbd:`F10`) instead of applying changes.

   .. image:: /images/vicibox13/firstboot-console-network.png
      :alt: Network setup during the first boot, with Continue
      :width: 560

#. The rest of the setup runs in a log window: updates, Cockpit, the RAID mirror, and preparing the server for ViciDial (database directory, firewall zones, PHP time zone and mail settings).
#. When the log says **First boot setup finished**, press **Back to the menu**. The manager's main menu opens; quit it with :kbd:`q` or :kbd:`F9`. The mirror keeps copying in the background.

   .. image:: /images/vicibox13/firstboot-console-log.png
      :alt: First boot setup finished, with the second drive added to the mirror
      :width: 560

#. It is highly recommended to remove the installation media and reboot. To reboot, type ``reboot`` and press :kbd:`Enter`.

If you press **Not now** instead of **Start**, nothing is changed and the setup is offered again at the next root login. Until it has finished, every root login starts it again; after that, ``vicibox`` opens the main menu directly.

A 4 GB swap file, ``/swapfile``, is created automatically during the first boot.

.. warning::
   **Reinstalling a mirrored server:** the installer only writes the drive it installs to, and offers to wipe the old mirror on the other drive (see above). If that is declined, the first boot stalls for about two minutes and then starts the *old* installation from the other drive. To recover, install again and accept the wipe, or wipe the other drive with ``wipefs -fa /dev/sdX`` from the :ref:`rescue-shell` first. A mirror left over from a different ViciBox release does no harm: **Software RAID** in the :ref:`manager` wipes it when the drive is added.

Congrats, ViciBox has been installed. Please remember the password you used as it will be needed in the next phase.

.. _rescue-shell:

Rescue Shell
------------
The install media also boots into a rescue shell, for repairs and for preparing drives. Pick **Rescue shell -- does not install** in its boot menu; network connectivity (DHCP) is brought up automatically. It does not install anything or touch a drive by itself: you get a root prompt, and typing ``exit`` reboots the server.

The shell has the tools for drives and RAID (``lsblk``, ``wipefs``, ``sgdisk``, ``parted``, ``mdadm``), file system repair (``fsck.ext4``, ``xfs_repair``), ``chroot``, ``scp`` and ``rsync``. It starts with a short list of common commands. For example, to get into an installed MD RAID server, to fix its boot loader or reset the root password:

.. code-block:: bash

   mdadm --assemble --scan
   mount /dev/md127 /sysroot
   for d in dev proc sys run; do mount --rbind /$d /sysroot/$d; done
   chroot /sysroot

Without the server's own ``mdadm.conf`` the mirror comes up as ``/dev/md127`` rather than ``/dev/md0``; ``cat /proc/mdstat`` shows the name. On an install without RAID, mount the root partition instead, I.E. ``/dev/sda3``. When done, leave the chroot with ``exit``, unmount with ``umount -lR /sysroot`` and type ``exit`` again to reboot.

For problems inside a system that still boots, the **recovery mode** entries under **Advanced options** in the installed server's own boot menu start it in single-user mode instead.
