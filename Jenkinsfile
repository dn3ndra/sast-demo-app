pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/dn3ndra/sast-demo-app.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install bandit
                '''
            }
        }

        stage('SAST Analysis') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    bandit -r . -f xml -o bandit-output.xml || true
                '''
            }
        }

        stage('Publish Results') {
            steps {
                // Jika kamu ingin menampilkan hasil Bandit di Jenkins, gunakan plugin seperti Warnings NG
                // Contoh konfigurasi dengan Warnings NG plugin (opsional):
                recordIssues(tools: [bandit(pattern: 'bandit-output.xml')])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
