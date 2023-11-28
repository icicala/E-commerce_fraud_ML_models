pipeline {
    agent any
    stages {
        stage('Feature Creation') {
            steps {
                bash '''
                #!/bin/bash
                source /home/icicala/PycharmProjects/eFraud_ML/venv/bin/activate
                python3 /home/icicala/PycharmProjects/eFraud_ML/main.py
                '''
            }
        }
        // Add more stages
    }
}