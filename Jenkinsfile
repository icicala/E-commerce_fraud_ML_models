pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }
    stages {
        stage('Feature Creation) {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt --user'
                    sh 'python3 feature_creation.py'
                }
            }
        }
    }
}
