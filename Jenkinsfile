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
                    sh 'echo $PATH' // Print the current PATH variable
                    sh 'which docker' // Check the location of the 'docker' executable
                }
            }
        }
    }
}
