# Makefile for ansible linode examples

# secrets.mk is not under version control and you will need to create it if you
# have not done so.  please see README.md.
include secrets.mk

# This var is only used within the Makefile.  If you change it, you should also
# edit create-linode.yml
GROUP=example_group
LABEL_PREFIX=simple-linode-

# Create a new node and update the inventory file
create: create-node inventory.yml

create-node: vars
	@ansible-playbook create-linode.yml

# Check connectivity for linodes in our group
ping: vars inventory.yml
	@ansible -i inventory.yml $(GROUP) -u root -m ping

# Check connectivity for all of your linodes
ping-all: vars inventory.yml
	@echo This may fail for linodes that require passwords or a different ssh key.
	@ansible -i inventory.yml all -u root -m ping

# Execute a simple command on each linode in the group
date: vars inventory.yml
	@ansible -i inventory.yml $(GROUP) -u root -a "date"

# list group linodes
list-group: vars inventory.yml
	@echo $(GROUP):
	@ansible -i inventory.yml $(GROUP) --list-hosts | tail -n +2

# list all linodes
list-linode: vars inventory.yml
	@echo linode:
	@ansible -i inventory.yml linode --list-hosts | tail -n +2

# Destroy will prompt before deleting each node, but still dangerous.
destroy: vars
	@ansible-inventory -i linode.yml --list | python3 inventory.py > inventory.yml
	$(eval NODES = $(shell ansible -i inventory.yml $(GROUP) --list-hosts | tail -n +2))
	$(foreach h,$(NODES),ansible-playbook -i inventory.yml destroy-linode.yml --extra-vars "label=$(h)";)

clean:
	-rm inventory.yml
	-rm group_vars/all.yml

# Use the linode inventory plugin to generate a current list of hosts
# This output is formatted for /etc/hosts and may be concatenated as
# appropriate.
hosts: linode.yml
	@ansible-inventory -i linode.yml --list | python3 hosts.py

# Update the vars file with latest secrets
vars: group_vars/all.yml

group_vars/all.yml: secrets.mk
	@echo "# Generated on " `date` >  group_vars/all.yml
	@echo "label: ${LABEL_PREFIX}" >> group_vars/all.yml
	@echo "ssh_keys: ${SSH_KEYS}" >> group_vars/all.yml
	@echo "token: ${LINODE_ACCESS_TOKEN}" >> group_vars/all.yml 
	@echo "password: ${SSH_PASSWORD}" >> group_vars/all.yml

# Refresh the inventory file to be sure newly created linodes are included,
# and newly deleted linodes are not
inventory.yml:
	@ansible-inventory -i linode.yml --list | python3 inventory.py > inventory.yml

.PHONY:  ping ping-all list-linode list-group destroy clean hosts inventory.yml
