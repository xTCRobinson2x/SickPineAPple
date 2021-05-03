import os
import alert_sys
def compare_to_known():
    # Get current connection info and write to c_network.txt
    os.system('cmd /c "netsh wlan show interfaces > c_network.txt"')
    current_connection_file = open("c_network.txt","r")

    # Break up file so only SSID is saved
    split_string = current_connection_file.read().split('SSID')
    next_split = str(split_string[1]).split(': ')
    last_split = str(next_split[1]).split('\n')
    SSID = last_split[0]

    #Close instance of current connection file and delete it
    current_connection_file.close()
    os.remove("c_network.txt")

    # Get Wi-Fi default gateway info
    os.system('cmd /c "ipconfig > ip_info.txt"')
    ip_info_file = open("ip_info.txt","r")

    # Break up file so Wi-Fi gateway is stored
    split_string = ip_info_file.read().split('Wi-Fi:')
    next_split = split_string[1].split('Default Gateway . . . . . . . . . : ')
    last_split = next_split[1].split('\n')
    default_gateway = last_split[0]

    # Close instance of gateway info file and delete it
    ip_info_file.close()
    os.remove("ip_info.txt")

    # Get MAC address of gateway using ARP table
    os.system('cmd /c "arp -a > arp_info.txt"')
    arp_file = open("arp_info.txt","r")
    # Get only MAC address
    split_string = arp_file.read().split('{}'.format(default_gateway))
    next_split = split_string[1].split()
    mac_of_gateway = next_split[0]
    # Close and delete info file
    arp_file.close()
    os.remove("arp_info.txt")
    # Create string of current information, see if SSID is in known list, compare
    current_connection_info = "{} - {} - {}".format(SSID,default_gateway,mac_of_gateway)
    known_networks_file = open("known_networks.txt","r")
    known_info = ''
    for line in known_networks_file:
        if line.startswith("{}".format(SSID)):
            known_info = line
            known_info = known_info.split("\n")
            known_info = known_info[0]
            if(known_info == current_connection_info):
                return True
            else:
                return False
    return "Unknown Network"

def show_known_networks():
    os.system('known_networks.txt')
