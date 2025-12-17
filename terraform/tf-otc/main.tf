# main.tf
# 1. Create a VPC
resource "opentelekomcloud_vpc_v1" "example_vpc" {
  name = "my_vpc"
  cidr = "192.168.0.0/16" # Use a private CIDR block
}