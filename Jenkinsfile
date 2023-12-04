pipeline {
    agent any
    stages {
        stage('Set Anaconda Path') {
            steps {
                script {
                    // Add Anaconda path to PATH for all subsequent steps
                    withEnv(["PATH=/opt/anaconda3/condabin/:$PATH"]) {
                    }
                }
            }
        }
        stage('Install dependencies') {
            steps {
                // Activate conda environment and install dependencies
                sh 'conda activate mlenv && conda install --file requirements.txt'
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
