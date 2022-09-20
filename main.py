import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="You can enter the interface which you use")
parse_object.add_option("-m","--mac",dest="mac_address",help="YOu can enter the mac adress which you use")
print("Welcome to EkMacChanger!")


(cevap,arguments) = parse_object.parse_args()
user_interface = cevap.interface
user_mac = cevap.mac_address
print(user_interface)
print(user_mac)
print("You changed succesfully!")
subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
subprocess.call(["ifconfig",user_interface,"up"])
