provider "linode" {
  token = var.linode_api_token
}

resource "linode_sshkey" "terraform" {
  label = "terraform"
  ssh_key = chomp(file(var.pub_ssh_key_file))
}

resource "linode_instance" "hello" {
        image = var.web_image_name
        label = "terraform-hello"
        group = "terraform-hello"
        region = var.region
        type = var.web_image_type
        authorized_keys = [ linode_sshkey.terraform.ssh_key ]
        root_pass = var.root_password
        tags = [
          "env-type:dev",
          "creator:terraform",
          "app:hello"
        ]
}

output "public_ip" {
  value = linode_instance.hello.ip_address
}
