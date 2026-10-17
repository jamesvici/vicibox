.. _cockpit:

Cockpit Web Console
===================

`Cockpit <https://cockpit-project.org/>`__ is a web-based console for the server: logs, services, storage, network, a terminal and resource graphs in a browser. ViciBox |release| includes it, but it is off by default. It is not needed for ViciDial; the :ref:`manager` remains the way to configure ViciBox.

Cockpit answers on TCP port 9090 over HTTPS. Log in with ``root`` and the root password.

Enabling Cockpit
----------------
The easiest way is the **Enable Cockpit** option on the **Welcome to ViciBox** screen at the first root login (see :ref:`phase1`). It starts Cockpit and opens port 9090 in the **internal** and **trusted** firewall zones only, so it can be reached from the LAN but not from the internet (see :ref:`firewall-zones`).

To enable it later, log in as ``root`` and run:

.. code-block:: bash

   systemctl enable --now cockpit.socket
   firewall-cmd --permanent --zone=internal --add-service=cockpit
   firewall-cmd --zone=internal --add-service=cockpit

The first ``firewall-cmd`` saves the change (``--permanent``) and the second applies it to the running firewall, instead of a ``firewall-cmd --reload``. The **trusted** zone needs no change: it already lets everything in.

.. warning::
   Avoid ``firewall-cmd --reload`` on a telephony server. A reload rebuilds the firewall's IP block lists, and the VoIP Blacklist alone holds about 100,000 addresses: firewalld can take several minutes to rebuild them, and meanwhile it drops every connection, SSH included.

Then browse to ``https://SERVER-IP:9090/``. The browser warns about the certificate until a real one is installed.

.. warning::
   Don't open port 9090 in the **public** or **external** zone. Cockpit gives full control over the server to anyone who has the root password.

To turn it off again, run ``systemctl disable --now cockpit.socket``.

Servers Installed From an Early 13.0 Image
------------------------------------------
Servers installed from the first ViciBox 13.0 images may have the ``cockpit-firewalld`` package, which opens Cockpit in the **public** zone, and opens it again whenever the package is updated. Check with ``rpm -q cockpit-firewalld``. If it is installed, remove it this way:

.. code-block:: bash

   zypper addlock cockpit-firewalld
   rpm -e --noscripts cockpit-firewalld
   for zone in public external; do
     firewall-cmd --permanent --zone=$zone --remove-service=cockpit
     firewall-cmd --zone=$zone --remove-service=cockpit
   done

.. warning::
   Don't remove it with ``zypper remove`` or a plain ``rpm -e``: the package's own removal script runs ``firewall-cmd --reload``, which locks a telephony server out for several minutes (see above).
