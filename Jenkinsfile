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
                    // Update the PATH variable within the pipeline
                    withEnv(["PATH=/usr/bin:$PATH"]) {
                        sh 'docker ps'
                    }
                }
            }
        }
    }
}
