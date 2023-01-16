# radio cli...
Radio Player

Files radio.py / radio1.py / radio.sh use file radio.txt as "database"
* Each one is an individual player. There is no dependency between .py and .sh files
** radio-player.py using same text file but I intend to use sqlite3

For radio.py work correctlly is necessary to have installed python3 and python3-dialog packages.

Installing dependencies
For RHEL/Centos/Fedora/...
- sudo dnf install python3 python3-dialog

For Debian/Ubuntu/...
- sudo apt install python3 python3-dialog

* Radios station of example are from Brazil as shell script for search
