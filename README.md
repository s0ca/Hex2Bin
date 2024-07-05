# Hex2Bin
Simple Hex2Bin script for converting data extracted from UART with SPI READ.

Example : 
You got partitions listed during the boot while looking through ``uBoot``
```
[...]
0x000001fd0000-0x000001ff0000 : "Config_Bak"
[...]
```
While looking for the built-in options you can see the ``spi read <addr> <len>`` command
Let's use it to get the ``Config_Bak``content 

First, we need to get the length which is easy since we got the start and end of the memory segment:
``0x000001fd0000 - 0x000001ff0000 = 131072`` --> Hex converting --> ``131072 = 0x20000``

Now let's just log everything from the serial port 

``screen /dev/ttyUSB0 115200 -L -Logfile out.txt`` 

Then read the partition :
``spi read 0x000001fd0000 0x20000``

the output will be a lof of gibberish (Hex raw) in our ``out.txt``file

Use the script on the out.txt file 
``python Hex2Bin.py out.txt out.bin``

Enoy your binary :)

``strings out.bin | grep -i "user\|pass"``
or ``binwalk -e out.bin``
or whatever you're using :) 
