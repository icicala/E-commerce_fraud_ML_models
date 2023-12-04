pipeline {
    agent any
    stages {
        stage('Activate Environment and Install Dependencies') {
            steps {
                // Activate conda environment and install dependencies
                sh '''
                    source /opt/anaconda3/bin/activate mlenv
                    conda install --file requirements.txt
                '''
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
