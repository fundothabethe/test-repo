# Terraform configuration file
# Provider configuration with AWS credentials and region settings

provider "aws" {
  region = var.aws_region

  # Default tags applied to all resources
  default_tags {
    tags = local.common_tags
  }
}

# Backend configuration for storing Terraform state
# Uncomment and configure if using remote state storage
/*
terraform {
  backend "s3" {
    bucket  = "your-terraform-state-bucket"
    key     = "ultra-expensive/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
    
    # DynamoDB table for state locking
    dynamodb_table = "terraform-state-locks"
  }
}
*/
