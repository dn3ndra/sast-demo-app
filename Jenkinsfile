pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dn3ndra/sast-demo-app.git', branch: 'main'
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
                    bandit -f xml -o bandit-output.xml -r .
                '''
                archiveArtifacts artifacts: 'bandit-output.xml', fingerprint: true
                // Show the report in the Jenkins console to verify it works
                sh 'cat bandit-output.xml'
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
