
Static IP
=========

While not necessary, it is highly recommended to use a static IP. Once ViciDial is installed, its configuration will be tied to the current LAN and WAN IP. If those IPs change, then ViciDial's configuration must also change to match. While not usually a problem with a LAN, a static IP is very important for the WAN. This static WAN IP is what will allow ViciDial to work reliably behind firewalls and with SIP carriers.

This might not be a problem if the ISP doesn't rotate the IPs that often. My residential cable modem ISP seems to rotate the IP every 30 days. Still, the cost to get a static IP is usually worth what a few hours of unexpected downtime in the middle of the day will be.

The IP address, net mask, and default gateway will be unique to your network and is beyond the scope of this document. While the DNS servers listed in the below example can be used safely it might be better to use the local router or ISP for DNS instead.

If there is a LAN and WAN network connected to the server then the WAN's default gateway should be used. There should only ever be one default gateway on the server no matter how many networks it is connected to.

If this server is to be used in a ViciDial cluster then each server must have a unique hostname. The recommended convention is 'DBX', 'webX', and 'dialerX'. For example, a basic three server cluster would use the hostnames 'DB1', 'web1', and 'dialer1'. An additioner Telephony server would be 'dialer2', etc. Please limit the hostname to 16 characters or less.

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
     - 192.168.50.4
   * - Subnet Mask
     - 255.255.255.0 (/24)
   * - Default Gateway
     - 192.168.50.1
   * - Name Server 1
     - 208.67.222.222
   * - Name Server 2
     - 208.67.220.220

.. note:: 
   While the server supports IPv6 ViciDial itself has not been extensively tested with it. Therefore the documentation will assume IPv4 only for all networking.

YaST Network Configuration
--------------------------
#. If not already, login as the ``root`` user to get to the **#** command prompt.
#. Type ``yast lan`` to start the network configuration.
#. Press the ``TAB`` key until the network interface is highlighted.
#. If there are multiple network interfaces, use the up and down arrow key to highlight the correct network interface
#. Press ``ALT``-``I`` to edit the highlighted network interface.
#. Press ``ALT``-``T`` to select **Statically Assigned IP Address**
#. Press ``TAB`` or ``ALT``-``I`` to move to the **IP Address** field.
#. Type in the static IP address for this network interface, I.E. ``192.168.50.4``.
#. Press ``TAB`` or ``ALT``-``S`` to move to the **Subnet Mask** field.
#. Type in the subnet mask for this network interface, I.E. ``255.255.255.0``. CIDR formats are also supported and can be typed in directly, I.E. ``/24``.
#. Press ``ALT``-``N`` to continue back to the network Overview.
#. If you have multiple networks repeat steps 3 through 11 for any additional network interfaces needed
#. Press ``ALT``-``S`` to change to the Hostname/DNS configuration.
#. Press ``ALT``-``T`` or ``TAB`` to move to the **Static Hostname** field.
#. Type in the server name for this server, I.E. ``vicibox-docs``
#. Press ``ALT``-``1`` or ``TAB`` to move to the **Name Server 1** field.
#. Type in the primary DNS server IP, I.E. ``208.67.222.222``.
#. Press ``ALT``-``2`` or ``TAB`` to move to the the **Name Server 2** field.
#. Type in the secondary DNS server IP, I.E. ``208.67.220.220``.
#. If you have a tertiary DNS server you can add it in the **Name Server 3** field.
#. Press ``ALT``-``R`` to change to the Routing configuration.
#. You will likely receive a notification about adapting the network configuration for the new hostname. Press ``ALT``-``Y`` to make sure **Yes** is selected and then press ``ENTER``.
#. Press ``ALT``-``D`` to add a gateway to the server. The **Default Route** option should be checked.
#. Press ``ALT``-``G`` or ``TAB`` to move to the **Gateway** field
#. Type in the default gateway to use for this server, I.E. ``192.168.50.1``
#. Press ``ALT``-``O`` or ``TAB`` to select the **OK** button. You should see the newly added gateway listed as default
#. Press ``ALT``-``O`` or ``TAB`` to select the **OK** button to accept the network configuration and make changes. If you are connected via SSH you might be disconnected during this process and will need to connect to the new static IP in the next step.
#. Before continuing it is necessary to log out and back in as root for the hostname change to take full effect. In the below screenshots the command prompt goes from **vicibox11\:~ #** to **testBox1\:~ #**.
#. At this point the network should be connected. Verify by pinging some hosts, I.E. ``ping -4 google.com``.
#. Press ``CTRL``-``C`` to cancel the ping.

   If only certain aspects of the network need to be modified, for instance changing the hostname or DNS servers, then only the instructions related to that setting need to be ran.

   For Example, to change the hostname
      #. If not already, login as the ``root`` user to get to the **#** command prompt.
      #. Type ``yast lan`` to start the network configuration.
      #. Press ``ALT``-``S`` to change to the Hostname/DNS configuration.
      #. Press ``ALT``-``T`` or ``TAB`` to move to the **Static Hostname** field.
      #. Type in the server name for this server, I.E. ``vicibox-docs``.
      #. You will likely receive a notification about adapting the network configuration for the new hostname. Press ``ALT``-``Y`` to make sure **Yes** is selected and then press ``ENTER``.
      #. Press ``ALT``-``O`` or ``TAB`` to select the **OK** button to accept the network configuration and make changes.
      #. Before continuing with the rest of the setup it is necessary to log out and back in as root for the hostname change to take effect on the command line. In the below screenshots the command prompt goes from **vicibox11\:~ #** to **testBox1\:~ #**

Screenshots
-----------
   Run yast lan
      .. image:: static-ip-1.png
         :alt: Login as root user, run 'yast lan'
         :width: 640

   Select network interface
      .. image:: static-ip-2.png
         :alt: Select the network interface to configure
         :width: 640

   Assign static IP
      .. image:: static-ip-3.png
         :alt: Select static IP and configure the IP Address and Subnet Mask
         :width: 640

   Configure DNS
      .. image:: static-ip-4.png
         :alt: Assign a meaningful hostname and DNS servers
         :width: 640

   Accept hostname change
      .. image:: static-ip-5.png
         :alt: Accept the new hostname and adapt the network configuration
         :width: 640

   Add a Default Route
      .. image:: static-ip-6.png
         :alt: Add a default route to the server
         :width: 640

   Single Default Route
      .. image:: static-ip-7.png
         :alt: Only one default gateway should exist
         :width: 640

   Save changes
      .. image:: static-ip-8.png
         :alt: Save changes and apply network configuration
         :width: 640

   Verify connectivity and hostname change
      .. image:: static-ip-9.png
         :alt: Verify network connectivity and hostname chane
         :width: 640