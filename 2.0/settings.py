import os
import re

current_dir = os.path.dirname(os.path.realpath(__file__))


# Request
url = 'https://www.glassdoor.com/Reviews/Snap-Reviews-E671946.htm'

name = re.findall(r'https://.+/Reviews/([A-Za-z0-9].+).htm', url)
name = name[0] + '.db'

# print(name)
# Database
# database = name
database = 'snapchat.db'
host = ""
user = ""

# Proxies
proxies = [
    # your list of proxy IP addresses goes here
    # check out https://proxybonanza.com/?aff_id=629
    # for a quick, easy-to-use proxy service
]
proxy_user = ""
proxy_pass = ""
proxy_port = ""

