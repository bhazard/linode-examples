# hello
A simple terraform script to create an ssh key and a node.

## setup

Install terraform per the instructions in the README above.

Create / copy a public key file to `linode.pub` in this directory.  This pub key
will be uploaded to create a new ssh key in linode.

Copy `terraform.tfvars.template` to `terraform.tfvars`.  Add your API key and
preferred root password.  Edit other values if you wish.

## running

To see what will happen, run `terraform plan`.  If all is well, you should see
what terraform will do if we run it. 

To create the resources for real, use `terraform apply`.  As apply can also be
destructive, this command will prompt you to be sure you want to do the thing ...
type "yes" to apply the changes.  You can avoid the prompt by using the `-auto-approve`
option (i.e., `terraform apply -auto-approve`). 

The apply command will output the public ip address of your new node.  You
should be able to ssh to the node via `ssh root@<the public IP>` and entering
the root password you supplied in the `terraform.tfvars` file.

## undoing the changes

After you've examined the new resources in linode, you'll probably want to
destroy them all (since they're useless as is).  You can destroy all of the
resources via `terraform destroy`.  Again, you'll be prompted to enter `yes`
to confirm destruction.

## 

You will find (not surpisingly) that if you run `terraform apply` again, and try
to ssh to the (new) linode host, `ssh` will complain that the remote host is
not the same host and will refuse to connect.  Since we expect this,
we can avoid this by using `ssh root@<the public IP> -o StrictHostKeyChecking=no`.

You could also remove the IP from `~/.ssh/known_hosts`, or you can add the option
to `~/.ssh/config` if you will be playing for a little bit (note that the IP may eventually change and you probably don't want this as a "permanent" change to your
ssh config).

```
Host <the public IP>
  StrictHostKeyChecking no
```

