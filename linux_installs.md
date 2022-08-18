# Linux App Installs
This is my personal list of apps I usually install on a new fresh system. If you want to create your own quick installers, make sure to use:

- the -y parameter lets you install everything without confirm "YES"
- use ; to combine several commands. Ideal if you first install something, then uninstall as this wouldn't work at once
- a multi-install like this also works in flatpak and snap

### Navigation
- [Apt Installs](#apt-installs-personal-list)
- [Flatpak Installs](#flatpak-installs)
- [Snap Installs](#snap-installs)
#### More Installs
- [Quick Folder Creation](#quick-folder-needed-for-certain-apps)
- [Activate/Install Snap on Linux Mint](#activate-and-install-snap-on-linux-mint)
- [KX Repositories Installs](#kx-repositories-installs)
- [LAMPP Install/Setup](#install-lampp-and-setup)
- [Grub Customizer](#grub-customizer-install)


#### Install generator planned!
In the future, it is planned to make a simple apt-install generator in HTML/JS so you can easily customize your own, throw everything in and only tick everything you need.
- - - - 

## Apt Installs (Personal list)
```
sudo apt install qjackctl mc 
bc git vim feh id3v2 wmctrl ranger samba 
hollywood ncdu nnn mpv w3m gocryptfs cmus 
neofetch xz-utils curl cmatrix pavucontrol
terminator winff audacious alacarte python3 python3-pip htop 
smbclient flatpak unrar ffmpeg virtualbox usb-creator-gtk 
arc-theme doublecmd-gtk mixxx -y; 

sudo pip3 install --upgrade youtube_dl; 
sudo apt remove celluloid rhythmbox -y;
```
## Flatpak Installs
```
flatpak install syncthing libresprite obsproject godot gimp skype spotify shotcut visualstudio.code steam
```
## Snap Installs
```
sudo snap install puddletag-snap mp3gain discord love2d kdenlive
```

- - - -

# More Installs
#### Quick Folder, needed for certain apps
```
mkdir Apps Jeux Progg VMs .themes .sounds .icons .vst3 .vst;
```

#### Activate and install Snap on Linux Mint:
```
sudo rm /etc/apt/preferences.d/nosnap.pref; sudo apt install snapd -y;
```

#### KX Repositories Installs
[KX Repositories](https://kx.studio/Repositories) is a collection of free and opensource audio plugins and applications. Since I am a music producer and make music in linux fulltime since 2021, this list is the perfect resource for professional linux audio production.

If you want to create your own list, then follow the link above to the KX repo and follow their simple terminal instruction. After that, **make sure to do `sudo apt update`** again to refresh the new package list and then head over to their [Applications](https://kx.studio/Repositories:Applications) 
and/or [Plugins](https://kx.studio/Repositories:Plugins) page. From there you can check and try out all these plugins - just copy the package name and create your own multi-install like mine. My recommendations are Carla, Calf-Plugins and Vitalium! 
> A summary of the best KX apps is planned for the future!

```
sudo apt install fluidsynth cadence carla cardinal-vst3 gxplugins calf-plugins surge protrekkr lsp-plugins -y ; 
```

#### Install LAMPP and setup
```
sudo apt-get install apache2 libapache2-mod-php php php-mysql mysql-server -y
```
Check "localhost" in your browser, if it works. Then create link to your project folder using "ln"
```
sudo ln -s ~/Documents/YOURPROJECTFOLDER/ /var/www/html/
```
Then you can just open up localhost/YOURPROJECTFOLDER and work with .php or other server-based things.

#### Grub Customizer Install
```
sudo add-apt-repository ppa:danielrichter2007/grub-customizer
sudo apt-get update
sudo apt-get install grub-customizer
```

- - - -
# App Notes

- Minecraft works fine with Flatpak/Snap but the file structure of the official version seems better

#### Problems with flatpaks
- `discord` works but problems with file upload --> snap version or official download 
- `shotcut` crashes, unsuable (Linux Mint 20.x) --> apt version 
- `visualstudio.code` works but [.deb from website](https://code.visualstudio.com/Download) seems a little less buggy

#### Problems with snaps

#### Problems with apt
- `mp3gain` is not available anymore in apt. Use `sudo snap install mp3gain`

