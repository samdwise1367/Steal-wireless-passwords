#Get all wireless password stores on a pc and save to a file
import subprocess, re

command = "netsh wlan show profile"
networks = str(subprocess.check_output(command, shell=True))
print(networks)
network_list = re.findall("(?:\s:\s[A-Za-z0-9-@_']*)\s*(?:\d|[A-Za-z]*)",networks) #use regex to find name of netwoorks
print(network_list)



final_output = ""

for network in network_list:
    temp = network.split(': ')
    print(temp[1])
    command2 = "netsh wlan show profile "+ str(temp[1]).strip()+" key=clear"
    one_network_result = str(subprocess.check_output(command2, shell=True))
    result_re = re.findall("(?:Key\s*Content\s*:\s[A-Za-z0-9_!#$%&*]*)",one_network_result)
    final_output += network+" = "+str(result_re)+"\n"


#save to file
file = open("wifipasswords.txt",'w')
file.write(final_output)
file.close()