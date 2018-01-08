# b-CD
A barcode-scanner based audio player.

<img src="b-cd_logo.png" alt="Logo" style="width: 50px;"/>

CDs are soon getting obsolete with the increasing use of streaming services. Anyway, if you still like to browse through your CD collection in real life and let others explore it in an easy way, just grab a barcode scanner and have fun!

b-CD is an application that runs in your terminal with a very basic curses GUI. At the current state it is used to play random tracks from a CD. You can off course map the music to any item in your room - After all, there are just any kind of barcode. Optionally, you can of course run the code on a RaspberryPi, that is mounted onto your CD shelf and connect it via bluetooth to a nearby music box.

## Setup
In order to use the program, you have to put the path to your music root directory into the accessories.py at the `music_dir` variable. You should rip your CDs and put the them structured into different subfolders at this location. OGG works best, since the pygame library sometimes cannot handle MP3 files well.

You\`ll need to have python installed and you can use `pip install` for the dependencies mentioned below.

In order to do the mapping from barcode to album, you have to create a file named `barcode` in each folder that you want to include in the library. At startup, all folders beginning with your root folder will be crawled and the barcodes will be put into a file at your current terminal location, which is automatically used by the program as a mapping file.

Now you are good to go!

## Usage
To start the program, simply do <br>
`python ./run.py`

After finishing to load the library, it waits for input. Here, the scanner comes in handy. Just scan the codes that you have put into your library off the Cds/items and you should hear the music playing.

You could also type the codes, but this is not practical at all. Other commands are:
* `r` - random album
* `p` - Pause/Play
* `+` - increase volume
* `-` - decrease volume
* `q` - quit

By the way, when listening to an album, you can see the barcode and can hence copy it to the input box in order to play one more song from the album. This is useful if you do not have a barcode scanner and use `r` for a random album, which you would like to explore further.
## TODO
- Playlist
- Hotkey Thread
- Resize Handling
- Split Song and Band

### Dependencies
- pygame
- pyttsx
