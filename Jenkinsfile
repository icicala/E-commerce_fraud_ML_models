pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }
    stages {
        stage('Install ML Libraries') {
        steps {
            script {
                sh 'pip3 install -r requirements.txt --user'
            }
        }
    }
        stage('Feature Creation') {
            steps {
                script {
                    sh 'python3 feature_creation.py'
                }
            }
        }

        stage('ML Model creation') {
            steps {
                script {
                    sh 'python3 ml_models.py'
                }
            }
        }

        stage('Build FastAPI Docker Image') {
            agent {
                docker {
                    image 'docker:20.10' // Use Docker CLI image for building Docker images
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