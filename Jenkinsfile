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
                    bandit -f xml -o bandit-output.xml -r .
                '''
            }
        }

        stage('Archive Bandit Report') {
            steps {
                archiveArtifacts artifacts: 'bandit-output.xml', onlyIfSuccessful: true
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
