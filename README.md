# DevOps Project

This project provides an automated deployment pipeline using Jenkins, Docker, and Kubernetes.

## Prerequisites

- AWS CLI configured with appropriate access credentials.
- Jenkins with the necessary plugins installed.
- Docker registry credentials configured in Jenkins.
- Terraform installed on the local machine.
- Python 3.x installed on the local machine.

## Getting Started

Follow the steps below to set up the project:

1. Clone the repository
   `git clone https://github.com/ArielDomchik/DevOpsProject.git`

2. Provision the VPC and cluster infrastructure using Terraform:

 -   `cd terraform-configuration`
 -   `terraform init`
 -   `before applying, change the backend in terraform.tf "name = <change_here>"`

## Note: Make sure to attach the AmazonEBSCSIPolicy manually in the AWS Management Console.

- This gets done by `kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.16"`
- Alternatively, this command is inside the Jenkinsfile as a step in the pipeline


3. Update the kubeconfig context to use the provisioned cluster API server:
  `aws eks --region <region> update-kubeconfig --name <cluster-name>`

4. Label the node in availability zone us-east-1a with "vol=pers":
  `kubectl label node <node> vol=pers`

5. On the ELK instance, run the following command to adjust the system settings:
  ` sudo sysctl -w vm.max_map_count=262144 `

6. Set up the Jenkins pipeline:

   - Create a new Jenkins pipeline job.
   - Configure the pipeline to use the provided Jenkinsfile.
   - Set the Docker registry credentials as environment variables in Jenkins:
    -    `DOCKER_USER (Docker registry username)`
    -    `DOCKER_PASS (Docker registry password)`

Run the Jenkins pipeline to build, test, and deploy the application.

## Cleanup

 - use `terraform destroy` in terraform-configuration directory


## Additional steps

- terraform apply to provision vpc and cluster
- Dont forget to manually attach AmazonEBSCSIPolicy! (need to find a way to provision this with terraform)
- update-kubeconfig context to use provisioned cluster api server
- label node in az us-east-1a "vol=pers" (kubectl label node <node> vol=pers)
- run `sudo sysctl -w vm.max_map_count=262144` on elk instance
- run pipeline 

Need to do :
- Make the application as a helm bundle

