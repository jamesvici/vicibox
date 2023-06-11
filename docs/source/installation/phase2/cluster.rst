Cluster
=======
   ViciDial Setup Order
      * Database server
      * Web server
      * Telephony server

   All clusters start with the primary Database server since everything starts there. Afterwards the web server is installed to provide services needed by the Telephony server. Lastly the Telephony server is installed and will setup portions of ViciDial needed by other servers. Any additional servers can be setup after these three are working together as a cluster.

   The hostname for each server in a cluster is used as that server's name in the ViciDial database. Because of this each server must have a unique hostname. The recommended naming convention is to use 'DBX', 'webX', and 'dialX' as the prefix for the hostname, I.E. 'DB1', 'web1, 'dial1', etc. This designates the servers role as well as which one it is if there are multiple of that type in the cluster. How to change the hostname can be found in the :ref:`phase1_5-static-ip` section.
   
.. tip::
   While it might sound good to use greek gods, disney characters, or transformers for the hostname of your servers, don't. Being told that Optimus Prime went down but Megatron is handling it now is just confusing. And yes, that is based on a true story of an 11-server cluster. Optimius Prime was the primary database, Megatron was the replicated backup. Bumblebee was the web server and Starscream was their primary telephony server. No numbers either, so the second telephony server was Skywarp I think. Don't be that guy.

Planning
--------
   With ``vicibox-install`` the different roles of ViciDial can be ran on multiple servers. These servers can then connect with each other across the network to scale. By doing this a ViciDial Cluster can scale up to 500 agents.

   The examples in this section will be for the three initial servers needed to make a ViciDial Cluster. This is the starting point upon which any size cluster can be built. To add more servers just repeat the install as needed.

   If there are only two servers available for a cluster it is advised to have the Database and Web server role running on the more powerful of the two servers. To accomplish this the Web server role would also be selected during the setup of the Database. Fun fact, if you were to select all 3 roles on the same server you would end up with an :ref:`express`.

   A ViciDial cluster can only have one primary Database server. The primary Database server is what all Web and Telephony servers will connect to. More information on the Database server role is available in the :ref:`hardware` section.

   .. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
   .. list-table:: Cluster Information
      :name: server-network-info
      :widths: 60 80
      :class: longtable
      :header-rows: 1
      :align: center

      * - Server
        - IP Address
      * - DB1
        - 192.168.50.4
      * - web1
        - 192.168.50.6
      * - dial1
        - 192.168.60.10

.. include:: cluster-db.rst
.. include:: cluster-web.rst
.. include:: cluster-tel.rst

