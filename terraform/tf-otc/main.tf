# resource "opentelekomcloud_vpc_v1" "testVPC" {
#   name = "testVPC"
#   cidr = "192.168.0.0/16" # Use a private CIDR block
# }

resource "opentelekomcloud_compute_instance_v2" "TestECS" {
  name            = "TestECS"
  image_id        = "b3e8b5a3-638a-42d5-a069-75a54e2388df"
  flavor_id       = "s7n.small.1"
  key_pair        = "gKollar_NL"
  security_groups = ["default"]
  user_data       = <<-EOF
              #!/bin/bash
              echo "Hello, World 1" > index.html
              python3 -m http.server 8080 &
              EOF
}
