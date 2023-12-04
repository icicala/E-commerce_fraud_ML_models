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
                    sh 'pip install -r requirements.txt'
                    sh 'python3 main.py'
                }
            }
        }
    }
}
