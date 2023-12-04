pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                // Activate conda environment and install dependencies
                sh '/opt/anaconda3/bin/conda activate mlenv && /opt/anaconda3/bin/conda install --file requirements.txt'
            }
        }
        stage('Feature Creation') {
            steps {
                // Run Python script
                sh 'python3 main.py'
            }
        }
    }
}
