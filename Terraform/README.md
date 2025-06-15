# 🚀 RobinHook AWS Deployment Guide

This guide explains how to deploy the RobinHook FastAPI app and its dependencies (Postgres, Redis, Kafka) to AWS using Elastic Beanstalk, RDS, ElastiCache, and MSK, with Terraform for infrastructure as code.

---

## 🗂️ Project Structure

- **Terraform/**
  - `main.tf`, `variables.tf`, `outputs.tf`: Terraform files to provision AWS resources.
  - `Dockerrun.aws.json`: Beanstalk config for deploying your Docker image.
- **app/**: Your FastAPI application code.
- **Dockerfile**: Docker build instructions for your app.
- **.env**: (Not committed) Environment variables for local/dev use.

---

## 🛠️ AWS Services Used

- **Elastic Beanstalk**: Hosts your FastAPI Docker app.
- **RDS (Postgres)**: Managed PostgreSQL database.
- **ElastiCache (Redis)**: Managed Redis cache.
- **MSK (Kafka)**: Managed Kafka cluster for event streaming.

---

## 🚦 Deployment Steps

### 1. **Build and Push Your Docker Image**
```sh
docker build -t longbui23/robinhook:latest .
docker push longbui23/robinhook:latest
```

### 2. **Configure Terraform Variables**
Edit `Terraform/variables.tf` to set your AWS region and DB password.

### 3. **Provision AWS Infrastructure**
```sh
cd Terraform
terraform init
terraform apply
```
- This will create RDS, ElastiCache, MSK, and Beanstalk environment.
- Outputs will include service endpoints.

### 4. **Deploy to Elastic Beanstalk**
- Ensure `Dockerrun.aws.json` references your Docker image.
- Upload `Dockerrun.aws.json` to your Beanstalk environment (or let Terraform handle it if configured).

### 5. **Set Environment Variables**
Elastic Beanstalk will use the environment variables set in `main.tf` for DB, Redis, and Kafka connection strings.

### 6. **Access Your App**
- The Beanstalk URL will be shown in Terraform outputs.
- API docs: `http://<beanstalk-url>/docs`

---

## 📝 Notes

- **Security**: For production, restrict security groups, use secrets managers, and disable public access where possible.
- **Costs**: MSK and ElastiCache can be expensive—use small instances for testing.
- **Scaling**: You can scale Beanstalk, RDS, and MSK as needed.

---

## 📚 References

- [AWS Elastic Beanstalk Docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [RobinHook FastAPI Docs](http://<beanstalk-url>/docs)

---

**Happy deploying!**