pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Python and Pip') {
            steps {
                sh 'python3 --version' // Check Python version
                sh 'pip3 --version'    // Check Pip version
            }
        }
    }
}
