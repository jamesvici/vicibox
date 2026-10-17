.. _black-list:

Black List
==========

The Black List blocks specific IP addresses from accessing the server. This is controlled through an IP List inside ViciDial called **ViciBlack**. This allows for easy administration, as the firewall can be controlled from the Admin interface. It can be combined with the :ref:`voip-bl` and :ref:`geo-block`.

Setup
-----
#. In ViciDial, enable the IP List feature under :menuselection:`Admin --> System Settings`.
#. Log in as ``root``, type ``vicibox`` and press :kbd:`Enter` to start the :ref:`manager`.
#. Select **Firewall** and press :kbd:`Enter`.
#. Tick **Firewall on** and **ViciBlack list (ViciDial Admin > IP Lists)**, plus any other block lists you want.
#. Press **Apply** and confirm.

Control
-------
The Black List is controlled through the **ViciBlack** IP list. This can be found by going to :menuselection:`Admin --> IP Lists`. The format is simple, with one IP or CIDR network per line. Changes are loaded the next time ``VB-firewall`` runs; see :ref:`firewall`.

.. code-block:: none
   :caption: Sample Black List entries

   203.0.113.25
   198.51.100.0/24
