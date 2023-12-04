pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Run Python Script') {
            steps {
                script {

                    sh 'python main.py'
                }
            }
        }
    }
}
