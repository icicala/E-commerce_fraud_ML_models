pipeline {
    agent any // Runs on any available agent in the Jenkins environment
    stages {
        stage('Verify Docker Path') {
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }
    }
}