# ansible linode example(s)

This directory provides a few different simple ansible examples for controling
linode nodes.  The examples include:

- create-linode -- creates one linode
- destroy-linode -- destroys one linode

## Setup

If you use `pipenv`, you can install required packages via `pipenv install` and
then activate the environment via `pipenv shell`.  

If you do not use `pipenv`, you can install via `pip` as follows:

`pip install ansible linode_api4`


### Secrets

This example takes a simple approach to secrets management -- we'll put them
in an unversioned file.  Not the best approach for security, but works for a
simple example.  There's a separate example that demonstrates how to use
hashicorp's secrets vault.

Start by creating a public key to use for accessing your nodes.  Our example uses
the name linode.pub, but call it whatever you like.  The public key will be uploaded
to the new linodes to identify root.

You will also need to edit the variables file to configure the example for
your needs.  In particular, you will need to add your token, a root password
and the path to your pub key.

Copy the file `secrets.mk.template` to `secrets.mk` and edit it to add your
linode token, your ssh key(s) and the root password you'd like to use for your
new nodes.


## Test Drive

This example provides a `Makefile` to ensure that commands are easy to execute.
You can obviously type the commands directly, but use of a `Makefile` ensures
that the commands get the proper variable assignments and include the correct
options.  The `Makefile` also provides you with some additional information about
how all this works (see next section).

### Create a Linode

To create a linode (after performing the setup above), 

```
make create
```

You can ping your new nodes by running:

```
make ping
````

Ansible communicates with
its hosts via `ssh`, so an ansible "ping" is more than just an ICMP ping -- ansible
will login to the remote host and verify that Note that it takes a minute
or two for `sshd` to be listening, so if the first go fails, try waiting a little
bit and trying again.

If you run `make create` again, it will create another linode.  And now, `make ping`
will ping both of them.

To execute a command on all of your linode hosts, you can do so easily by using
the linode group.  For example, to show the date on all linodes:

```
ansible -i inventory.yml linode -u root -a "date"
```

You can list the nodes via `make hosts`, which will show you both the label and the
IP addy for the new nodes.  Note that the output of `make hosts` is compatible with
standard hosts format, so if you like, you can append the output to your hosts file
and then use host names in lieu of ip addy's in the examples below.

You can ssh to one of the nodes via:

```
ssh root@ip
```

### Destroy the Linodes

Once you're done, you'll want to clean up.  The `Makefile` includes a target
that will destroy all of your newly created linodes.  It will prompt you for
each one before destroying it.  To clean up:

```
make destroy
```
And answer "yes" after confirming that the correct linode is being destroyed.


## How it Works

Our goal is to be able to create, modify or destroy linodes using Ansible.  Ansible
interacts with linodes in one of two ways.  If it is creating linodes, modifying attributes
of linodes or destroying linodes, it uses the linode v4 API.  Such interactions 
use playbooks that run on your local machine (localhost).  The second type of interaction
is to modify what's running on your linode.  For those interactions, Ansible will
ssh to your linode and execute commands there to update that linode.  So to say
a little differently, to create or destroy a linode, or to modify a linode's
properties, Ansible runs a local playbook and to modify the content of a linode,
Ansible targets that linode via its inventory and related mechanisms to run a
playbook on that node.

### Creating and Destroying Linodes

To create or destroy a linode (or to modify its properties), you will use a 
playbook that targets localhost.  

When managing linode resources in your linode account, we need a machine to
interact with that environment.  For that purpose, your localhost will be fine.

Ansible also operates via an inventory -- a list of hosts that it knows about.
This inventory is created and managed by the `Makefile` as `inventory.yml`.  You'll
note that most commands include a reference to this file in the form, `-i inventory.yml`.
That file is generated via a `makefile` target, `inventory.yml`.  That target
uses an ansible command to gather information about the relevant hosts, and a
small python script (`inventory.py`) to format the output properly for an inventory
file.  The only important bit of information is really the public IP address, which
you'll see as an attribute for each host in `inventory.yml`.  You could avoid much
of this by adding the hosts to your hosts file (perhaps via an ansible task!).

## Guides
[Deploy Linodes Using Ansible](https://www.linode.com/docs/applications/configuration-management/deploy-linodes-using-ansible/)

## To-dos

- [ ] Add hosts to the local hosts file and ditch the inventory file bits.
