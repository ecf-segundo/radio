# radio cli...
Radio Player

Files radio.py / radio1.py / radio.sh use file radio.txt as "database"
* Each one is an individual player. There is no dependency between .py and .sh files
** radio-player.py using same text file but I intend to use sqlite3
File radio-player.py use sqlite3 file radio.db

For radio.py work correctlly is necessary lib subprocess and dialog
For radio-player is necessary libs: sqlite3, dialog, bs4(Beautiful Soup 4), requests, subprocess

All of them needs python3 and mplayer

* Radios station of example are from Brazil as shell script for search
