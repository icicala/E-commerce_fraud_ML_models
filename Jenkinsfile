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
}
