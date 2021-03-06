# Simple script to take json output from linode's dynamic ansible inventory
# and generate output to create an ansible inventory file.
# 
# Usage:
#     ansible-inventory -i linode.yml --list | python3 inventory.py

import sys, json
from datetime import datetime

# Read json from standard input
j = json.load(sys.stdin)

# Grab the main list of hosts
hosts_json = j['_meta']['hostvars']

print("# inventory.yml")
print("# autogenerated file.  Do not edit directly.")
print(f"# Generated: {datetime.now()}")
print("# ---------------------------------------------------------------\n")

print("# The all group is implied, and would target every node that is idenfitied in your inventory.\n")

print("# List of all nodes that can be targeted on linode")
print("linode:")
print("  hosts:")

# The hostvars dict has an object for each host.  That object has info that we may
# need to connect to the host.  Like the IP addy for example.  We'll grab that
# and include it in our inventory so that we don't need to muck with our hosts
# file.
for h in hosts_json.keys():
  print(f'    {h}:')
  print(f'      ansible_host: {hosts_json[h]["ipv4"][0]}\n')


# And under the list of hosts, we have some linode groups that we may wish
# to make use of in targeting.
print("  children:")

# Loop over groups
for g in j['all']['children']:

  # Skip hosts that are not in any group -- we didn't create them for sure.
  if g != "ungrouped":

    # Output the group name
    print(f'    {g}:')
    print(f'      hosts:')

    # And for each host in the group, output that name.
    for h in j[g]['hosts']:
      print(f'        {h}:')
