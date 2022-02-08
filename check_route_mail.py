#!/home/kadar/WSL-Project-env/bin/python3
from nornir import InitNornir
from nornir.plugins.functions.text import print_result,print_title
from nornir.plugins.tasks.networking import netmiko_send_command,netmiko_send_config
from datetime import datetime
import time
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def my_sendmail(mail_body):
    exchange_sender = "email of sender to be specified by user"
    exchange_passwd = "sender password for authentication to be specified by user"
    smtp_server = "smtp server to be specified by user"
    #works with multiple recipients example recipients = "test1@expamle.com,test2@example.com"
    recipients = "comma seperated emails"
    smtp_port = 25

    msg = MIMEMultipart()
    msg['From'] = exchange_sender
    msg['To'] = recipients
    msg['Subject'] = "Remote branch utilizing backup link"
    body = mail_body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(exchange_sender, exchange_passwd)
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'].split(","), text)
    server.quit()
# End of function

def main():
    hostname = []
    device_list = []
    ip_addr = []

    #print("Beginning: ", datetime.now())
    nr = InitNornir(config_file="config.yaml")
    route = input("Please type route to check and press enter: ")
    # info contains the output of the command
    info = nr.run(task=netmiko_send_command, command_string="show ip route | in "+route)

    # Get hosts to use as argument in info['hosts'].result
    for dev in nr.inventory.hosts.keys():
        output =  info[dev].result
        #ip_addr = nr.inventory.hosts[dev].hostname
        if route not in output:
            device_list.append(dev)
    # Create one list with hostnames and one list with ip addresses
    for host in device_list:
        hostname.append(host)
        ip_addr.append(nr.inventory.hosts[host].hostname)
    # combine two lists into a dictionary
    output_dev = dict(zip(hostname,ip_addr))

    nr.close_connections()
    #if output_dev not empty
    if output_dev:
        tmp = json.dumps(output_dev)
        mail_body = tmp.replace("\"","").replace(",","\n").strip("{").strip("}")
        my_sendmail(mail_body)

    return()



