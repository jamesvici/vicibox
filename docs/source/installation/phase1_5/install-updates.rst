.. _phase1_5-install-updates:

==================
Install Updates
==================

While not required, it is *highly* recommended to install updates. This will update the ViciBox installer used in phase 2 as well as any new bug fixes or security updates. Internet connectivity is required to install updates. If the server is used in a secured network without internet access, updates can be skipped. It's still recommended to at least install updates when the OS is first installed prior to securing the server.

Installing Updates
------------------

#. If not already, login as the ``root`` user to get to the **#** command prompt.
#. Type ``zypper up`` and press ``ENTER`` to start the update process.
#. A list of updates and a summary of them will be shown. Type ``Y`` and press ``ENTER`` to start downloading and installing updates.
#. Occasionally an update will ask if you want to view it's update notice. Press ``ENTER`` to continue if this happens.
#. While not strictly necessary, it's advised to reboot the server at this time. Type ``reboot`` and press ``ENTER`` to reboot the server.

Some alternative commands for ``zypper up`` is ``zypper inr`` and ``zypper dup``. The ``zypper inr`` variant installs recommended packages most likely specific for the hardware or host. The ``zypper dup`` one installs packages that require repository changes like when adding a new repository.

.. note:: It's not unusual for there to be up to 300 megs of updates depending on how old the system is. This can take a while to download and install depending upon the internet connection speed.

Screenshots
-----------
   Installing normal updates
      .. figure:: install-updates-1.png
         :alt: Install updates with zypper up
         :width: 665
      
   Installing recommended updates
      .. figure:: install-updates-2.png
         :alt: Install recommendations with zypper inr
         :width: 665
