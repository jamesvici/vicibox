Install Updates
===============
   While not required, it is *highly* recommended to install updates. This will update the ViciBox installer used in phase 2 as well as any new bug fixes or security updates. Internet connectivity is required to install updates. The initial update may take a while depending upon how many updates are available and how fast the internet connection is.

zypper up
---------
   #. If not already, login as the 'root' user to get to the command prompt.
   #. Type ``zypper up`` to refresh the system repositories and find updates.
   #. A list of updates and a summary of their size will be listed. Type in ``Y`` and press ``ENTER`` to accept the updates. This will start the download process.
   #. While not strictly necessary, it's advised to reboot the server at this time. Type ``reboot`` to reboot the server

Screenshots
^^^^^^^^^^^
   Run zypper up
      .. image:: new-updates-1.png
         :alt: Refresh repositories and fine new updates
         :width: 665

   Accept new updates
      .. image:: new-updates-2.png
         :alt: Accept new updates and install them
         :width: 665

   Reboot
      .. image:: new-updates-3.png
         :alt: Reboot for good measure for any system updates
         :width: 665