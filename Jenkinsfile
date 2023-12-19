pipeline {
    agent none // Define no default agent

    stages {
        stage('Python Execution') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root'
                }
            }
            steps {
                script {
                    // Your Python script execution steps
                    sh 'python3 --version'

                }
            }
        }

        stage('Docker CLI Execution') {
            agent {
                docker {
                    image 'docker:20.10' // Or any other image with Docker installed
                    args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    // Your Docker CLI commands here
                    sh 'docker ps'
                }
            }
        }
    }
}
