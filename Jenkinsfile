pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build Docker Container ps') {
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }
    }
}
