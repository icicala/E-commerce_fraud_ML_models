pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
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

        stage('Build Docker Container') {
            steps {
                script {
                    sh 'docker build -t fastapi-app -f Dockerfile .'
                }
            }
        }
    }
}
