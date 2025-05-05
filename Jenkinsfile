pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/maruwrks/sast-demo-app.git', branch: 'main'
            }
        }

        stage('Setup Virtual Environment') {
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
                    bandit -f xml -o bandit-output.xml -r . || true
                '''
            }
        }
    }

    post {
        always {
            recordIssues(
                tool: issues(name: 'Bandit', pattern: 'bandit-output.xml', reportEncoding: 'UTF-8')
            )
            archiveArtifacts artifacts: 'bandit-output.xml', fingerprint: true
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
