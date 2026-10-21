.. ViciBox documentation master file

.. image:: ./images/Vicibox_pixel_green_whitebg_20180921.png
   :align: center
   :alt: The ViciBox Logo
   :width: 320

ViciBox |release| Documentation
===============================

.. warning::

   **Security notice for ViciBox 12.0:** two critical PHP vulnerabilities (CVE-2026-109618 and CVE-2026-109619) allow unauthenticated remote code execution. Every ViciBox 12.0 server needs to be upgraded to PHP 8.2.35 or later. See `ViciBox 12.0 PHP remote code execution (php2shell) <https://docs.vicibox.com/en/12.0/bugfix/bugfix120-2.html>`__ for the fix.

ViciBox is the official installation image for the `ViciDial® Call Center Suite <https://www.vicidial.org/vicidial.php>`__.

Official support is available through the `ViciDial Group <https://www.vicidial.com>`__.

Free community-based support is available on the `ViciDial Forums <https://www.vicidial.org/VICIDIALforum/index.php>`__.

ViciBox |release| is based upon the `openSUSE Leap 16.0 <https://www.opensuse.org/#Leap>`__ distribution. The official `openSUSE Documentation <https://doc.opensuse.org/>`__ is also available online.

Leap 16.0 no longer includes YaST, so ViciBox |release| comes with its own administration program, the :ref:`manager`. The :ref:`manager` is designed to be easy to use and simplify the most common configuration tasks.

Coming from an earlier ViciBox? :ref:`whats-new` lists what changed.

.. _previous-manuals:

Previous Versions
-----------------
This manual covers ViciBox |release|. The manuals for earlier releases, including their bug fixes and errata, are still available:

* `ViciBox v.12.0 Documentation <https://docs.vicibox.com/en/12.0/>`__
* `ViciBox v.11.0 Documentation <https://docs.vicibox.com/en/11.0/>`__

.. toctree::
   :maxdepth: 2
   :caption: Contents

   introduction
   installation
   manager
   networking
   selinux
   maintenance
   bugfixerrata
