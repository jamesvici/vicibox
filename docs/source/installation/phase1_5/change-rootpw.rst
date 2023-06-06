Change root password
====================
   Please try to pick a root password you will remember. Recovering a lost or forgotten root password is not overly trivial. Lastly, if there is no root access to the server then ViciDial and ViciBox cannot be maintained. You have been warned!

   The root user is everything in Linux. It's highly recommended to change the root users password to something secure. While everyone will have their own preferences for passwords, here are some rough guidelines to help create a more secure password:
   * At least 14 characters in length
   * Contains at least one upper case (ABC)
   * Contains at least one lower case (abc)
   * Contains at least one number (123)
   * Contains at least one special character (@%!)
   * Does NOT contain 'vicidial', 'vici', 'password', or 'pass'
    
   .. note:: While a truly random password is the most secure, a password you can remember is more useful. I recommend basing the password around a 'phrase' to help. As an example, albeit a bad one, of this is the password 'ViciPass4U!'.

passwd
------
   #. If not already, login as the 'root' user to get to the command prompt.
   #. Type ``passwd`` to change the root password.
   #. At the 'New password:' prompt type in your new root password.
   #. At the 'Retype new password:' prompt type in yoru new root password again to verify it.


Screenshots
^^^^^^^^^^^
   Run passwd
      .. image:: change-rootpw-1.png
         :alt: Run passwd to change root password
         :width: 665