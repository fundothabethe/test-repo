# Terraform configuration for EXTREMELY expensive AWS infrastructure
# WARNING: This will incur MASSIVE charges - potentially $500-1000+ per day!

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Variables
variable "key_pair_name" {
  description = "Name of the EC2 Key Pair"
  type        = string
  default     = "my-key-pair"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "expensive-test"
}

# Data sources
data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# VPC and Networking
resource "aws_vpc" "expensive_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
    CostCenter  = "VERY-EXPENSIVE"
  }
}

resource "aws_subnet" "public_subnets" {
  count = 3
  
  vpc_id                  = aws_vpc.expensive_vpc.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.environment}-public-subnet-${count.index + 1}"
  }
}

resource "aws_subnet" "private_subnets" {
  count = 3
  
  vpc_id            = aws_vpc.expensive_vpc.id
  cidr_block        = "10.0.${count.index + 10}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${var.environment}-private-subnet-${count.index + 1}"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.expensive_vpc.id

  tags = {
    Name = "${var.environment}-igw"
  }
}

resource "aws_eip" "nat_eips" {
  count  = 3
  domain = "vpc"

  tags = {
    Name = "${var.environment}-nat-eip-${count.index + 1}"
  }
}

resource "aws_nat_gateway" "nat_gateways" {
  count = 3
  
  allocation_id = aws_eip.nat_eips[count.index].id
  subnet_id     = aws_subnet.public_subnets[count.index].id

  tags = {
    Name = "${var.environment}-nat-gateway-${count.index + 1}"
  }

  depends_on = [aws_internet_gateway.igw]
}

# Route Tables
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.expensive_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "${var.environment}-public-rt"
  }
}

resource "aws_route_table" "private_rts" {
  count  = 3
  vpc_id = aws_vpc.expensive_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateways[count.index].id
  }

  tags = {
    Name = "${var.environment}-private-rt-${count.index + 1}"
  }
}

resource "aws_route_table_association" "public_rta" {
  count = 3
  
  subnet_id      = aws_subnet.public_subnets[count.index].id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "private_rta" {
  count = 3
  
  subnet_id      = aws_subnet.private_subnets[count.index].id
  route_table_id = aws_route_table.private_rts[count.index].id
}

# Security Groups
resource "aws_security_group" "expensive_sg" {
  name        = "${var.environment}-expensive-sg"
  description = "Security group for expensive instances"
  vpc_id      = aws_vpc.expensive_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.environment}-expensive-sg"
  }
}

# EXTREMELY EXPENSIVE EBS Volumes
resource "aws_ebs_volume" "ultra_expensive_volumes" {
  count = 6
  
  availability_zone = data.aws_availability_zones.available.names[count.index % 3]
  size              = 5000  # 5TB each!
  type              = "io2"
  iops              = 20000  # Maximum IOPS for ultra-high cost
  encrypted         = true
  
  tags = {
    Name = "${var.environment}-ultra-expensive-volume-${count.index + 1}"
    Cost = "ULTRA-HIGH"
  }
}

# ULTRA EXPENSIVE EC2 INSTANCES

# GPU Instance for ML/AI workloads - EXTREMELY EXPENSIVE!
resource "aws_instance" "gpu_instances" {
  count = 2
  
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "p4d.24xlarge"  # $32.77/hour each!
  key_name        = var.key_pair_name
  subnet_id       = aws_subnet.public_subnets[count.index].id
  security_groups = [aws_security_group.expensive_sg.id]

  root_block_device {
    volume_size           = 2000  # 2TB root volume
    volume_type           = "io2"
    iops                  = 15000
    delete_on_termination = false
    encrypted             = true
  }

  user_data = base64encode(<<-EOF
    #!/bin/bash
    yum update -y
    yum install -y docker
    systemctl start docker
    systemctl enable docker
    echo "<h1>GPU Instance ${count.index + 1} - ULTRA EXPENSIVE</h1>" > /tmp/index.html
  EOF
  )

  tags = {
    Name = "${var.environment}-gpu-instance-${count.index + 1}"
    Type = "GPU-ULTRA-EXPENSIVE"
    Cost = "MAXIMUM"
  }
}

# High Memory Instances
resource "aws_instance" "high_memory_instances" {
  count = 3
  
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "x1e.32xlarge"  # $26.688/hour each!
  key_name        = var.key_pair_name
  subnet_id       = aws_subnet.public_subnets[count.index].id
  security_groups = [aws_security_group.expensive_sg.id]

  root_block_device {
    volume_size           = 3000  # 3TB root volume
    volume_type           = "io2"
    iops                  = 18000
    delete_on_termination = false
    encrypted             = true
  }

  tags = {
    Name = "${var.environment}-high-memory-${count.index + 1}"
    Type = "HIGH-MEMORY-EXPENSIVE"
  }
}

# Compute Optimized Instances
resource "aws_instance" "compute_instances" {
  count = 4
  
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "c5n.18xlarge"  # $3.888/hour each
  key_name        = var.key_pair_name
  subnet_id       = aws_subnet.public_subnets[count.index % 3].id
  security_groups = [aws_security_group.expensive_sg.id]

  root_block_device {
    volume_size           = 1500
    volume_type           = "io2"
    iops                  = 12000
    delete_on_termination = false
    encrypted             = true
  }

  tags = {
    Name = "${var.environment}-compute-${count.index + 1}"
    Type = "COMPUTE-EXPENSIVE"
  }
}

