Introduction
============

.. _introduction:

Foreward
--------

While this documentation aims to be complete there might be sections that are out of date or features that are undocumented. That is why the ViciBox documentation was moved to GitHub and implemented using Read The Docs. The goal is to encourage other contributors to help maintain the ViciBox documentation.


Knowledge and Skills
--------------------

The documentation is made to be user friendly for beginners but some basic knowledge is assumed. If you are not comfortable with basic network environments, working with a Linux shell, or editing configuration files it is highly recommended to find someone who is. You will also need to have a basic understanding of your network environment since everyones will be somewhat unique.

You will be required to interact with the command line interface in order to install and setup ViciBox. While this can be done directly from the server itself it's highly recommended to connect via SSH. You can use an SSH Client such as PuTTY or through the native 'ssh' command if your operating system supports it.

Hardware Specs
--------------

**Minimum** 
    * Four CPU Cores 2.0+Ghz
    * 8-GB RAM
    * 160-GB Drive

**Recommended Telephony and Web**
    * Six CPU Cores 2.0+Ghz
    * 16-GB ECC RAM
    * 500-GB RAID1 SSD

**Dedicated Database 150-Agents**
    * Eight CPU Cores 2.0+Ghz
    * 32-GB ECC RAM
    * 500-GB RAID1 SSD

**Dedicated Database 300-Agents**
    * Sixteen CPU Cores 3.0+Ghz
    * 64-GB ECC RAM
    * 500-GB RAID1 NVMe

Dimensioning
------------

Server Scaling and Dimensioning is one of the hardest parts of ViciDial. The biggest consideration is that the telephony portion of ViciDial does not scale vertically much past a modern quad-core CPU. Due to locking issues in the core of Asterisk there is a very high likelihood that Asterisk will deadlock or hang up once the channel load goes above 300 channels. In asterisk, a channel is any connection between the core and any other module or endpoint. An agent logging in creates one channel in Asterisk for their phone connection. The conference room for that same agent also uses a channel in asterisk. Every call placed in Asterisk also creates its own channel. At any one time a single agent can be using up to 6 channels. This is why the recommendation is to have 25 agents and 125 trunks per Telephony server.

The web server using the recommended hardware spec can support up to 150-agents in most scenarios. The limitation on the web server will usually be a port-exhaustion issue within the TCP stack itself. Until that point is reached though you can generally scale the web server vertically by adding more memory or bigger CPUs depending upon your load.

The limitation on the database server usually happens somewhere between 300-500 agents. The problem is a single-threaded locking issue related to memory tables in MySQL. There is no real way to address this issue other then to try faster CPUs and Memory. Even then it's all generally going to be single-digit percentile gains at that point. The suggestion is to look at splitting your cluster into multiple smaller clusters once this limit is reached.

Example Installs
----------------

**15-Agent ViciBox Express**
    * Single server with recommended hardware spec
    * 75-Trunk capacity
    * All-In-One install, best for small call centers

**75-Agent ViciDial Cluster** 
    * Three telephony servers using recommended hardware spec
    * One web server using recommended hardware spec
    * One database server using recommended hardware spec

**150-Agent ViciDial Cluster**
    * Six telephony servers using recommended hardware spec
    * One web server using recommended hardware spec
    * One database server using 150-Agent database hardware spec

**300-Agent ViciDial Cluster**
    * Twelve telephony servers using recommended hardware spec
    * Two web servers using recommended hardware spec
    * Optionaly a load balancer of some sort
    * One database server using 300-agent database hardware spec
    * Optionally a second database server doing replication for reporting




