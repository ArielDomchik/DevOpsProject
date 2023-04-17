pipeline {
    agent any
    
    environment { DOCKER_USER = credentials('dockeruser') 
    DOCKER_PASS = credentials('dockerpassword')
    }

    stages {
        stage('build') {
            steps {
                sh 'echo ${DOCKER_PASS} |  docker login -u ${DOCKER_USER} --password-stdin'
                sh 'docker pull ${DOCKER_USER}/ariel:pythonapp'
                sh 'docker run -p 5000:5000 -d --name pythonapp ${DOCKER_USER}/ariel:pythonapp'
            }
        }
        
        stage('test') {
            steps {
                sh 'python3 check.py'
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
                sh 'kubectl apply -f deployment.yaml'
                sh "kubectl patch deployment pythonapp-deployment --type=json -p '[{\"op\": \"replace\", \"path\": \"/spec/template/spec/containers/0/image\", \"value\": \"arieldomchik/ariel:pythonapp3\"}]'"
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}