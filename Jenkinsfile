pipeline {
    agent any

    parameters {
        string(name: 'EC2_PRIVATE_IP', defaultValue: '', description: 'Private IP of the EC2 instance')
    }

    stages {
        stage('Checkout App Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/bharath-1320/flask-song-auto-update.git'
            }
        }

        stage('Deploy Updated App') {
            steps {
                sshagent(['ec2-prod-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@${params.EC2_PRIVATE_IP} '
                        if [ ! -d flask-song-auto-update ]; then
                            git clone https://github.com/bharath-1320/flask-song-auto-update.git
                        fi
                        cd flask-song-auto-update
                        git pull origin main
                        chmod +x deploy.sh
                        ./deploy.sh
                    '
                    """
                }
            }
        }
    }
}

