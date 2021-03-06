# traceme

**traceme** is a python script works similar to traditional traceroute utility, additionaly it will it give the  **Visual traceroute path** in **Google Earth** by using the latitude and longitude value of the ip address from **ip-api.com**. Then create a **KML(Keyhole Markup Language)** file for expressing geographic annotation and visualization within Internet-based, two-dimensional maps and three-dimensional Earth.

3 Process involves in the scripts are:
- **traceroute**: Get the intermediate IP Address
- **getlocation**: Get the Geolocation of the IP Address
- **createKML file** : Get a Keyhole Markup Language suitable to view in Google maps app or web or mobile 


## Requirements
- Python 2.7
- Python pip
- scapy
- requests
- ast
- simplekml


### Installation

1. Clone (or download the ZIP) to your computer.
2. Install the requirements package using `sudo -H pip install requirements.txt`
3. Run as **Root**, Scapy requires Root Privilege to Inject Packet into Network
4. Run the program using hostname or IP Address as Input 

```sh
# git clone https://github.com/prabhudeva17/traceme.git
# cd traceme
# sudo ./traceme.py -i wwww.google.com
```
### How To Use
1. Using the command line run:
    `python traceme.py -i <ip-address>`
               or
    `./traceme.py -i <ip-address>`
2. Wait for the program to finish to traceroute.
3. Wait for the program to create a KML tracemap file 
4. Open the KML file with  Google Earth or import to Google Maps.


### DEMO TIME!!

[![0vlx97](https://user-images.githubusercontent.com/30696072/50482781-73cac800-0a0e-11e9-9527-ac331c713029.gif)](https://youtu.be/6WmbnYw03BE)

### traceme
![screenshot-1](https://user-images.githubusercontent.com/30696072/50468642-f338a700-09ce-11e9-9558-a1f9d43c8a5e.png)

### tracemap
![screenshot-2](https://user-images.githubusercontent.com/30696072/50468648-03508680-09cf-11e9-91df-900580f55de6.png)


### Development

Want to contribute? Great!
Open your favorite Terminal and fix bug if their any.
Still in development more plugin will added in future

License
----

MIT


**Free Software!**
