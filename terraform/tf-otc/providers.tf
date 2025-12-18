terraform {
  required_providers {
    opentelekomcloud = {
      source  = "opentelekomcloud/opentelekomcloud"
      version = "~> 1.36.54"
    }
  }
  cloud { 
    organization = "geri-tf" 
    workspaces { 
      name = "geri-tf" 
    }
  }
}

provider "opentelekomcloud" {
  auth_url    = "https://iam.eu-nl.otc.t-systems.com:443/v3" # IAM endpoint for your region
  domain_name = var.otc_domain
  tenant_name = var.otc_project
  region      = "eu-nl"
  
  # Replace user_name/password with access_key/secret_key
  access_key = var.otc_access_key
  secret_key = var.otc_secret_key
}

# Define sensitive variables
variable "otc_access_key" {
  description = "OTC Access Key (AK)"
  type        = string
  sensitive   = true
}

variable "otc_secret_key" {
  description = "OTC Secret Key (SK)"
  type        = string
  sensitive   = true
}

variable "otc_domain" {
  description = "OTC Domain Name"
  type        = string
  sensitive   = true
}

variable "otc_project" {
  description = "OTC Project ID"
  type        = string
  sensitive   = true
}