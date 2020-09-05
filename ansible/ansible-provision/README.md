# ansible provisioning example

This example extends the simple ansible example to provision a new linode after
creating it.

## Setup

Setup is the same as for the ansible example ... see ../ansible/README.md

## Test Drive

This example provides a `Makefile` to ensure that commands are easy to execute.
You can obviously type the commands directly, but use of a `Makefile` ensures
that the commands get the proper variable assignments and include the correct
options.  The `Makefile` also provides you with some additional information about
how all this works (see next section).

### Create and Provision a Linode

To create a linode (after performing the setup), 

```
make create
```


### Destroy the Linode

Once you're done, you'll want to clean up.  The `Makefile` includes a target
that will destroy all of your newly created linodes.  It will prompt you for
each one before destroying it.  To clean up:

```
make destroy
```
And answer "yes" after confirming that the correct linode is being destroyed.



## Guides

[Deploy Linodes Using Ansible](https://www.linode.com/docs/applications/configuration-management/deploy-linodes-using-ansible/)

