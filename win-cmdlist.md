# Windows CMD and Run Commandlist

Started creating this cheatsheet when I began my new apprentice ship as IT specialist.<br>
Useful run commands (Win + R) and cmd commands. <br>
Sub texts are German names as I need to know them as well.

This list is still under construction. There might be some language errors

### Quick navigation
- [Important Commands](#important-commands)
- [Control Panel Commands](#control-panel-commands)
- [Systen Information Commands](#system-information-commands)
- [Management Apps Commands](#management-apps-commands)
- [Simple Windows Apps Commands](#simple-windows-apps-commands)
- [Folders/Location Commands](#folderslocations-commands)
- [System Repair Commands](#system-repair-commands)
- [Useful CMD Commands](#useful-cmd-commands)
- [Basic Movement](#basic-movement)
- [Win10 Control Panel Quick Commands](#windows-10-control-panel-quick-commands)
- [Abbreviation List](#abbreviation-list)

## Important Commands
|Command|Action|
|---|---|
| `control` | Control Panel (old) <sub>(Systemsteuerung)</sub> |
| `sysdm.cpl` | Computer Settings |
| `mmsys.cpl` | Sound (old) |
| `appwiz.cpl` |	Un/Install Apps (old) |
| `optionalfeatures`| Un/Install optional features |
| `mstsc` | Remote Desktop Session |
| `ncpa.cpl` | Network Connections <sub>Netzwerkverbindungen</sub> |

## Control Panel Commands
|Command|Action|
|---|---|
|	`	control desktop	`	|	Personalization Settings |
|	`	control folders	`	|	File Explorer Options	|
|	`	control keyboard	`	|	Keyboard Properties	|
|	`	control mouse 	`	|	Mouse Properties |
|	`	control printers	`	|	Devices and Printers |
|	`	firewall.cpl`	|	Firewall |
|	`	joy.cpl	`	|	Gamepad	|
|	`	wscui.cpl	`	|	Security and Maintenance <sub>Wartungscenter</sub>	|
|	`	powercfg.cpl	`	|	Power Options |
|	`	sndvol	`	| Volume Mixer (old)	|
|	`	taskmgr	`	|	Taskmanager	|
|	`	control update	`	|	Windows Update	|
|	`	control system	`	|	PC System Info	|

## System Information Commands
|Command|Action|
|---|---|
|	`	msconfig	`	|	System configuration	|
|	`	msinfo32	`	|	System information	|
|	`	winver	`	|	Windows Version	|
|	`	systeminfo (run in CMD)	`	|	Outputs computer hardware	|
|	`	systeminfo \| find "NAME"	`	|	Finds specific entry	|
|	`	dxdiag	`	|	Quickly display graphic card |
|	`	wmic path win32_VideoController get name	`	|	Quickly display graphic card |
|	`	wmic memorychip	`	|	Quickly display RAM informations |
|	`	arp -a	`	|	all IP adresses on router	|
|	`	ipconfig (/all)	`	|	network informations like ip adresses	|
|	`	ipconfig /flushdns	`	|	Deletes DNS Cache Resolver	|
|	`	ping & nslookup	`	|	Ping server and vice versa (with nslookup) |
|	`	tracert	`	|	Shows all routes before reaching target server	|
|	`assoc \| find \"mp3\" ` |	Shows file associations	|

## Management Apps Commands
|Command|Action|
|---|---|
|	`	devmgmt.msc	`	|	Device Manager <sub>Gerätemanager</sub>	|
|	`	dfrgui	`	|	Defragment Tool	|
|	`	diskmgmt.msc	`	|	Disk Management	|
|	`	eventvwr	`	|	Event Viewer	|
|	`	fsmgmt.msc	`	|	Shared Folders	|
|	`	lusrmgr.msc `	|	Local Users and Groups 	|
|	`	perfmon	`	|	Performance Monitor	|
|	`	regedit	`	|	Registry Editor	|
|	`	rstrui	`	|	System Restore	|
|	`	services.msc	`	|	Win Services	|
|	`	slui `	|	Windows Activation	|
|	`	taskschd.msc	`	|	Task Schedule	|
|	`	virtmgmt.msc	`	|	Hyper-V	|
|	`	wf.msc	`	|		Windows Defender Firewall with Advanced Security	|
|	`	control keymgr.dll	`	|	Windows Credentials <sub>Anmeldeinformationsverwaltung</sub>	|

## Simple Windows Apps Commands
|Command|Action|
|---|---|
|	`	calc	`	|	Calculator	|
|	`	charmap	`	|	Char Map	|
|	`	magnify	`	|	Glasses	|
|	`	notepad(++)	`	|	Notepad(++)	|
|	`	osk	`	|	On-Screen-Keyboard	|
|	`	write	`	|	Wordpad	|
|	`	wmplayer	`	|	Windows Media Player	|
|	`	quickassist	`	|	New Remote Assistance	|

## Folders/Locations Commands
|Command|Action|
|---|---|
|	`	..	`	|	All User folders	|
|	`	.	`	|	Current User Folder	|
|	`	\	`	|	c:\\	|
|	`	Desktop	`,`	Documents	`,`	Downloads	`,`	Pictures`| Open user folders directly	|
|	`	shell:recyclebinfolder	`	|	Recycle Bin |
|	`	shell:startup	`	|	Autostart	|
|	`	%appdata%	`	|	Appdata -- Roaming	|
|	`	net use Z: \\server\path /persistent:Yes	`	|	Bind network devices quickly |

## System Repair Commands
|Command|Action|
|---|---|
|	`	sfc /scannow	`	|	System scan for errors / repair	|
|	`	chkdsk C: /r	`	|	Disk Errors & Bad Sectors repair	|
|	`	netsh wlan show wlanreport	`	|	Checking WLAN problems	|
|	`	powercfg /energy ` OR `powercfg /batteryreport	`	|	Checking power supply errors OR battery	|

## Useful CMD Commands
|Command|Action|
|---|---|
|	`	tasklist	`	|	list every task	|
|	`	taskkill (/f /t) /pid PIDNUMBER	`	|	kill task per PID	|
|	`	tasklist | find "vivaldi" 	`	|	Die Zahl daneben ist die PID	|
|	`	taskkill /f /t) `	|	/f = force /t = kill child tasks	|
|	`	color (a)	`	|	Terminal color	|
|	`	robocopy "C:\Users\" "D:\Backup" /mir	`	|	Mirror folder ( /e = copy and keeping old)	|
|	`	date ` |	(admin) change date (syntax like your current format)	|
|	`	time ` |	(admin) change time (syntax like your current format) |
|	`	notepad %systemroot%\system32\drivers\etc\hosts	`	|	Put IP or websites to lock them	|
|	`	net user USERNAME PW /add	`	|	add new user with. PW = password	|
|	`	net user Administrator /active:yes	`	|	Activate administrator account	|
|	`	net user USERNAME /random 	`	|	Creates random password for user	|
|	`	copy con "name.txt"	`	|	Quickly create file. CTRL+S to save, then CTRL+C to stop	|
|	`	fc (/b) a.txt b.txt `	| File comparison |
|	`	> C:\alle_user.txt 	`	|	Put this at the end - Creates file, storing output	|
|	`	\| find "SUCHWORT"	`	|	Put this at the end - searches for names, for example in tasklist	|


## Basic Movement
|Commands|Action|
|---|---|
|	`	cd, del, move, copy, ren	`	|	change dir, delete, move, copy, rename	|
|	`	md ; rd /S ORDNER	`	|	make/remove dir 	|
|	`	C: ; D:	`	|	Change drive	|
|	`	diskpart `  then  `list volume	`	|	list all drives	|

## Windows 10 Control Panel Quick Commands
|Commands|Action|
|---|---|
|	`	ms-settings:	`	|	System Settings	|
|	`	ms-settings:display	`	|		|
|	`	ms-settings:yourinfo	`	|	
|	`	ms-settings:workplace	`	|	
|	`	ms-settings:dateandtime	`	|	
|	`	ms-settings:startupapps	`	|	
|	`	ms-settings:defaultapps	`	|	

For a full Win10 control panel list, [check out this page.](https://winaero.com/ms-settings-commands-in-windows-10/)


# Abbreviation List
|Command|Meaning|
|---|---|
| `appwiz` | App(lication) wizard |
| `assoc` | Associate |
| `.cpl` | **C**ontrol **P**ane**l** |
| ` fsmgmt` | Folder Share Management |
| `lusrmgr` | Local User Manager |
| `mgr` OR `mgmt` | Manager/Management |
| `mmsys` | Multimedia System |
| `ms` | Microsoft |
| `.msc` | Microsoft Management Console|
| `mstsc` | Microsoft Terminal Services Client |
| `ncpa` | Network Control Panel |
| `osk` | on screen keyboard|
| `powercfg` | Power Configuration |
| `regedit` | Registry Editor |
| `rstrui` | Restore User Interface |
| `slui` | Software Licensing User Interface |
| `sndvol` | Sound Volume |
| `sysdm` | System Device Manager |
| `taskschd` | Task Schedule |
| `tracert` | Trace Route |
| `wf.msc`| Windows (Defender) Firewall |
| `wmic` | ??? |
| `wscui` | Win Security User Interface |

