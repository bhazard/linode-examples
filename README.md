# linode-examples
Examples for setting up various [linode](linode.com) application configurations using 
[terraform](terraform.io), stackscripts, ansible and more. 

The linode doc includes a Guide called [How to Build Your Infrastructure Using Terraform and Linode](https://www.linode.com/docs/applications/configuration-management/terraform/how-to-build-your-infrastructure-using-terraform-and-linode/) which
provides a good introduction for how to get started with Terraform and Linode,
but it does not cover provisioning of VM's or more concrete examples such as
multi-node setups and networking.  This small repository attempts to fill those
gaps via more complete examples.

## Contributing

Pull-requests, suggestions and issue reports are all welcome and available via the
normal github mechanisms.

## Tools and Setup

To run these examples, you'll need a few things.  The [Guide](https://www.linode.com/docs/applications/configuration-management/terraform/how-to-build-your-infrastructure-using-terraform-and-linode/) mentioned above
covers terraform setup, so we only summarize here.  Refer to the guide if you
need more detail.

First, you'll need a linode account.  These are easy to create and very inexpensive
to use (but you probably already know that).  See linode.com.

You'll also need a linode API key.  Terraform uses the API to do its thing.

And finally, some tools.  All of these examples use [terraform](terraform.io) along 
with the linode terraform provisioner.

## Examples

Each example is presented in a separate directory and described briefly below.

### hello

Creates one node to be sure terraform is running.

Uses: terraform

### stackscript node

Uses: terraform and linode's stackscript

### ansible node


### webapp

Builds a simple 3-node webapp including a flask / nginx web front end, a postgresql
backend and a load balancer.

### jenkins x

### testing infrastructure

# To-dos

# Reference Information

- [Terraform Linode Provide Reference](https://registry.terraform.io/providers/linode/linode/latest/docs)
