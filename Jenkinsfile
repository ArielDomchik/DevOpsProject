pipeline {
    agent any
    
    environment { DOCKER_USER = credentials('dockeruser') 
    DOCKER_PASS = credentials('dockerpassword')
    }

    stages {
        stage('build') {
            steps {
                sh 'echo ${DOCKER_PASS} |  docker login -u ${DOCKER_USER} --password-stdin'
                sh 'docker pull ${DOCKER_USER}/ariel:pythonapp-v2'
                sh 'docker run -p 5000:5000 -d --name pythonapp ${DOCKER_USER}/ariel:pythonapp-v2'
            }
        }
        
        stage('test') {
            steps {
                sh 'python3 check.py'
            }
        }

        stage('Push to dockerhub') {
            steps {
                sh 'docker tag arieldomchik/ariel:pythonapp-v2 arieldomchik/ariel:pythonapp'
                sh 'docker push arieldomchik/ariel:pythonapp'
             }
        }

        stage('Clean Dockerized application') {
            steps {
                sh 'docker stop pythonapp'
                sh 'docker rm pythonapp'
                sh 'docker logout'
            }
        }
        
        stage('Deploy to EKS') {
            steps {
                dir('/home/ubuntu/workspace/final/k8s-configuration') {
                sh 'kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.16"'
                sh 'kubectl apply -f pv.yaml'
                sh 'kubectl apply -f storageclass.yaml'
                sh 'kubectl apply -f pvc.yaml'
                sh 'kubectl apply -f configmap.yaml'
                sh 'kubectl apply -f deployment.yaml'
                sh "kubectl patch deployment pythonapp-deployment --type=json -p '[{\"op\": \"replace\", \"path\": \"/spec/template/spec/containers/0/image\", \"value\": \"arieldomchik/ariel:pythonapp\"}]'"
                sh 'kubectl apply -f service.yaml'
               }
            }
        }
    }
}
