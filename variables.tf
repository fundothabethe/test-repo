# Variables for the ultra-expensive Terraform configuration

variable "key_pair_name" {
  description = "Name of the EC2 Key Pair to use for instances"
  type        = string
  default     = "my-key-pair"
  
  validation {
    condition     = length(var.key_pair_name) > 0
    error_message = "Key pair name cannot be empty."
  }
}

variable "environment" {
  description = "Environment name (will be used in resource naming)"
  type        = string
  default     = "ultra-expensive-test"
  
  validation {
    condition     = length(var.environment) > 0 && length(var.environment) <= 20
    error_message = "Environment name must be between 1 and 20 characters."
  }
}

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
  
  validation {
    condition = can(regex("^[a-z0-9-]+$", var.aws_region))
    error_message = "AWS region must be a valid region name."
  }
}

variable "enable_gpu_instances" {
  description = "Enable GPU instances (WARNING: These are EXTREMELY expensive - $32.77/hour each!)"
  type        = bool
  default     = true
}

variable "enable_high_memory_instances" {
  description = "Enable high memory instances (WARNING: $26.69/hour each!)"
  type        = bool
  default     = true
}

variable "enable_database_clusters" {
  description = "Enable RDS and ElastiCache clusters (WARNING: Very expensive!)"
  type        = bool
  default     = true
}

variable "enable_elasticsearch" {
  description = "Enable Elasticsearch clusters (WARNING: Expensive!)"
  type        = bool
  default     = true
}

variable "ebs_volume_size" {
  description = "Size of each EBS volume in GB (WARNING: Large volumes are very expensive!)"
  type        = number
  default     = 5000
  
  validation {
    condition     = var.ebs_volume_size >= 100 && var.ebs_volume_size <= 10000
    error_message = "EBS volume size must be between 100 and 10000 GB."
  }
}

variable "ebs_volume_iops" {
  description = "IOPS for EBS volumes (WARNING: High IOPS are extremely expensive!)"
  type        = number
  default     = 20000
  
  validation {
    condition     = var.ebs_volume_iops >= 100 && var.ebs_volume_iops <= 64000
    error_message = "EBS volume IOPS must be between 100 and 64000."
  }
}

variable "rds_storage_size" {
  description = "Storage size for RDS instances in GB"
  type        = number
  default     = 10000
  
  validation {
    condition     = var.rds_storage_size >= 100 && var.rds_storage_size <= 20000
    error_message = "RDS storage size must be between 100 and 20000 GB."
  }
}

variable "db_username" {
  description = "Username for RDS instances"
  type        = string
  default     = "admin"
  sensitive   = true
}

variable "db_password" {
  description = "Password for RDS instances"
  type        = string
  default     = "ExpensivePassword123!"
  sensitive   = true
  
  validation {
    condition     = length(var.db_password) >= 8
    error_message = "Database password must be at least 8 characters long."
  }
}

variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default = {
    Project     = "ultra-expensive-infrastructure"
    Environment = "test"
    Owner       = "terraform"
    CostCenter  = "EXTREMELY-HIGH"
    Warning     = "ULTRA-EXPENSIVE-DELETE-ASAP"
  }
}

# Local values for computed configurations
locals {
  # Availability zones
  azs = slice(data.aws_availability_zones.available.names, 0, 3)
  
  # Common tags merged with variables
  common_tags = merge(var.common_tags, {
    Environment = var.environment
    Terraform   = "true"
    CreatedDate = timestamp()
  })
  
  # Instance configurations
  gpu_instance_config = {
    count         = var.enable_gpu_instances ? 2 : 0
    instance_type = "p4d.24xlarge"  # $32.77/hour each
    root_size     = 2000
    root_iops     = 15000
  }
  
  high_memory_config = {
    count         = var.enable_high_memory_instances ? 3 : 0
    instance_type = "x1e.32xlarge"  # $26.69/hour each
    root_size     = 3000
    root_iops     = 18000
  }
  
  compute_config = {
    count         = 4
    instance_type = "c5n.18xlarge"  # $3.89/hour each
    root_size     = 1500
    root_iops     = 12000
  }
  
  storage_config = {
    count         = 2
    instance_type = "i3en.24xlarge"  # $10.85/hour each
    root_size     = 2000
    root_iops     = 15000
  }
}
