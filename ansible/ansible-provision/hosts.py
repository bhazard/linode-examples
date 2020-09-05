# Simple script to take json output from linode's dynamic ansible inventory
# and generate output for a hosts file.
# 
# Usage:
#     ansible-inventory -i linode.yml --list | python3 inventory.py

import sys, json

j = json.load(sys.stdin)['_meta']['hostvars']

for k in j.keys():
  print(f'{j[k]["ipv4"][0]}\t{k}')
