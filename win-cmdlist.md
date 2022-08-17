# Windows CMD and Run Commandlist

Started creating this cheatsheet when I began my new apprentice ship as IT specialist.<br>
Useful run commands (Win + R) and cmd commands. <br>
Sub texts are German names as I need to know them as well.

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
- [Abbreviation List](#abbreviation-list)

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

## Folders/Locations Commands
|Command|Action|
|---|---|
|	`	..	`	|	Alle Benutzer Ordner	|
|	`	.	`	|	Current User Ordner	|
|	`	\	`	|	c:\\	|
|	`	Desktop	`,`	Documents	`,`	Downloads	`,`	Pictures`| Open common user folders directly (per run command)	|
|	`	shell:startup	`	|	Autostart	|
|	`	%appdata%	`	|	appdata Roaming	|
|	`	net use Z: \\server\pfad /persistent:Yes	`	|	Schnelle Möglichkeit für Netzlaufwerke	|

## System Repair Commands
|Command|Action|
|---|---|
|	`	sfc /scannow	`	|	System nach Schäden durchsuchen / Reparatur	|
|	`	DISM /Online /Cleanup-Image /RestoreHealth	`	|	Das checkt nochmal, einfach eingeben _:D	|
|	`	chkdsk C: /r	`	|	Disk Errors & Bad Sectors reparieren	|
|	`	netsh wlan show wlanreport	`	|	Bei Problemen mit WLAN	|
|	`	powercfg /energy ODER /batteryreport	`	|	Bei Problemen mit Netztteil/Strom/Batterie	|

## Useful CMD Commands
|Command|Action|
|---|---|
|	`	tasklist	`	|	Zeigt alle Tasks an. PID merken	|
|	`	taskkill (/f /t) /pid PIDNUMBER	`	|	Task ProcessID end (/f force /t child processes)	|
|	`	tasklist | find "vivaldi" 	`	|	Die Zahl daneben ist die PID	|
|	`	color (a)	`	|	Terminalfarbe	|
|	`	robocopy "C:\Users\" "D:\Backup" /mir	`	|	Spiegelt Ordner	|
|	`	date ` |	date 01.08.2022 ändert sofort Datum (Adminrechte)	|
|	`	time ` |	time 13:00:00 ändert sofort Zeit (Adminrechte)	|
|	`	notepad %systemroot%\system32\drivers\etc\hosts	`	|	Am Ende 127.0.0.1 URL anhängen, um Webseiten zu sperren	|
|	`	net user USERNAME PW /add	`	|	neuen Nutzer hinzufügen	|
|	`	net user Administrator /active:yes	`	|	Adminkonto aktivieren, falls gebraucht	|
|	`	net user USERNAME /random 	`	|	Random PW erstellen für existierenden Benutzer	|
|	`	copy con "name.txt"	`	|	Quickly create file. CTRL+S to save, then CTRL+C to stop	|
|	`	fc (/b) a.txt b.txt (file comparison, same folder)	`	|	Unterschiede feststellen von zwei Dateien	|
|	`	> C:\alle_user.txt 	`	|	In Datei schreiben z.B. net user	|
|	`	\| find "SUCHWORT"	`	|	Suchen zB. tasklist; systeminfo	|
|	`	cipher /e D:\encrypt	`	|	Verschlüsselt mit user Passwort	|
|	`	cipher /e /s:D:/folder	`	|	Wenn schon Dateien drin sind	|
|	`	cipher /w:C. oder D:	`	|	Schreibt Riesendatei	|

## Basic Movement
|Commands|Action|
|---|---|
|	`	cd, del, move, copy, ren	`	|	cd, löschen, bewegen, kopieren	|
|	`	md ; rd /S ORDNER	`	|	make/remove dir 	|
|	`	C: ; D:	`	|	Wechseln	|
|	`	"diskpart ` then `list volume"	`	|	list all drives	|



# Abbreviation List
|Command|Meaning|
|---|---|
| `cpl` | **C**ontrol **P**ane**l** |
| `mstsc` | Microsoft Terminal Services Client |
| `ncpa` | (network control panel) |
| `osk`| on screen keyboard|
| `wscui` | Win Security UI |

