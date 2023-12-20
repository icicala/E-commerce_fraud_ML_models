pipeline {
    agent none

        stage('Build FastAPI Docker Image') {
            agent any
            steps {
                script {
                    sh 'docker run hello-world'
                }
            }
        }
    }
}
