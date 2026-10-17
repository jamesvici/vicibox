.. _network-setup:

Network Setup
=============

While not necessary, it is highly recommended to use a static IP. Once ViciDial is installed, its configuration will be tied to the current LAN and WAN IP. If those IPs change, then ViciDial's configuration must also change to match. While not usually a problem with a LAN, a static IP is very important for the WAN. This static WAN IP is what will allow ViciDial to work reliably behind firewalls and with SIP carriers.

This might not be a problem if the ISP doesn't rotate the IPs that often. My residential cable modem ISP seems to rotate the IP every 30 days. Still, the cost to get a static IP is usually worth what a few hours of unexpected downtime in the middle of the day will be.

The IP address, net mask, and default gateway will be unique to your network and is beyond the scope of this document. While the DNS servers listed in the below example can be used safely it might be better to use the local router or ISP for DNS instead.

If there is a LAN and WAN network connected to the server then the WAN's default gateway should be used. There should only ever be one default gateway on the server no matter how many networks it is connected to.

If this server is to be used in a ViciDial cluster then each server must have a unique hostname. The recommended convention is 'DBX', 'webX', and 'dialerX'. For example, a basic three server cluster would use the hostnames 'DB1', 'web1', and 'dialer1'. An additional Telephony server would be 'dialer2', etc. Please limit the hostname to 16 characters or less.

Network Settings
----------------
.. list-table:: Example Network Configuration
   :widths: 30 70
   :header-rows: 1
   :align: center

   * - Setting
     - Value
   * - Host Name
     - vicidocs
   * - IP Address
     - 192.168.122.47/24 (subnet mask 255.255.255.0)
   * - Default Gateway
     - 192.168.122.1
   * - DNS Servers
     - 192.168.122.1
   * - Firewall Zone
     - public

.. note::
   While the server supports IPv6 ViciDial itself has not been extensively tested with it. Therefore the documentation will assume IPv4 only for all networking.

The Network Setup Screen
------------------------
The network is set up with **Network setup** in the :ref:`manager`, which replaces ``yast lan`` from earlier releases. The screen shows the server-wide settings (hostname, DNS and default gateway) at the top, and below them every network card (NIC) and bond in the server with its addressing, VLANs and link state. The settings are saved as NetworkManager connections, the network service ViciBox |release| uses.

Nothing changes while you edit: the changes are collected, shown for review, and only then applied. If the new settings cut off your connection, they are rolled back automatically after two minutes, so a typo in the gateway can't lock you out of a remote server.

The overview has a button for each step; the keys below do the same.

.. list-table:: Network setup buttons and keys
   :widths: 25 20 55
   :header-rows: 1
   :align: center

   * - Button
     - Key
     - Action
   * - **New bond**
     - :kbd:`F3`, :kbd:`b`
     - Create a new bond
   * - **Edit**
     - :kbd:`F4`, :kbd:`e`
     - Edit the highlighted NIC or bond
   * - **Delete**
     - :kbd:`F5`, :kbd:`d`
     - Delete the highlighted NIC's configuration or bond (press again to undo)
   * - **Global**
     - :kbd:`F7`, :kbd:`g`
     - Edit the hostname, DNS and default gateway
   * - **Back**
     - :kbd:`F8`, :kbd:`Esc`
     - Leave without changing anything (asks first if there are unsaved changes)
   * - **Review & apply**
     - :kbd:`F10`, :kbd:`a`
     - Review and apply the changes

During the first boot setup, **Review & apply** reads **Continue** until something is changed: press it to keep the network as it is.

Static IP Steps
---------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Network setup** and press :kbd:`Enter`.
#. Using the up and down arrow keys, highlight the network interface to configure, I.E. ``eth0``, and press **Edit** (:kbd:`F4`).

   .. image:: /images/vicibox13/network-overview.png
      :alt: The Network setup overview with one NIC and the Edit, Delete, New bond, Global, Back and Review & apply buttons
      :width: 720

