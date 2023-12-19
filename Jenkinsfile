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

        stage('ML Model Creation') {
            steps {
                script {
                    sh 'python3 ml_models.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or other tasks to execute irrespective of earlier stages' success/failure
        }
        success {
            // Build FastAPI Docker Image only on successful completion of earlier stages
            script {
                docker.image('docker:20.10').inside {
                    sh 'docker build -t fastapi-app -f Dockerfile .'
                }
            }
        }
    }
}
