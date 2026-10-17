
Foreword
========

This documentation is for the IT professional or sysadmin tasked with installing and maintaining ViciBox, focusing on back-end aspects that integrate with ViciDial. It does not cover ViciDial administration such as creating users, loading leads, configuring campaigns, etc. The goal is to get ViciBox to the point where those things are all that's left.

For ViciDial administration, we recommend downloading the official manuals. There is an Agent and Manager manual which cover all aspects of their respective web interfaces. They are available in either a free low-resolution black and white version or a high-resolution color paid-for version. The manuals are available at `Eflo.net <http://eflo.net/store.php>`_.

While this documentation aims to be complete, it will never cover everything. That is why the ViciBox manual was recreated as a GitHub project. This allows anyone to submit changes and additions to the manual for review. Who knows, the next one who benefits from what you submit might just be future you the next time you run into a problem. Ask me how I know.

Recommended Skills
------------------

This documentation is designed to help those who are new or inexperienced with ViciBox and not necessarily Linux itself. If you have never installed Linux before, it might be a good idea to find someone more experienced to help you. The good news is basic Linux experience will likely be enough to follow along with these instructions.

For network experience, you will need a decent understanding of what a LAN/WAN is and how a basic NAT firewall works. If you have never done a port forward before, then it might be a good idea to find someone more experienced to help you. ViciDial is very sensitive to its networking environment, so it's important that it be properly implemented.

Installing and setting up ViciBox is done from the command line, mostly through the :ref:`manager`. While this can be done directly from the server's console, it's highly recommended to connect via SSH: the manager uses colour and the mouse over SSH, while the server's own console is limited to 80x25 characters and eight colours. You can use a stand-alone SSH client like `Putty <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ or the built-in ``ssh`` command if your operating system supports it.

Reading Guide
-------------

In order to remove as much ambiguity as possible, a certain syntax or style has been implemented. It is there to help readers understand what the intent of that instruction is. The following table shows how this style is implemented, what the intent is, along with a working example.

.. tabularcolumns:: p{0.132\linewidth}p{0.198\linewidth}p{0.330\linewidth}
.. list-table:: Style and Syntax Example
   :name: reading-guidelines
   :widths: 60 170 80
   :class: longtable
   :header-rows: 1
   :align: center

   * - As Written
     - Intention
     - Example
   * - some **Prompt**
     - Look for the Prompt to come up on the CLI or console
     - at command prompt **#**
   * - type ``this``
     - Type everything in the block on the keyboard
     - type ``vicibox`` and
   * - press :kbd:`Key`
     - Press the corresponding key, do not type out K E Y
     - press :kbd:`Enter`
   * - press :kbd:`Tab`
     - You may need to press the tab key multiple times
     - press :kbd:`Tab` to move
   * - press :kbd:`Key1+Key2`
     - Press Key1 and Key2 at the same time
     - press :kbd:`Ctrl+C` to stop
   * - select **Item**
     - In the :ref:`manager`, move to the item with the arrow keys or :kbd:`Tab` and press :kbd:`Enter` (or click it)
     - select **Network setup**
   * - tick **Option**
     - Move to the checkbox and press :kbd:`Space` or :kbd:`Enter` so it shows an **X**
     - tick **Web server**
