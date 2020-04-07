##################################################################
# Website Blocker 
# Description:
# This program rewrites the hosts file to add 
# specified addresses to point to the local loopback address
# so it is not accessible.
##################################################################


# Import modules
import os # for accessing OS files
import time as t # For accessing time module
from datetime import datetime as dt # for accessing datetime module

# Path to hosts file
hosts_path = "C:\\Windows\\system32\\drivers\\etc\\hosts"
# Path to alternate hosts file, for testing
temp_path = "hosts"
# List of websites to block
website_list = ["www.facebook.com","facebook.com","gmail.com","www.gmail.com"]
redirect="127.0.0.1"
# Alternative "row" line to tell Python to ignore escape characters
# hosts_path = r"C:\Windows\system32\drivers\etc\hosts"

# Infinite loop
# meant to run as a process 
while True:
    # if the hour is between 8 AM and 4 PM 
    if 8 <= dt.now().hour < 16:
        print("Working hours")
        # open the hosts file for writing
        with open(hosts_path,'r+') as file:
            content = file.read()
            # add the websites in the websites list to the host file 
            # if the website already exists in the file, don't add it 
            for website in website_list:
                if website in content:
                    pass
                # if it doesn't exist, add it to the list 
                else:
                    file.write(f"{redirect}\t{website}\n")
    # if it is outside of those bound (ie "play time"), then rewrite the file 
    else:
        print("Not working hours")
        with open(hosts_path,'r+') as file:
            # read the lines
            content = file.readlines()
            # place cursor at the beginning of the file 
            file.seek(0)
            # for the lines just read, if the item does not exist in the 
            # websites list, add it to the file from the beginning of the 
            # file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                # after writing, truncate the end 
                file.truncate()

    # sleep for an hour 
    # so loop will run once an hour 
    t.sleep(3600)
