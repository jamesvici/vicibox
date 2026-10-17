.. _firewall:

Firewall
=========

ViciBox uses firewalld for its firewall. On top of it, ``VB-firewall`` loads IP lists into the firewall: lists of addresses to block, or, in the stricter modes, the only addresses allowed in. Each list is designed to handle a specific use case that comes up in a VoIP environment, and some can be combined.

On ViciBox |release| the firewall is turned on by the installer for every server except a dedicated database server. Telephony servers start with the :ref:`voip-bl` loaded, which downloads and maintains a list of known SIP abusers. While effective, it's important to understand what the firewall is doing and how to configure it properly.

.. list-table:: Firewall lists
   :widths: 25 75
   :header-rows: 1
   :align: center

   * - List
     - What it does
   * - :ref:`black-list`
     - Blocks the addresses in ViciDial's **ViciBlack** IP list
   * - :ref:`voip-bl`
     - Blocks the community-maintained list of known SIP abusers from voipbl.org
   * - :ref:`geo-block`
     - Blocks whole countries
   * - :ref:`white-list`
     - Allows only the addresses in ViciDial's **ViciWhite** IP list (and the LAN); everyone else is locked out
   * - :ref:`dynamic-portal`
     - Allows only the addresses of agents who logged in to the dynamic portal

The three block lists can be combined with each other. The two allow-only lists can be combined with each other, but turn the block lists off: when only listed addresses can connect, there is nothing left to block.

Configuring the Firewall
------------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`. The **Security** panel shows whether the firewall is running and which lists it uses.
#. Select **Firewall** and press :kbd:`Enter`.
#. Tick **Firewall on** to run the firewall, or untick it to turn it off completely.
#. Tick the lists to use. For **Geo blocking by country**, also fill in **Blocked countries**.
#. Leave **Load the lists now** ticked to load the lists straight away; otherwise they are loaded at the next scheduled run.

   .. image:: /images/vicibox13/firewall.png
      :alt: The Firewall screen with the VoIP Blacklist on and the number of entries in each IP set
      :width: 720

#. Press **Apply** and confirm.

The manager writes the chosen options into the ``VB-firewall`` lines of root's crontab, which load the lists at boot and then reload them on a schedule. With the White List or the Dynamic Portal on, they reload every minute, so an address added to the White List or an agent who just logged in to the portal gets in within a minute. With only the block lists, they reload every 6 hours, since the VoIP Black List is a large download. A schedule you changed by hand in the crontab is left as it is. To pick up a change to a block list straight away, run **Firewall** again with **Load the lists now** ticked. The screen also shows how many entries each list currently holds.

.. warning::
   An allow-only list with the wrong entries locks everyone out, including you. Before turning on the White List or the Dynamic Portal, make sure the address you connect from is on the White List or in the **trusted** or **internal** zone (see :ref:`firewall-zones`), or that you have console access to the server.

Running VB-firewall by Hand
---------------------------
``VB-firewall`` can also be run from the command prompt. Add ``--test`` to see what it would change without changing anything:

.. code-block:: bash

   VB-firewall --black --voipbl --test

Run ``VB-firewall --help`` for all options.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   firewall/ports
   firewall/zones
   firewall/whitelist
   firewall/blacklist
   firewall/dynamic
   firewall/voipbl
   firewall/geoblock
