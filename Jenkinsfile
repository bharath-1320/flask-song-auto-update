pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/satya66655/flask-song-auto-update.git'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-user']) {
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@13.220.117.50 "cd flask-song-auto-update && ./deploy.sh"'
                }
            }
        }
    }
}

