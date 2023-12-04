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
                    sh 'sudo pip3 install -r requirements.txt --user'
                    sh 'sudo python3 main.py'
                }
            }
        }
    }
}
