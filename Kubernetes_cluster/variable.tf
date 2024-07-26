variable "region" {
  description = "The AWS region to create the cluster in"
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "private_subnets" {
  description = "The CIDR blocks for the private subnets"
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "public_subnets" {
  description = "The CIDR blocks for the public subnets"
  default     = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}
