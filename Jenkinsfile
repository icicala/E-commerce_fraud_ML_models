pipeline {
    agent any
    stages {
        stage('Feature Creation') {
            steps {
                sh 'source PycharmProjects/eFraud_ML/venv/bin/activate && python3 PycharmProjects/eFraud_ML/main.py' > /home/icicala/Desktop/Data_Ecom_Fraud/EFraud_data.csv
            }
        }
        // Add more stages if needed
    }
}