# Storage Optimized Instances
resource "aws_instance" "storage_instances" {
  count = 2
  
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "i3en.24xlarge"  # $10.848/hour each
  key_name        = var.key_pair_name
  subnet_id       = aws_subnet.public_subnets[count.index].id
  security_groups = [aws_security_group.expensive_sg.id]

  root_block_device {
    volume_size           = 2000
    volume_type           = "io2"
    iops                  = 15000
    delete_on_termination = false
    encrypted             = true
  }

  tags = {
    Name = "${var.environment}-storage-${count.index + 1}"
    Type = "STORAGE-EXPENSIVE"
  }
}

# Attach EBS volumes to instances
resource "aws_volume_attachment" "ebs_attachments" {
  count = 6
  
  device_name = "/dev/sd${substr("fghijk", count.index, 1)}"
  volume_id   = aws_ebs_volume.ultra_expensive_volumes[count.index].id
  instance_id = count.index < 2 ? aws_instance.gpu_instances[count.index].id : aws_instance.high_memory_instances[count.index - 2].id
}

# Application Load Balancers (multiple for high availability and cost)
resource "aws_lb" "expensive_albs" {
  count = 3
  
  name               = "${var.environment}-alb-${count.index + 1}"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.expensive_sg.id]
  subnets            = aws_subnet.public_subnets[*].id

  enable_deletion_protection = false

  tags = {
    Name = "${var.environment}-alb-${count.index + 1}"
  }
}

# Network Load Balancers for additional costs
resource "aws_lb" "expensive_nlbs" {
  count = 2
  
  name               = "${var.environment}-nlb-${count.index + 1}"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public_subnets[*].id

  enable_deletion_protection = false

  tags = {
    Name = "${var.environment}-nlb-${count.index + 1}"
  }
}

# RDS Instances with maximum specifications
resource "aws_db_subnet_group" "expensive_db_subnet_group" {
  name       = "${var.environment}-db-subnet-group"
  subnet_ids = aws_subnet.private_subnets[*].id

  tags = {
    Name = "${var.environment}-db-subnet-group"
  }
}

resource "aws_db_instance" "expensive_rds" {
  count = 2
  
  identifier = "${var.environment}-expensive-rds-${count.index + 1}"
  
  engine         = "postgres"
  engine_version = "15.4"
  instance_class = "db.r6g.24xlarge"  # $17.28/hour each!
  
  allocated_storage     = 10000  # 10TB
  max_allocated_storage = 20000  # Can auto-scale to 20TB
  storage_type          = "io1"
  iops                  = 20000
  storage_encrypted     = true
  
  db_name  = "expensivedb${count.index + 1}"
  username = "admin"
  password = "ExpensivePassword123!"
  
  db_subnet_group_name   = aws_db_subnet_group.expensive_db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.expensive_sg.id]
  
  backup_retention_period = 35  # Maximum retention
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  multi_az               = true  # Doubles the cost
  publicly_accessible    = false
  deletion_protection    = false
  skip_final_snapshot    = true
  
  performance_insights_enabled = true
  monitoring_interval          = 60
  
  tags = {
    Name = "${var.environment}-expensive-rds-${count.index + 1}"
    Type = "DATABASE-ULTRA-EXPENSIVE"
  }
}

# ElastiCache Redis clusters
resource "aws_elasticache_subnet_group" "expensive_cache_subnet_group" {
  name       = "${var.environment}-cache-subnet-group"
  subnet_ids = aws_subnet.private_subnets[*].id
}

resource "aws_elasticache_replication_group" "expensive_redis" {
  count = 2
  
  replication_group_id       = "${var.environment}-redis-${count.index + 1}"
  description                = "Expensive Redis cluster ${count.index + 1}"
  
  node_type                  = "cache.r6g.12xlarge"  # $6.48/hour per node
  num_cache_clusters         = 6  # 6 nodes per cluster
  
  engine                     = "redis"
  engine_version             = "7.0"
  port                       = 6379
  parameter_group_name       = "default.redis7"
  subnet_group_name          = aws_elasticache_subnet_group.expensive_cache_subnet_group.name
  security_group_ids         = [aws_security_group.expensive_sg.id]
  
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  
  automatic_failover_enabled = true
  multi_az_enabled          = true
  
  tags = {
    Name = "${var.environment}-redis-${count.index + 1}"
    Type = "CACHE-EXPENSIVE"
  }
}

# Elasticsearch/OpenSearch clusters
resource "aws_elasticsearch_domain" "expensive_es" {
  count = 2
  
  domain_name           = "${var.environment}-es-${count.index + 1}"
  elasticsearch_version = "7.10"

  cluster_config {
    instance_type            = "r6g.2xlarge.elasticsearch"  # $1.008/hour per node
    instance_count           = 9  # 9 nodes per cluster
    dedicated_master_enabled = true
    master_instance_type     = "r6g.large.elasticsearch"
    master_instance_count    = 3
    zone_awareness_enabled   = true
    
    zone_awareness_config {
      availability_zone_count = 3
    }
  }

  ebs_options {
    ebs_enabled = true
    volume_type = "io1"
    volume_size = 1000  # 1TB per node
    iops        = 3000
  }

  vpc_options {
    subnet_ids         = aws_subnet.private_subnets[*].id
    security_group_ids = [aws_security_group.expensive_sg.id]
  }

  encrypt_at_rest {
    enabled = true
  }

  node_to_node_encryption {
    enabled = true
  }

  domain_endpoint_options {
    enforce_https = true
  }

  tags = {
    Name = "${var.environment}-elasticsearch-${count.index + 1}"
    Type = "SEARCH-EXPENSIVE"
  }
}
