pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }

    stages {
        stage('Run Python Script') {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt --user'
                    sh 'python3 main.py'
                }
            }
        }
    }
}
