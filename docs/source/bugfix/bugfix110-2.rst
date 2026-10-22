11.0 Apache config files missing after vicibox-install update
*************************************************************
   ViciBox v.11.0 shipped a vicibox-install package that installed its Apache config files directly into ``/etc/apache2``. Newer vicibox-install packages keep their copies in ``/usr/share/vicibox`` instead and only copy them to ``/etc/apache2`` when they are missing. When a ViciBox v.11.0 server updates vicibox-install with ``zypper up``, the update makes a ``.old`` backup of each config file, but removing the old package then deletes the config files themselves. Config files that had been edited are renamed to ``.rpmsave`` instead. This applies to all releases of ViciBox v.11.0.

   The affected files are:

   * ``/etc/apache2/conf.d/mod_deflate.conf``
   * ``/etc/apache2/conf.d/audiostore.conf``
   * ``/etc/apache2/conf.d/viciarchive.conf``
   * ``/etc/apache2/conf.d/vicirecord.conf``
   * ``/etc/apache2/vhosts.d/0000-default.conf`` and ``0000-default-ssl.conf``, or the older ``1111-default.conf`` and ``1111-default-ssl.conf``

Symptoms
========
   Apache will not start, or the ViciDial web pages, recordings or archive are no longer reachable after running ``zypper up``. The dynamic portal includes ``mod_deflate.conf``, so ``apachectl configtest`` will report that it cannot find ``/etc/apache2/conf.d/mod_deflate.conf``. The files above will be missing, with only a ``.old`` copy, and possibly a ``.rpmsave`` copy, left behind.

The Fix
=======
   The below commands put back any of the ``conf.d`` files that are missing, using the ``.rpmsave`` copy if there is one and the ``.old`` copy otherwise.

   .. code-block:: bash
      :caption: Restore the conf.d files

      cd /etc/apache2/conf.d
      for f in mod_deflate audiostore viciarchive vicirecord; do
        [ -e $f.conf ] || { [ -e $f.conf.rpmsave ] && cp -p $f.conf.rpmsave $f.conf || cp -p $f.conf.old $f.conf; }
      done

   The default web site files need to be restored by hand, since a server only uses either the ``0000-default`` or the older ``1111-default`` files and restoring both would create two default web sites. List the directory to see which files the server used:

   .. code-block:: bash
      :caption: Check the default web site files

      ls /etc/apache2/vhosts.d/

   If ``0000-default.conf`` and ``0000-default-ssl.conf`` are missing but their ``.old`` or ``.rpmsave`` copies are there, copy them back. Use the ``.rpmsave`` copy if there is one. For example:

   .. code-block:: bash
      :caption: Restore the default web site files

      cp -p /etc/apache2/vhosts.d/0000-default.conf.old /etc/apache2/vhosts.d/0000-default.conf
      cp -p /etc/apache2/vhosts.d/0000-default-ssl.conf.old /etc/apache2/vhosts.d/0000-default-ssl.conf

   Use the ``1111-default`` names instead if those are the ``.old`` or ``.rpmsave`` copies the server has. Then check the config and restart apache:

   .. code-block:: bash
      :caption: Check the config and restart apache

      apachectl configtest && systemctl restart apache2
