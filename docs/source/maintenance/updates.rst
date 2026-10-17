.. _updates:

Updates
=======

There are two kinds of updates on a ViciBox server: openSUSE package updates, which cover the operating system, Asterisk, MariaDB, the ViciBox packages and everything else installed from the repositories, and ViciDial updates, which come from ViciDial's SVN repository. The **Updates** panel of the :ref:`manager` shows how many of each are waiting.

System Updates
--------------
While not required, it is *highly* recommended to install updates. This will update the ViciBox manager and the other ViciBox packages as well as install bug fixes and security updates. Internet connectivity is required to install updates.

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **System updates (zypper)** and press :kbd:`Enter`.
#. Pick what to run. The list underneath shows what each choice would change:

   * **System update (zypper up)** installs updated versions of the installed packages. This is the normal choice.
   * **Distribution upgrade (zypper dup)** also allows package changes that need a vendor or repository change, for example after a repository was added or moved.
   * **New recommended packages (zypper inr)** installs packages recommended by what's already installed, often hardware drivers or firmware.

   .. image:: /images/vicibox13/updates-preview.png
      :alt: System updates with System update (zypper up) selected and the packages it would update
      :width: 720

#. Press **Run** and confirm. The update runs in the log window.
#. If the kernel or core libraries were updated, reboot the server: quit the manager with :kbd:`q`, then type ``reboot`` and press :kbd:`Enter`.

The same updates can be installed from the command prompt with ``zypper up``, ``zypper dup`` or ``zypper inr``.

.. note::
   It's not unusual for there to be several hundred megabytes of updates depending on how old the system is. This can take a while to download and install depending upon the internet connection speed.

ViciDial Updates
----------------
ViciDial is installed from its SVN repository, and every server in a cluster must run the same ViciDial SVN revision as the database. The **Cluster** panel of the manager shows each server's revision and flags any that don't match.

ViciDial updates are done in two steps: first on the master database server, which upgrades the database schema and moves the whole cluster to the new revision, then on every other server.

On the master database server (or an Express server):

#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **ViciDial update (SVN)** and press :kbd:`Enter`.
#. The screen shows this server's revision, the cluster's revision and the latest revision available, with the list of changes in between. **Update to revision** defaults to the latest; type in an older revision number to stop short of it.

   .. image:: /images/vicibox13/vicidial-update-master.png
      :alt: ViciDial update on the master database with the revisions and the list of changes
      :width: 720

#. Leave **Back up the database first** ticked. The backup is written to ``/root/vicibox-asterisk-DATE-rREVISION.sql`` before anything changes.
#. Press **Update** and confirm. The database schema is upgraded and ViciDial's ``install.pl`` runs on this server.

Then on each web and telephony server in the cluster:

#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **ViciDial update (SVN)** and press :kbd:`Enter`. The screen shows that the server is behind the cluster's revision.

   .. image:: /images/vicibox13/vicidial-update-member.png
      :alt: ViciDial update on a telephony server that is behind the cluster revision
      :width: 720

#. Press **Update** and confirm. The server is updated to exactly the cluster's revision.
#. Reboot the server once it's done.

.. warning::
   A server must never run a newer ViciDial revision than the database, and going back to an older revision is not supported because the database schema can't be downgraded. Always update the master database first.
