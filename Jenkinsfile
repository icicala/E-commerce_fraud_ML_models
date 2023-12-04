pipeline {
    agent {
        docker {
            image 'python:3.11'
            // Mount a volume
            args '-v /home/icicala/PycharmProjects/output:/app/output'
        }
    }
    stages {
        stage('Setup') {
            steps {
                // Install pip
                sh 'apt-get install -y python3-pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Run pip to install dependencies from requirements.txt
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Python Scripts') {
            steps {
                // Run Python scripts within the Docker container
                sh 'python main.py'
            }
        }

        stage('Save Output') {
            steps {
                // Copy output files to a mounted volume accessible from the host
                sh 'cp -r . /app/output'
            }
        }
    }
}
