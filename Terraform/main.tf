provider "aws" {
  region = var.aws_region
}

# --- RDS (Postgres) ---
resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro"
  name                 = "market"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
  publicly_accessible  = true
}

# --- ElastiCache (Redis) ---
resource "aws_elasticache_subnet_group" "redis" {
  name       = "redis-subnet-group"
  subnet_ids = [aws_default_subnet.default.id]
}

resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "robinhook-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  subnet_group_name    = aws_elasticache_subnet_group.redis.name
}

# --- MSK (Kafka) ---
resource "aws_msk_cluster" "kafka" {
  cluster_name           = "robinhook-kafka"
  kafka_version          = "3.6.0"
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type   = "kafka.t3.small"
    client_subnets  = [aws_default_subnet.default.id]
    security_groups = [aws_security_group.kafka.id]
  }
}

resource "aws_security_group" "kafka" {
  name        = "kafka-sg"
  description = "Allow Kafka traffic"
  vpc_id      = aws_default_vpc.default.id

  ingress {
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_default_vpc" "default" {}

resource "aws_default_subnet" "default" {
  availability_zone = data.aws_availability_zones.available.names[0]
}

data "aws_availability_zones" "available" {}

# --- Elastic Beanstalk Application ---
resource "aws_elastic_beanstalk_application" "app" {
  name        = "robinhook-app"
  description = "FastAPI RobinHook App"
}

resource "aws_elastic_beanstalk_environment" "env" {
  name                = "robinhook-env"
  application         = aws_elastic_beanstalk_application.app.name
  solution_stack_name = "64bit Amazon Linux 2 v3.5.7 running Docker"

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DATABASE_URL"
    value     = "postgresql://${var.db_username}:${var.db_password}@${aws_db_instance.postgres.address}:5432/market"
  }
  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "REDIS_URL"
    value     = "redis://${aws_elasticache_cluster.redis.cache_nodes.0.address}:6379/0"
  }
  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "KAFKA_BOOTSTRAP_SERVERS"
    value     = join(",", aws_msk_cluster.kafka.bootstrap_brokers)
  }
  setting {
    namespace = "aws:elasticbeanstalk:container:docker"
    name      = "Dockerfile"
    value     = "Dockerfile"
  }
}

output "beanstalk_url" {
  value = aws_elastic_beanstalk_environment.env.endpoint_url
}