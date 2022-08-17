# Windows CMD and Run Commandlist

Started creating this cheatsheet when I began my new apprentice ship as IT specialist: system integrator.
Useful run commands (CTRL + R) and cmd commands. Sub texts are German names as I need to know them as well.

## Important Commands
|Command|Action|
|---|---|
| `control` | Control Panel (old) <sub>(Systemsteuerung)</sub> |
| `sysdm.cpl` | Computer Settings |
| `mmsys.cpl` | Soundeinstellungen (alt) (Multimedia System) |
| `appwiz.cpl` |	Un/Install Apps (old) |
| `optionalfeatures`| Un/Install optional features |
| `mstsc` | Remote Desktop Session |
| `ncpa.cpl` | 	Network Connections (Netzwerkverbindungen) |

## Control Panel Commands
|Command|Action|
|---|---|
|	`	control desktop	`	|	Desktopeinstellung (RKL Desktop)	|
|	`	control folders	`	|	Ordneroptionen	|
|	`	control keyboard	`	|	Tastatureinstellungen	|
|	`	control mouse 	`	|	Mauseinstellungen	|
|	`	control printers	`	|	Geräte und Drucker	|
|	`	firewall.cpl / wf.msc	`	|	Firewall / Win Defender Firewall	|
|	`	inetcpl.cpl	`	|	Interneteigenschaften von Inet Explorer xD	|
|	`	joy.cpl	`	|	Gamepad	|
|	`	wscui.cpl [win Security UI]	`	|	Wartungscenter	|
|	`	powercfg.cpl	`	|	Energieoptionen (power config)	|
|	`	sndvol	`	|	Sound Lautstärke Mixer (alt) (sound volume)	|
|	`	taskmgr	`	|	Taskmanager	|
|	`	control update	`	|	Windows Update	|
|	`	control system	`	|	System Info (PC Umbenennen)	|

## System Information Commands
|Command|Action|
|---|---|
|	`	msconfig	`	|	Systemkonfiguration	|
|	`	msinfo32	`	|	Systeminformationen	|
|	`	winver	`	|	Windows Version	|
|	`	systeminfo (in CMD)	`	|	im CMD aufrufen für Infos	|
|	`	systeminfo \| find "Speicher"	`	|		|
|	`	find Installationsdatum	`	|		|
|	`	find Prozessor, Domäne ->	`	|	Anmeldeserver, Hyper-V	|
|	`	Betriebssystem etc.	`	|		|
|	`	dxdiag	`	|	Grafikkarte schnell auslesen	|
|	`	wmic path win32_VideoController get name	`	|	Grafikkarte schnell auslesen	|
|	`	wmic memorychip	`	|	Alles über RAM (auch Banks etc)	|
|	`	arp -a	`	|	Alle IP Adressen am Router	|
|	`	ipconfig (/all)	`	|	Informationen zu Netzwerk	|
|	`	ipconfig /flushdns	`	|	Löscht DNS Cache Resolver	|
|	`	ping & nslookup	`	|	Webseite pingen und andersrum	|
|	`	tracert	`	|	Zeigt Umwege bis Zielserver	|
|	`assoc (\| find \"mp3\")` |	Zeigt, was mit was assoziiert ist	|

## Management Apps Commands
|Command|Action|
|---|---|
|	`	devmgmt.msc	`	|	Gerätemanager	|
|	`	dfrgui	`	|	Defragmentierung	|
|	`	diskmgmt.msc	`	|	Datenträgerverwaltung	|
|	`	eventvwr	`	|	Ereignisanzeige	|
|	`	fsmgmt.msc	`	|	Freigegebende Ordner	|
|	`	lusrmgr.msc [local user manager]	`	|	Benutzer und Gruppen Manager 	|
|	`	perfmon	`	|	Leistungsüberwachung (alt)	|
|	`	regedit	`	|	Registry Editor	|
|	`	rstrui [restore UI]	`	|	Systemwiederherstellung	|
|	`	services.msc	`	|	Win Dienste	|
|	`	slui [Software Licensing User Interface]	`	|	Win Key	|
|	`	taskschd.msc	`	|	Aufgabenplanung	|
|	`	virtmgmt.msc	`	|	Hyper-V	|
|	`	wf.msc	`	|	Windows Defender Firewall m. erw. Sicherheit	|
|	`	control keymgr.dll	`	|	Windows Credentials (Anmeldeinformationsverwaltung)	|

## Simple Windows Apps Commands
|Command|Action|
|---|---|
|	`	calc	`	|	Taschenrechner	|
|	`	charmap	`	|	Zeichentabelle	|
|	`	magnify	`	|	Bildschirmlupe	|
|	`	notepad(++)	`	|	(Notepad)Editor	|
|	`	osk on screen keyboard	`	|	Bildschirmtastatur	|
|	`	write	`	|	Wordpad	|
|	`	wmplayer	`	|	Windows Media Player	|
|	`	shell:RecycleBinFolder	`	|	Papierkorb	|
|	`	quickassist	`	|	Remotehilfe	|














# Abbreviations of certain commands

|Command|Meaning|
|---|---|
| `cpl` | **C**ontrol **P**ane**l** |
| `mstsc` | Microsoft Terminal Services Client |
| `ncpa` | (network control panel) |
| `wscui` | Win Security UI |
| `osk`| on screen keyboard|

