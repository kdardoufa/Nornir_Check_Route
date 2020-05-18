## Description 

We were looking for a quick way to identify which routers in our infrastructure where utilizing their ADSL link. 
Since we are using GETVPN and the actual links (primary/secondary) are on the providers equipment, and taking into account that
when the backup link is utilized a specific route dissappears from the routing table, we decided to look for that exact route. 
The initial attempt was done creating a scheduled job in Cisco Prime Infrastructure, but the process took a long time and involved
manually going over the output to figure out which devices where using the backup link. 
Using Nornir greatly improved performance! The devices using the backup link are written to a file (name/IP address).

# Configuration
The following should be configured by the user, according to their environment.
- inventory directory: defaults.yaml, devices.yaml, groups.yaml

# Technologies & Frameworks Used
* Nornir.
* WSL - Ubuntu 18.04.3
* The script is written in Python 3.

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
Since the testing was done on WSL Ubuntu 18.04.3 and we wanted it to run via crontab, we also had to enable cron services.
* service cron start
For the cron to always start when the WSL is activated:
* Edit /root/.bashrc, and add the following line at the very end: service cron start
(https://scottiestech.info/2018/08/07/run-cron-jobs-in-windows-subsystem-for-linux/)
The way to configure crontab with example:
* 00 07 * * * cd /home/user_home_directory/script_directory/ && /home/user_home_directory/virtual_enviornment_directory/bin/python3 check_route.py > /tmp/cron.log 2>&1

# Author(s)
This project was written and is maintained by the following individuals
> Katerina Dardoufa (kdardoufa@gmail.com)
