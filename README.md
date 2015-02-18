# Ninja-Wardriver
A tool for the Wardriver hobbyist. Simple and Idiot. Still on process of Development .

First of all we write a tool to scan our environment forWifi networks. Thanks to the
pyhtonwifi module this is done with a few lines of Python code.

The function scan(), like the name implies, scans for access points on the network interface defined in the constructor Wireless() and returns a list of access point (Iwscanresult) objects. For every access point we print the SSID (the network name), BSSID (it’s hardware address), the signal strength, frequency and the channel. The channel is deduced from the frequency. A Wifi card that is radioing on the 2.412GHz frequency, sends its data on channel 1, one that is using
2.442GHz on channel 7.Scanning is an active operation. The tool transmits probe request packets with a set broadcast SSID. That is why such scanners like Netstumbler, the most used Scanner on Windows, are so simple to detect.

if you are using other network interface just change this code :  wifi = Wireless("wlan0")

# Dev Status
Still on Process
