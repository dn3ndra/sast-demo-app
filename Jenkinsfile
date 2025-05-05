pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/maruwrks/sast-demo-app.git', branch: 'master'
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
                recordIssues(
                    tool: issues(name: 'Bandit', pattern: 'bandit-output.xml', reportEncoding: 'UTF-8')
                )
                archiveArtifacts artifacts: 'bandit-output.xml', fingerprint: true
            }
        }

        stage('Display SAST Issues') {
            steps {
                script {
                    def output = sh(
                        script: '''
                            python3 -c "
import xml.etree.ElementTree as ET

tree = ET.parse('bandit-output.xml')
root = tree.getroot()

for issue in root.findall('.//Issue'):
    severity = issue.get('severity')
    confidence = issue.get('confidence')
    text = issue.find('description').text if issue.find('description') is not None else 'No description'
    fname = issue.find('file').text if issue.find('file') is not None else 'unknown file'
    lineno = issue.find('line_number').text if issue.find('line_number') is not None else 'unknown line'
    print(f'[{severity}] {text} (File: {fname}, Line: {lineno}, Confidence: {confidence})')
" || true
                        ''',
                        returnStdout: true
                    ).trim()
                    echo output
                }
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
