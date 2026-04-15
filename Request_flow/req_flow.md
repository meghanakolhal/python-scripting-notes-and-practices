User Browser
   |
   | (1) DNS Query
   v
Route53 (Public Hosted Zone)
   |
   | (2) Alias → ALB DNS
   v
================ INTERNET =================
   |
   v
Internet Gateway (IGW attached to VPC)
   |
   v
Public Subnet (AZ-1 / AZ-2)
   |
   |-- Route Table: 0.0.0.0/0 → IGW
   |
   v
ALB (in 2 AZs for HA)
   |
   |-- Security Group:
   |     Inbound: 443 from 0.0.0.0/0
   |     Outbound: to EKS CIDR
   |
   | (3) HTTPS → HTTP (SSL Termination via ACM)
   v
Target Group (IP mode)
   |
   |-- Health Checks (/health)
   |
   v
Private Subnet (EKS Worker Nodes - AZ-1 / AZ-2)
   |
   |-- Route Table:
   |     0.0.0.0/0 → NAT Gateway
   |
   |-- NACL (stateless filtering)
   |
   v
EKS Worker Nodes (EC2)
   |
   |-- Security Group:
   |     Allow ALB SG → Node traffic
   |
   v
Pod Network (AWS VPC CNI)
   |
   |-- Each pod gets VPC IP
   |
   v
NGINX Ingress Controller Pod
   |
   | (4) Host/Path routing
   v
Kubernetes Service (ClusterIP)
   |
   v
Application Pods