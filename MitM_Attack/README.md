# Man in the Middle Attack Module

This README will go through the process of performing this attack.

## Raspberry Pi Setup

This part is important. These items must be completed before starting this module.  

1. The SD card must be imaged with the Kali Linux OS using the Raspberry Pi imager:
    1. Using a micro-SD USB adapter, insert the card into a computer with the Raspberry Pi Imager.
    2. Load up the Imager.  
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager1.png?raw=true)
    3. Under "Other specific-purpose OS" find "Kali Linux" and choose the  
    "Raspberry Pi 2,3,4 & 400 (32-Bit)" option.  
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager2.png?raw=true)
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager3.png?raw=true)
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager4.png?raw=true)
    4. Next, click "Choose Storage" and select the drive containing the SD you wish to image.  
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager5.png?raw=true)
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager7.png?raw=true)
    5. Finally, click "Write". When prompted, select "Yes".
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager8.png?raw=true)
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager9.png?raw=true)
    6. The image will start writing to the SD card and will notify when completed.  
    This may take several minutes.  
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/RPi_imager10.png?raw=true)
    7. Once complete, you can remove the adapter from the adapter from your computer and remove  
    the SD from the adapter to insert into the Pi.
2. Once the SD card is in, power the device on.
3. The username and password is `kali`
![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/kali_login_screen.jpg?raw=true)  
4. Once in, you will also want to connect to the internet.
![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/kali_wifi.png?raw=true)  
![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/kali_wifi_connected.png?raw=true)  
5. then open a terminal (`Ctrl + [Alt] + t`) and run `sudo apt update && sudo apt upgrade -y`.  
This process could take several minutes.
![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/kali_update.png?raw=true)
6. Once the updates are done, you will want to install the following items:
    1. arpspoof: `sudo apt install dsniff`
    2. There may be more items added... (in general, as long as the updates are done, command-line  
    tools can be installed on the fly by using `sudo apt install [PACKAGE-NAME]`)
7. After all the above items are complete, it is time to start the module!

## Attacker Instructions

More is involved with the attacker in this module so we will start here:

1. Power on the Raspberry Pi with Kali Linux. `kali` should be both the username and password.
2. Open three terminals `Ctrl + [Alt] + t`:
    1. one will be used to communicate with the victim of the attack.
    2. the other will be used to communicate with the device that the victim intended to communicate with (via the router).
    3. the third will be to enter other commands
3. To make things easy, go into the root shell by typing `sudo -i` on each terminal. It will likely prompt you to enter a password  
which will just be `kali` which was used to log in. This elevates your privileges.
4. Find your victim and the gateway's IP addresses:
    1. A simple way find the IP addresses is to type `ifconfig` on the target machine.  
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/ifconfig_targ_ip.png?raw=true)
    ![alt text](https://github.com/nagallegos/WTAMU_WAGNER_MODULES/blob/main/Images/ifconfig_targ_mac.png?raw=true)
    2. Another way is to utilize `arp-scan -l` on the attacking machine and if the attack
    is being performed on a small, isolated network, the machine should be easily identified.
    The gateway typically ends in a 1 (Ex. `192.168.1.1`) and the target device will end
    in something larger (Ex. `192.168.1.105`).
    3. IMPORTANT: Take note of:  
        1. The Gateway's current IP & MAC address.
        2. The target's IP & MAC address.
        3. Your (the attacker's) current IP & MAC address.
5. Turn on packet forwarding:
    1. Type the command `sysctl net.ipv4.ip_forward`. What value do you see?
    2. If it is 0, we need to issue the command `sysctl net.ipv4.ip_forward=1`  
    to turn ipv4 forwarding on. This means that your device will now forward packets  
    instead of dropping them which would make the target unable to communicate over the network.
6. On the terminal being used to communicate with your target (the victim), type in the command:  
`arpspoof -i wlan0 -t [VICTIMS_IP] [GATEWAY_IP]`
7. On the terminal being used to communicate with the gateway (the router), type in the command:  
`arpspoof -i wlan0 -t [GATEWAY_IP] [VICTIMS_IP]`
8. You are now making the target device think that you are the gateway and you are making the  
gateway think that you are the target device. This also means that we can use Wireshark to see
all of the target devices traffic.
