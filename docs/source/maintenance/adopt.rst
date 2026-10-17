.. _adopt-cluster:

Adopt Cluster
=============

The manager tracks every server in the cluster in the ViciDial database: its roles, settings and ViciDial SVN revision. Servers installed with the manager are registered automatically. Servers installed with ViciBox 12 or earlier are not; the **Cluster** panel then says the cluster is a legacy cluster, or doesn't list the server.

**Adopt cluster** registers such a server, so that the manager can show it, keep it on the database's SVN revision (see :ref:`updates`), and rebuild it with **Restore Server** (see :ref:`restore`).

Steps
-----
Adopt the master database server first, then the other servers.

#. If not already, log in as the ``root`` user to get to the **#** command prompt.
#. Type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Adopt cluster** and press :kbd:`Enter`. It's greyed out once the server is registered.
#. Check the roles, which are detected from the server's configuration: **Master database**, **Slave database**, **Web server**, **Telephony server**.
#. Press **Register** and confirm.

The **Cluster** panel then lists the server with its roles and revision.
