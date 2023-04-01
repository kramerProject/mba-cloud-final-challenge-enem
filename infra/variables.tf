variable "region" {
  description = "AWS region"
  type = string
  default = "us-east-1"
}

variable "project_name" {
  description = "project name"
  type = string
  default = "btc-edc-m3-kramer"
}

variable "glue_crawler_name" {
  default = "glue_crawler_enem"
}

variable "database_name" {
  default = "enem-challenge-db"
}

variable "glue_role" {
  default = "arn:aws:iam::401868797180:role/service-role/AWSGlueServiceRole-kramer-test-igti"
}

locals {
  cluster_name = "${var.project_name}-eks"
}