pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Verify Docker Path') {
            steps {
                script {
                    sh '/usr/bin/docker ps'
                }
            }
        }
    }
}
