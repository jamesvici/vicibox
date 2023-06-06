Configure Static IP
===================
   While not necessary it is highly recommend to use a static IP whenever possible. The IP address, net mask, and default gateway will be unique to your network and is beyond the scope of this document. While the DNS servers used in this example can be used safely it might be better to use the local router or ISP DNS servers instead. This example will be using the following:
   
   * Host Name : vicibox-docs
   * IP Address : 192.168.1.4
   * Subnet Netmask : 255.255.255.0 (/24)
   * Default Gateway : 192.168.1.1
   * Name Server 1 : 208.67.222.222
   * Name Server 2 : 208.67.220.220
      
   .. note:: If there is a LAN and WAN network connected to the server then the WAN default gateway should be used. There should only ever be one default gateway on the server no matter how many networks it is connected to.

yast lan
--------
   #. If not already, login as the 'root' user to get to the command prompt.
   #. Type ``yast lan`` to start the network configuration.
   #. Press the ``TAB`` key until the network interface is highlighted.
   #. If there are multiple network interfaces, use the up and down arrow key to highlight the correct network interface
   #. Press ``ALT``-``I`` to edit the highlighted network interface.
   #. Press ``ALT``-``T`` to select 'Statically Assigned IP Address'
   #. Press ``TAB`` or ``ALT``-``I`` to move to the 'IP Address' field.
   #. Type in the static IP address for this network interface, I.E. ``192.168.1.4``.
   #. Press ``TAB`` or ``ALT``-``S`` to move to the 'Subnet Mask' field.
   #. Type in the subnet mask for this network interface, I.E. ``255.255.255.255``. CIDR formats are also supported and can be typed in directly, I.E. ``/24``.
   #. Press ``ALT``-``N`` to continue back to the network overview.
   #. If you have multiple networks, repeat steps 3 through 11 for any additional network configurations needed.
   #. Press ``ALT``-``S`` to change to the Hostname/DNS configuration.
   #. Press ``ALT``-``T`` or ``TAB`` to move to the 'Static Hostname' field.
   #. Type in the server name for this server, I.E. ``vicibox-docs``
   #. Press ``ALT``-``1`` or ``TAB`` to move to the 'Name Server 1' field.
   #. Type in the primary DNS server's IP, I.E. ``208.67.222.222``.
   #. Press ``ALT``-``2`` or ``TAB`` to move to the the 'Name Server 2' field.
   #. Type in the secondary DNS server's IP, I.E. ``208.67.220.220``.
   #. If you have or a tertiary DNS server you can add it in the 'Name Server 3' field.
   #. Press ``ALT``-``R`` to change to the Routing configuration.
   #. You will likely receive a notification about adapting the network configuration for the new hostname. Press ``ALT``-``Y`` to make sure 'Yes' is selected and then press ``ENTER``.
   #. Press ``ALT``-``D`` to add a gateway to the server. The 'Default Route' option should be checked.
   #. Press ``ALT``-``G`` or ``TAB`` to move to the 'Gateway' field
   #. Type in the Default Gateway to use for this server, I.E. ``192.168.1.1``
   #. Press ``ALT``-``O`` or ``TAB`` to select the 'OK' button. You should see the newly added gateway listed as default
   #. Press ``ALT``-``O`` or ``TAB`` to select the 'OK' button to accept the network configuration and make changes. When it's finished you should be back at the command prompt. The basic network configuration is complete.

Screenshots
^^^^^^^^^^^
   Run yast lan
      .. image:: static-ip-1.png
         :alt: Login as root user, run 'yast lan'
         :width: 665

   Select network interface
      .. image:: static-ip-2.png
         :alt: Select the network interface to configure
         :width: 665

   Assign static IP
      .. image:: static-ip-3.png
         :alt: Select static IP and configure the IP Address and Subnet Mask
         :width: 665

   Configure DNS
      .. image:: static-ip-4.png
         :alt: Assign a meaningful hostname and DNS servers
         :width: 665

   Accept hostname change
      .. image:: static-ip-5.png
         :alt: Accept the new hostname and adapt the network configuration
         :width: 665

   Add a Default Route
      .. image:: static-ip-6.png
         :alt: Add a default route to the server
         :width: 665

   Single Default Route
      .. image:: static-ip-7.png
         :alt: Only one default gateway should exist
         :width: 665

   Save changes
      .. image:: static-ip-8.png
         :alt: Save changes and apply network configuration
         :width: 665