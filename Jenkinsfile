pipeline {
    agent any
    stages {
        stage('Set Anaconda Path') {
            steps {
                script {
                    // Add Anaconda path to PATH
                    sh 'export PATH="/opt/anaconda3/condabin/:$PATH"'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                // activate conda enviroment
                sh 'conda activate mlenv'
                // install dependencies from requirements file
                sh 'conda install --file requirements.txt'
            }
        }
        stage('Feature Creation') {
            steps {
                script {
                    sh 'python3 main.py'
                }
            }
        }
    }
}