.. _phase1_5-install-updates:

Install Updates
===============

While not required, it is *highly* recommended to install updates before installing ViciDial. This updates the ViciBox manager used in Phase 2 as well as installing any new bug fixes or security updates. Internet connectivity is required to install updates. If the server is used in a secured network without internet access, updates can be skipped. It's still recommended to at least install updates when the OS is first installed, prior to securing the server.

Installing Updates
------------------
#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **System updates (zypper)** and press :kbd:`Enter`.
#. Leave **System update (zypper up)** selected. The list below shows the packages it would update. Press **Run** and confirm with **Go**.

   .. image:: /images/vicibox13/updates-preview.png
      :alt: System updates with zypper up selected and the packages it would update
      :width: 720

#. The update runs in the log window and ends with **Updates finished**.

   .. image:: /images/vicibox13/updates-done.png
      :alt: The finished update in the log window
      :width: 720

#. When the update finishes, quit the manager with :kbd:`q` and reboot the server: type ``reboot`` and press :kbd:`Enter`.

If the manager itself was updated, it's restarted by starting ``vicibox`` again after the reboot. More on the update options, including ViciDial updates once it's installed, is in :ref:`updates`.
