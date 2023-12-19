pipeline {
    agent none

    stages {
        stage('Install ML Libraries') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root'
                }
            }
            steps {
                script {
                    sh 'pip3 install -r requirements.txt --user'
                    sh 'python3 feature_creation.py'
                    sh 'python3 ml_models.py'
                }
            }
        }
        stage('Build FastAPI Docker Image') {
            agent {
                docker {
                    image 'docker:20.10'
                    args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    sh 'docker build -t fastapi-app -f Dockerfile .'
                }
            }
        }
    }
}
