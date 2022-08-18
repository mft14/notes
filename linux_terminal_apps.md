# Linux Terminal Apps
Here are lists of common terminal apps I often use. <br>
Ordered alphabetically<br>
Still in work!

## 3rd Party CLI
#### cmus
|Command|Action|
|---|---|
|jkhl|moving (vim)|
|x|Play / Restart |
|c|Hold|
|v|Hold|

#### id3v2
|Command|Action|
|---|---|
|-t -a|t=Title / a=Artist |
|-A|Album|

#### ffmpeg
|Command|Action|
|---|---|
|-i|choose file|
|-vn|show progress|
|-ar 44100|audio (sample) rate|
|-ac 2|audio channels|
|-ab 192|audio bitrate|
|-f|file type: `-f mp3 NEWNAME.mp3`|
|video to mp3|ffmpeg -i video.flv -f mp3 audio.mp3|
|video to GIF|ffmpeg -i video.mp4 -vf scale=300:-1 -t 10 -r 10 image.gif|
|-r|Frame Rate|
|-t|Time (Duration of file)|

#### fluidsynth
Soundfont file first, then .mid file to playback
```
fluidsynth /usr/share/sounds/sf2/FluidR3_GM.sf2 YOURMIDI.mid
```

#### mp3gain
|Command|Action|
|---|---|
|-r|automatic gain|
|-a|automatic gain album|
|-p|keep date|
|*|whole folder|
|\*/\*|+ sub folder|
|||

#### Ventoy
Check disk path names with "Disks" 
1. `cd` to Ventoy folder
2. `sudo sh Ventoy2Disk.sh -i /dev/sd`**???** <--- insert exact letter here
3. Let it run 


## Preinstalled CLI

####chmod 
|Command|Meaning|
|---|---|
|`u ; g ; o ; a`|user ; group; others; all|
|`rwx`|read;write;executable|
|`+ OR -`|add OR remove|
|`0 1 2 3 4 5 6 7 `|no ; x ; w ; w+x ; r ; r+x ; r+w ; r+w+x |
|`chmod u+x FILE`|make executable for user|
|`chmod 100 FILE`|make executable for user|

#### find
|Command|Action|
|---|---|
|`find . -name *.txt`|find all txt files|


#### git
|Command|Action|
|---|---|
|`git config --global user.name "NAME"`|Enter username|
|`git config --global user.email "mail@example.com"`|Enter mail|
|`git status | add . | commit -m "MESSAGE" | push | pull`|Standard Git commands to check, stage, commit, push & pull|
|`git clone https://TOKEN@github.com/USER/REPO.git`|Quickly clone private repositories|

## Good to know:
- `cd` = use only `cd` to go to home directory
- `cd -` = alternative to `cd ..` 
- `rm *.txt` = removes every textfile (use with CARE)
