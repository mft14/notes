## Linux Quickstart Install
This is my personal list of apps I usually install on a new fresh system. If you want to create your own apt line, make use of these:

- the -y parameter lets you install everything without confirm "YES"
- use ; to combine several commands. Ideal if you first install something, then uninstall as this wouldn't work at once
- a multi-install like this also works in flatpak and snap

## Apt Installs (My personal list)
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



## App Notes

- Minecraft works fine with Flatpak/Snap but the file structure of the official version seems better

#### Problems with flatpaks
- `shotcut` flatpak crashes, unsuable (Linux Mint 20.x) --> apt version 
- `visualstudio.code` works but [.deb from website](https://code.visualstudio.com/Download) is better 
- 


#### Problems with snaps


#### Problems with apt

