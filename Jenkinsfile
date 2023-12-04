pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                //
                sh 'export PATH="/opt/anaconda3/condabin/:$PATH"'
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