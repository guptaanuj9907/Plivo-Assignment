# Kubernetes Cluster on AWS with Terraform

This guide will help you set up a Kubernetes cluster on AWS in the Asia Pacific (Mumbai) region (ap-south-1) using Terraform.

# Prerequisites

Terraform
* AWS CLI
* kubectl
* AWS account with required permissions
* Steps
Clone the repository and navigate to the project directory.

Initialize Terraform:
terraform init

Apply the configuration to create the cluster:

**terraform apply**

Save the kubeconfig output to configure kubectl:


**terraform output kubeconfig > ~/.kube/config
export KUBECONFIG=~/.kube/config**