import os
import compare
# Get current connection info and write to c_network.txt
def add_to_known():
    os.system('cmd /c "netsh wlan show interfaces > c_network.txt"')
    current_connection_file = open("c_network.txt","r")

    # Break up file so only SSID is saved
    split_string = current_connection_file.read().split('SSID')
    next_split = str(split_string[1]).split(': ')
    last_split = str(next_split[1]).split('\n')
    SSID = last_split[0]
    #print(SSID)

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
    #print(default_gateway)
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
    #print(mac_of_gateway)
    # Close and delete info file
    arp_file.close()
    os.remove("arp_info.txt")

    # Write to known networks file
    cur_info = "{} - {} - {}".format(SSID, default_gateway,mac_of_gateway)
    if(os.path.isfile('known_networks.txt')):
        known_networks_file = open("known_networks.txt", "r")
        known_info = ''
        flag = False
        for line in known_networks_file:
            if line.startswith("{}".format(SSID)):
                flag = True
                break
        if flag == False:
            known_networks = open("known_networks.txt","a+")
            known_networks.write("\n{} - {} - {}".format(SSID,default_gateway,mac_of_gateway))
            known_networks.close()
    else:
        known_networks = open("known_networks.txt", "a+")
        known_networks.write("\n{}".format(cur_info))
        known_networks.close()


def update_current_connection(SSID,current_info):
    known_networks_file = open("known_networks.txt", "r")
    lines = known_networks_file.readlines()
    known_networks_file.close()
    known_networks_file = open("known_networks.txt", "w")
    for line in lines:
        if (line.startswith(SSID) == False):
            known_networks_file.write(line)
    known_networks_file.write("\n{}".format(current_info))
