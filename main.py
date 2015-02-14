#!/usr/bin/python
#coded by Panggalu Ari and Vicky Dasta
#bug fixed by Vicky Dasta
import sys
try:
  from pythonwifi.iwlibs import Wireless
except ImportError:
  print 'python-wifi & scapy module not installed'
  sys.exit(0)

try:
  if sys.argv[1] == '-i' and sys.argv[2] != '':
    iface=sys.argv[2]
  else:
    pass
except Exception:
  print 'define your network card interface with -i <interface>'
  sys.exit()

def main():

    
  frequency_channel_map = {
  2412000000: "1",
  2417000000: "2",
  2422000000: "3",
  2427000000: "4",
  2432000000: "5",
  2437000000: "6",
  2442000000: "7",
  2447000000: "8",
  2452000000: "9",
  2457000000: "10",
  2462000000: "11",
  2467000000: "12",
  2472000000: "13",
  2484000000: "14",
  5180000000: "36",
  5200000000: "40",
  5220000000: "44",
  5240000000: "48",
  5260000000: "52",
  5280000000: "56",
  5300000000: "60",
  5320000000: "64",
  5500000000: "100",
  5520000000: "104",
  5540000000: "108",
  5560000000: "112",
  5580000000: "116",
  5600000000: "120",
  5620000000: "124",
  5640000000: "128",
  5660000000: "132",
  5680000000: "136",
  5700000000: "140",
  5735000000: "147",
  5755000000: "151",
  5775000000: "155",
  5795000000: "159",
  5815000000: "163",
  5835000000: "167",
  5785000000: "171",
  }

  wifi = Wireless(iface)
  for ap in wifi.scan():
    print "SSID: {}".format(ap.essid)
    print "AP: ".format(ap.bssid)
    print "Signal: ".format(ap.quality.getSignallevel())
    print "Frequency: ".format((ap.frequency.getFrequency()))
    print "Channel:".format(frequency_channel_map.get(ap.frequency.getFrequency()))
    print ""

if __name__ == '__main__':
  main()
