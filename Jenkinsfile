pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sou-008/flask-express-cicd.git'  // Your repository URL
            }
        }
        stage('Install Dependencies for Express') {
            steps {
                sh 'cd express-frontend && npm install'  // Install dependencies for Express app
            }
        }
        stage('Install Dependencies for Flask') {
            steps {
                sh 'cd flask-backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'  // Install Flask dependencies
            }
        }
        stage('Restart Express') {
            steps {
                sh 'pm2 restart express-frontend'  // Restart Express app using pm2
            }
        }
        stage('Restart Flask') {
            steps {
                sh 'pm2 restart flask-backend'  // Restart Flask app using pm2
            }
        }
    }
}