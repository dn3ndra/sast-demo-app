pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dn3ndra/sast-demo-app.git', branch: 'main'
            }
        }
        stage('SAST Analysis') {
            steps {
                // Jalankan Bandit yang sudah terinstall di sistem
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                // Simpan hasil scan ke Jenkins (jika kamu sudah install plugin Warnings Next Generation)
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
