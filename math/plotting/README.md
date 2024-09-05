More Info
Installing Matplotlib 3.0
pip install --user matplotlib==3.0
pip install --user Pillow
sudo apt-get install python3-tk
To check that it has been successfully downloaded, use pip list.

Configure X11 Forwarding
Update your Vagrantfile to include the following:

Vagrant.configure(2) do |config|
  ...
  config.ssh.forward_x11 = true
end
If you are running vagrant on a Mac, you will have to install XQuartz and restart your computer.

If you are running vagrant on a Windows computer, you may have to follow these instructions.

Once complete, you should simply be able to vagrant ssh to log into your VM and then any GUI application should forward to your local machine.

Hint for emacs users: you will have to use emacs -nw to prevent it from launching its GUI.
