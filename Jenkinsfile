pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build Docker Container') {
            steps {
                script {
                    sh 'docker build -t fastapi-app -f Dockerfile .'
                }
            }
        }
    }
}
