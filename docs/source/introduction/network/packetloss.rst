Packet Loss
***********
    VoIP, especially SIP, is very sensitive to packet loss. Typically any packet loss above 2-3% will start to result in significant audio quality issues. This will usually start as choppy audio or what sounds like clipping/stuttering. While less common it might also manifest as chirping noises. The general rule is the greater the number of hops the more likely and worse the packet loss will be. This loosely tracks with geographical distance. For instance, going from New York to the Phillipines will greatly increase your chances of packet loss as opposed to going from New York to Los Angeles.
    
    Generally there is very little you can do about packet loss as it mostly seems to happen in the middle of the internet. Very rarely is the issue within your network or even your ISP's network. If your ISP is a large regional cable modem provider then you are basically stuck waiting it out. If you are in an enterprise network space like a Data Center or Colocation Facility then they might be able to help. It will depend upon how close the bad hop is to their network and if they have any alternate routing paths available. The good news is that packet loss is bad for everybody so things will generally correct themselves pretty quickly.
    
    When Packet Loss occurs it will show up on the graph as a red shaded loss with every hop after it having a similar amount of loss. That means that the packet loss occurring at that hop is translating into packet loss at all the hops after it. If a hop is red showing packet loss, but all the hops after it don't have a similar amount of packet loss, then it's just that hop ignoring pings. Ignoring pings on routers is common as pings are viewed as a nuisance resource hog.

Example
=======
    This screenshot shows packet loss occuring at hop 4. You can tell because all hops after hop 4 have similar levels of packet loss. Real packet loss is always inherited to all the hops after it.

    .. image:: pingplotter-packetloss.png
        :align: center
        :alt: PingPlotter Screenshot with Packet Loss

