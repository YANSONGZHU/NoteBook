##### Disable Grub Message
sudo nano /etc/default/grub <br />
Edit this line <br />
GRUB_CMDLINE_LINUX_DEFAULT="quiet loglevel=0 splash" <br />
sudo update-grub <br />

##### disable initramfs message
echo FRAMEBUFFER=y | sudo tee /etc/initramfs-tools/conf.d/splash <br />
  sudo update-initramfs -u
