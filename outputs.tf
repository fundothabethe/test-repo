# Output values for the ultra-expensive Terraform infrastructure

output "total_estimated_hourly_cost" {
  description = "WARNING: Estimated hourly cost breakdown"
  value = <<-EOT
    🚨 ULTRA EXPENSIVE INFRASTRUCTURE COST BREAKDOWN (PER HOUR):
    
    💰 EC2 INSTANCES:
    - 2x p4d.24xlarge (GPU):     $65.54/hour  ($32.77 each)
    - 3x x1e.32xlarge (Memory):  $80.06/hour  ($26.69 each)  
    - 4x c5n.18xlarge (Compute): $15.55/hour  ($3.89 each)
    - 2x i3en.24xlarge (Storage): $21.70/hour  ($10.85 each)
    
    💾 EBS STORAGE:
    - 30TB+ io2 volumes with 20k IOPS: ~$3,750/month + $13,000/month IOPS = ~$556/day
    
    🗄️  DATABASE & CACHE:
    - 2x db.r6g.24xlarge RDS:    $34.56/hour  ($17.28 each)
    - 2x ElastiCache clusters:   $77.76/hour  (6 nodes × $6.48 each × 2 clusters)
    - 2x Elasticsearch clusters: $54.43/hour  (9 nodes × $1.01 each + masters × 2 clusters)
    
    🌐 NETWORKING:
    - 3x NAT Gateways:           $3.24/hour   ($0.045 each × 3 + data processing)
    - 5x Load Balancers:         $1.01/hour   ($0.0225 each × 3 ALBs + $0.0225 × 2 NLBs)
    
    ⚡ TOTAL ESTIMATED HOURLY COST: ~$350-400/hour
    📊 TOTAL ESTIMATED DAILY COST:  $8,400-9,600/day  
    💸 TOTAL ESTIMATED MONTHLY COST: $250,000-290,000/month
    
    ⚠️  WARNING: This is an EXTREMELY expensive setup that will cost more than most people's annual salary!
  EOT
}

output "vpc_id" {
  description = "ID of the expensive VPC"
  value       = aws_vpc.expensive_vpc.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public_subnets[*].id
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = aws_subnet.private_subnets[*].id
}

output "gpu_instance_ids" {
  description = "IDs of the GPU instances (ULTRA EXPENSIVE!)"
  value       = aws_instance.gpu_instances[*].id
}

output "gpu_instance_public_ips" {
  description = "Public IPs of the GPU instances"
  value       = aws_instance.gpu_instances[*].public_ip
}

output "high_memory_instance_ids" {
  description = "IDs of the high memory instances"
  value       = aws_instance.high_memory_instances[*].id
}

output "high_memory_instance_public_ips" {
  description = "Public IPs of the high memory instances"
  value       = aws_instance.high_memory_instances[*].public_ip
}

output "compute_instance_ids" {
  description = "IDs of the compute instances"
  value       = aws_instance.compute_instances[*].id
}

output "storage_instance_ids" {
  description = "IDs of the storage instances"
  value       = aws_instance.storage_instances[*].id
}

output "alb_dns_names" {
  description = "DNS names of the Application Load Balancers"
  value       = aws_lb.expensive_albs[*].dns_name
}

output "nlb_dns_names" {
  description = "DNS names of the Network Load Balancers"
  value       = aws_lb.expensive_nlbs[*].dns_name
}

output "rds_endpoints" {
  description = "RDS instance endpoints"
  value       = aws_db_instance.expensive_rds[*].endpoint
}

output "redis_endpoints" {
  description = "Redis cluster endpoints"
  value       = aws_elasticache_replication_group.expensive_redis[*].primary_endpoint_address
}

output "elasticsearch_endpoints" {
  description = "Elasticsearch cluster endpoints"
  value       = aws_elasticsearch_domain.expensive_es[*].endpoint
}

output "ebs_volume_ids" {
  description = "IDs of the ultra-expensive EBS volumes"
  value       = aws_ebs_volume.ultra_expensive_volumes[*].id
}

output "nat_gateway_ids" {
  description = "IDs of the NAT Gateways"
  value       = aws_nat_gateway.nat_gateways[*].id
}

output "critical_warning" {
  description = "CRITICAL WARNING MESSAGE"
  value = <<-EOT
    🚨🚨🚨 CRITICAL WARNING 🚨🚨🚨
    
    This Terraform configuration will create EXTREMELY expensive AWS resources!
    
    💰 Estimated cost: $250,000-290,000 PER MONTH
    🔥 That's $8,400-9,600 PER DAY!
    ⏰ That's $350-400 PER HOUR!
    
    📋 BEFORE APPLYING:
    ✅ Ensure you have a MASSIVE AWS budget
    ✅ Set up billing alerts immediately  
    ✅ Have a plan to destroy resources ASAP
    ✅ Monitor costs continuously
    
    🛑 REMEMBER TO RUN 'terraform destroy' IMMEDIATELY AFTER TESTING!
    
    💡 This is for educational/demonstration purposes only!
  EOT
}
