pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root' // Define a single agent for the initial stages
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

        stage('ML Model Creation') {
            steps {
                script {
                    sh 'python3 ml_models.py'
                }
            }
        }

        stage('Build Docker Container') {
            agent {
                docker {
                    image 'docker:20.10'
                    args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }
    }
}
