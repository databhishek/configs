#!/bin/bash
# Usage: $./ion-login.sh <username> <password>
# Author: Abhishek Singh

curl -sd 'mode=191' \
     -sd 'isAccessDenied=false' \
     -sd 'url=null' \
     -sd 'message=' \
     -sd 'regusingpinid=' \
     -sd 'checkClose=1' \
     -sd 'sessionTimeout=-1' \
     -sd 'guestmsgreq=false' \
     -sd 'logintype=2' \
     -sd 'orgSessionTimeout=-1' \
     -sd 'chrome=-1' \
     -sd 'alerttime=null' \
     -sd 'timeout=-1' \
     -sd 'popupalert=0' \
     -sd 'dtold=0' \
     -sd 'mac=04:c5:a4:f6:22:c5' \
     -sd 'servername=mahe3.dvois.com' \
     -sd 'temptype=' \
     -sd 'username='$1'' \
     -sd 'password='$2'' \
     -sd 'saveinfo=saveinfo' \
     -sd 'loginotp=false' \
     -sd 'logincaptcha=false' \
     -sd 'registeruserotp=false' \
     -sd 'registercaptcha=false' \
     --output /dev/null \
     https://mahe3.dvois.com/24online/servlet/E24onlineHTTPClient
     
     notify-send "ION Connected" -t 2000
