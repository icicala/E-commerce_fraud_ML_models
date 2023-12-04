pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v /home/jenkins_home:/var/jenkins_home -v /var/jenkins_home/workspace/_commerce_fraud_ML_models_master:/app'
        }
    }

    stages {
        stage('Python and Pip') {
            steps {
                sh 'python --version' // Check Python version
                sh 'pip --version'    // Check Pip version
            }
        }
    }
}
