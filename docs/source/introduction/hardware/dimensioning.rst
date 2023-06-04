Dimensioning
************
    Server Scaling and Dimensioning is one of the hardest parts of ViciDial. The specifications provided are more of a guideline then a hard rule. ViciBox and ViciDial itself will run on anything you can install it to. If you're just doing sandbox testing or dev work then literally anything will work.
    
Telephony Server
================
    Use the :ref:`specs-minimum` hardware specification if there is no call recording.

    Use the :ref:`specs-recommended` hardware specification if there is call recording.
    
    Both the above hardware specifications will allow for 25-agents and 125-trunks of capacity per server when using predictive dialing. For an inbound-only call center or one with minimal to no predictive dialing the above hardware specifications will allow for 50-agents and 250-trunks of capacity per server.

    The biggest limitation is Asterisk, the telephony engine used in ViciDial. This is due to locking issue with Asterisk's internal channels. A channel is any connection between the Asterisk core process and any endpoint or module. For example, a logged in agent is using two channels. One channel for their phone connection and one channel for the meetme conference. Every call placed or received through a SIP Carrier also creates its own channel. Starting a call recording uses a channel as well. At any one time a single agent can be using up to 6 channels in Asterisk. The more channels you have and the more activity you have on them is what drives the locking issue. This is especially prevalent with automated predictive dialing methods where a large number of channels are simultaneously created and generating a lot of activity with the Asterisk core. It's why 5 is the recommended calls per second for for most telephony servers. Asterisk also does not scale linearly with CPU performance. For example, a quad-core CPU might start having issues around 25-agents but an octal-core CPU might only get you up to 30-agents.

    The second consideration with a telephony server centers around call recordings. The process of recording a call is initally done to a temporary RAM drive before being compressed to MP3 and written to the actual drive. Both of these processes require significantly more RAM and drive space. More memory might be needed if the calls are long (more then 30 minutes on average) or there are a high number of inbound calls. Drive size is mostly dictated by how many recordings you generate per day and the size of the recordings. If the recordings are not being offloaded to an archive server or NAS then it might be better to install a 2TB or larger drive. This is essentially required if it's a single-server ViciBox Express installation.

Web Server
==========
    The :ref:`specs-minimum` hardware specification is fine for 75 or so agents with SSL. Memory will likely need to be increased more then anything else.
    
    The :ref:`specs-recommended` hardware specification is good for 150 or so agents with SSL. Once you start going above 150 agents I would just add RAM or CPU as you need it until you hit the TCP port limit. Drive storage needed for a web server is very minimal so the 500G drive listed in this spec is probably more then needed.

    The ultimate limiting factor in a Web server is the number of available TCP ports. Apache, the web engine used in ViciBox, is configured to use all available TCP ports between 1024 and 65535. Once all of these ports are in use the web server essentially becomes unreachable for any new requests. Determining when you will hit this limit is difficult. It is dependant upon multiple factors such as how many agents you have, the features enabled in the agent interface, how much API use (or abuse) you are doing, and how long it takes for the database to respond with results. When this limit is finally hit there is no fix other then to have multiple web servers.

    Apache itself mostly scales through available RAM followed by CPU performance. SSL in particular tends to be quite resource intensive and can easily cut the servers capacity in half. Fortunately memory and CPU is relatively cheap.

Database Server
===============
    The :ref:`specs-recommended` hardware specification is good up to about 75 agents as a dedicated database.

    The :ref:`specs-database` hardware specification is good up to about 150 agents.
    
    The :ref:`specs-database-large` hardware specification is good up to about 300 agents.

    The limiting factor of the database is the memory table type in MariaDB. The memory table is a single-threaded table that runs exclusively in RAM. They are used for temporary tracking info and statistics within ViciDial. What happens is eventually this single thread cannot read the data from RAM, parse it, and return results fast enough. This results in queries being locked and delayed waiting to run against the table. Eventually this delay becomes great enough that it prevents ViciDial from operating correctly. Faster raw CPU speed helps but once you hit 5 or so Ghz there's no where left to go. In that situation the recommendation is to split the cluster into two smaller clusters. The good news is this isn't really an issue until you get to around 450 to 500 agents.
    
    Memory is probably the best performance to value option with a database up to 64G. Everything after 64G or RAM is less effective due to the heavy write nature of ViciDial. In other words if 90% of the database load is all within the same 500-megs of data on the drive then there's only so much you can do with cache and buffers. Eventually the database just gets stuck waiting to read/write data from/to the drive. 

    For the drives it's recommended to use either a prosumer or enterprise grade drive. The Samsung Pro or Western Digital Black line of SSD drives are good examples of prosumer grade drives. An example of an enterprise grade drives would be the Intel Optane or Samsung PM lines. The primary drive metric you are looking for is mixed or random IO writes. ViciDial is very write intensive for a database application and random writes are what it does the most. The performance of even a basic SATA SSD is good enough for most smaller clusters. The second consideration with SSDs is their write endurance. This is why the prosumer grade or higher drives are recommended as their write endurance is much better. This is thanks to the use of MLC or TLC cells in the SSD as opposed to cheaper QLC cells.

    