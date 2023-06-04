Example Installs
****************
    All the following examples are using the :ref:`specs-recommended` hardware specification unless noted otherwise. Predictive Dialing is also assumed to be in use with a 5:1 dialing ratio. If the call center is inbound only or uses very minimal to no predictive dialing then you can also double the agent and trunk capacity shown.

15-Agent / 75-Trunk ViciBox Express
===================================
    * All-In-One install, best for small call centers
    * 75 trunk capacity
    * Recommend using a 2TB drive if you want call recordings

75-Agent / 375-Trunk ViciDial Cluster
=====================================
    * Three telephony servers
    * One web server
    * One database
    * Optionally an archive server or NAS to offload the recordings to

150-Agent / 750-Trunk ViciDial Cluster
=======================================
    * Six telephony servers
    * One web server
    * One database server using the :ref:`specs-database` hardware specification
    * Optionally a second database server doing replication for reporting and backup

300-Agent / 1500-Trunk ViciDial Cluster
=======================================
    * Twelve telephony servers
    * Two web servers to split agents onto
    * One database server using the :ref:`specs-database-large` hardware specification
    * Optionaly a load balancer to distribute agent connections
    * Optionally a second database server doing replication for reporting

