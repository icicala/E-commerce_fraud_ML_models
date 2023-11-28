pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Feature Creation') {
            steps {
                script {
                    sh 'python3 main.py'
                }
            }
        }
    }
}