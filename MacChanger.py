import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface",dest = "interface",help = "Interface to change MAC")
    parser.add_option("-m", "--mac",dest = "new_mac",help = "New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("No interface")
    if not options.new_mac:
        parser.error("No new mac")
    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if mac_address:
        return mac_address.group(0)
    else:
        print("No MAC address found")
def validation(options,mac_address):
    if mac_address == options.new_mac:
        print("Mac address successfully changed to " + current_mac)
    else:
        print("MAC address not changed")
options = get_arg()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
validation(options,current_mac)


