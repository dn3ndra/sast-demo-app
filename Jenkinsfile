pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/dn3ndra/sast-demo-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install bandit
                '''
            }
        }

        stage('SAST Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    bandit -f xml -o bandit-output.xml -r .
                '''
            }
        }

        stage('Archive Bandit Report') {
            steps {
                archiveArtifacts artifacts: 'bandit-output.xml', allowEmptyArchive: true
            }
        }
    }
}
