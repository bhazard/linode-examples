variable "linode_api_token" {
  description = "Linode API token"
}

variable "pub_ssh_key_file" {
  description = "Linode API token"
}

variable "root_password" {
  description = "root password"
}

variable "web_image_name" {
  description = "Image for web servers"
  default = "linode/ubuntu18.04"
}

variable "web_image_type" {
  description = "Image type for web servers"
  default = "g6-nanode-1"
}

variable "region" {
  default = "us-east"
}
