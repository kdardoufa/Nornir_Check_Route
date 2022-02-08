from nornir import InitNornir
from nornir.plugins.functions.text import print_result,print_title
from nornir.plugins.tasks.networking import netmiko_send_command,netmiko_send_config
from datetime import datetime
import time

def main():

    print("Beginning: ", datetime.now())

    device_list = []
    #ip_list = []
    route = "route_to_be_defined"  #route to be defined by user

    timestr = time.strftime("%Y%m%d_%H%M")
    ADSL_file = "adsl_"+timestr+".txt"

    nr = InitNornir(config_file="config.yaml")

    # info contains the output of the command
    info = nr.run(task=netmiko_send_command, command_string="show ip route | in "+route)

    # Get hosts to use as argument in info['hosts'].result
    for dev in nr.inventory.hosts.keys():
        output =  info[dev].result
        #ip_addr = nr.inventory.hosts[dev].hostname
        if route not in output:
            device_list.append(dev)

    with open(ADSL_file,'w') as filehandle:
        for host in device_list:
            filehandle.write('%s\t' % host)
            filehandle.write('\t%s\n' % nr.inventory.hosts[host].hostname)

    nr.close_connections()

    print("End: ", datetime.now())
    return()

if __name__ == "__main__":
    main()