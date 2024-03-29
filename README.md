## Description 

We were looking for a quick way to identify which routers in our infrastructure where utilizing their ADSL link. 
Since we are using GETVPN and the actual links (primary/secondary) are on the providers equipment, and taking into account that
when the backup link is utilized a specific route dissappears from the routing table, we decided to look for that exact route. 
The initial attempt was done creating a scheduled job in Cisco Prime Infrastructure, but the process took a long time and involved
manually going over the output to figure out which devices where using the backup link. 
Using Nornir greatly improved performance! The devices using the backup link are written to a file (name/IP address). This is done via the script "check_route.py".
The file is great... but wouldn't it be better if an email was sent, with the devices in the e-mail body? This is done via the script "check_route_mail.py"


# Configuration
The following should be configured by the user, according to their environment.
- inventory directory: defaults.yaml, getvpn_hosts.yaml, groups.yaml
- variable: route --> route_to_be_specified_by_user

For e-mails the user needs to specify the following variables:
- exchange_sender --> "email of sender to be specified by user"
- exchange_passwd --> "sender password for authentication to be specified by user"
- smtp_server --> "smtp server to be specified by user"
- recipients --> "comma seperated emails" (works with multiple recipients example recipients = "test1@expamle.com,test2@example.com")

# Technologies & Frameworks Used
* Nornir.
* WSL - Ubuntu 18.04.3 LTS 
* The script is written in Python 3. Tested also with Python3.8.10

Update (Feb 8th 2022): 
* Tests have been made with Ubuntu 20.04.3 LTS, python3.8.10 and nornir 2.5 (last version on the 2.x train)
* A version adapted for Nornir 3.x train will be developed soon.

# Installation
1. Clone the repo
  * git clone https://github.com/kdardoufa/Nornir_Check_Route.git

2. cd into directory
  * cd Nornir_Check_Route

3. Create the virtual environment in a sub dir in the same directory
  * python3 -m venv venv

4. Start the virtual environment and install requirements.txt
  * source venv/bin/activate
  * pip install -r requirements.txt

5. Execute the script as any other Python script form console. 
  * python check_route.py

# Comments
1 .Since the testing was done on WSL Ubuntu 18.04.3 and we wanted it to run via crontab, we also had to enable cron services.
_service cron start_

2. For the cron to always start when the WSL is activated: Edit /root/.bashrc, and add the following line at the very end: _service cron start_
(https://scottiestech.info/2018/08/07/run-cron-jobs-in-windows-subsystem-for-linux/)

3. The way to configure crontab with example: _00 07 * * * cd /home/user_home_directory/script_directory/ && /home/user_home_directory/virtual_enviornment_directory/bin/python3 check_route.py > /tmp/cron.log 2>&1_

# Author(s)
This project was written and is maintained by the following individuals
> Katerina Dardoufa (kdardoufa@gmail.com) - Author & maintainer

> Ioannis Theodoridis - maintainer
