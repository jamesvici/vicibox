==============
Specifications
==============

CPU requirements are pretty lax for ViciDial. Anything newer then an AMD Zen1 (Ryzen 1000/Epyc 7001) or Intel Sandy Bridge (i3-2300/E3-1200) will work. The database will get the most benefit from multiple and faster CPU cores then anything else.

ECC memory is not required but highly recommended. You can potentially do without ECC memory on the telephony servers since they should be rebooted daily in most cases.

SATA SSD is the recommended minimum for all drives used. Given how inexpensive SSDs are in the 500GB to 1TB size range there really is no reason to be using spinning drives. The only use case for spinning drives in ViciDial would be in an archive server or NAS where you need tens to hundreds of terabytes of bulk storage.

RAID1 is also highly recommended for all servers. This can be accomplished through either a hardware RAID card or through two drives and the use of a software RAID. ViciBox has installation images available for both.

.. _specs-minimum:

Minimum
-------
* Quad (4) Core CPU 2.0+Ghz
* 8-GB RAM
* 160-GB storage

.. _specs-recommended:

Recommended
-----------
* Quad (4) Core CPU  2.0+Ghz
* 16-GB RAM
* 500-GB storage


.. _specs-database:

Dedicated Database for 150-Agents
=================================
    * Octal (8) Core CPU 2.0+Ghz
    * 32-GB RAM
    * 500-GB storage


.. _specs-database-large:

Dedicated Database for 300-Agents
=================================
    * Sedecim (16) Core CPU 3.0+Ghz
    * 64-GB RAM
    * 500-GB NVMe storage