#. Under **Untagged network**, select **Static**.
#. In **IP address / prefix**, type in the static IP address with its prefix, I.E. ``192.168.122.47/24``. The prefix is the subnet mask in CIDR form: ``/24`` is ``255.255.255.0``.
#. If this network needs routes other than the default gateway, enter them in **Static routes**, I.E. ``10.0.0.0/8 via 192.168.122.254``, separated by commas. Most servers need none.
#. Under **Firewall zone**, pick the zone for this network. Use **public** for an interface connected to the internet and **internal** or **trusted** for a private LAN; see :ref:`firewall-zones`.

   .. image:: /images/vicibox13/network-edit-static.png
      :alt: Editing a NIC set to a static address, with static routes, firewall zone and VLANs
      :width: 720

#. Press **Save** to return to the network overview.
#. If you have multiple networks, repeat the previous six steps for each additional network interface.
#. Press **Global** (:kbd:`F7`) to edit the global settings.
#. In **Hostname**, type in the name for this server, I.E. ``vicidocs``.
#. In **DNS servers**, type in the DNS servers separated by commas, I.E. ``192.168.122.1``.
#. In **Default gateway**, type in the default gateway, I.E. ``192.168.122.1``.

   .. image:: /images/vicibox13/network-global.png
      :alt: The Hostname, DNS and default gateway screen
      :width: 720

#. Press **Save** to return to the network overview.
#. Press **Review & apply** (:kbd:`F10`) to review the changes. The review lists the NetworkManager profiles that will be written and any problems found, such as a default gateway that isn't on any of the networks configured here. Fix any problems before continuing.

   .. image:: /images/vicibox13/network-review.png
      :alt: The Review network changes screen with the NetworkManager profiles to write
      :width: 720

#. Press **Apply** and confirm. If you are connected via SSH and changed the IP you are connected to, reconnect to the new IP now.
#. When asked **Can you still reach this server as expected?**, press **Keep**. If nothing is pressed within two minutes, or you press **Revert**, the previous settings come back.

   .. image:: /images/vicibox13/network-keep.png
      :alt: The prompt asking whether the server can still be reached, with Revert and Keep and a countdown
      :width: 720

#. Log out and back in as root for the hostname change to take full effect on the command prompt, I.E. **vicibox13\:~ #** becomes **vicidocs\:~ #**.
#. Verify the network is connected by pinging some hosts, I.E. ``ping -4 google.com``. Press :kbd:`Ctrl+C` to stop the ping.

If only certain aspects of the network need to be modified, for instance changing the hostname or DNS servers, then only the steps related to that setting need to be done. For example, to change the hostname select **Network setup**, press **Global**, change **Hostname**, press **Save**, then press **Review & apply** and **Apply**.

Changing the IP of an Installed Server
--------------------------------------
If ViciDial is already installed and the IP it uses changes, the manager notices after the change is applied and offers to **Move ViciDial** to the new IP. This updates the ViciDial database (servers, phones, conferences and the like) and the manager's own cluster records. Reboot afterwards so every service picks up the new IP. Other servers in the cluster and phones that point to the old IP need updating separately.

Bonds and VLANs
---------------
A bond joins two or more NICs into one link for redundancy. Press **New bond** (:kbd:`F3`), tick at least two NICs and pick a bond mode:

* **Active-backup** works with any switch: one NIC carries the traffic and another takes over if it fails.
* **LACP 802.3ad** combines the NICs for more bandwidth, but the switch ports must be configured for LACP.
* **Adaptive load balancing** spreads traffic across the NICs and works with any switch.

The bond is then configured like a NIC. NICs that become part of a bond lose their own configuration.

VLANs are added on the edit screen of a NIC or bond under **VLANs on this interface (tagged)**: press **Add VLAN** and enter the VLAN ID, its addressing and its firewall zone. If an interface only carries VLANs, set its **Untagged network** to **No address**.
