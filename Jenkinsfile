pipeline {
    agent any

    environment {
        APP_NAME = 'my-flask-app'
        IMAGE_NAME = 'my-flask-app:latest'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git'
            }
        }

        stage('Set Up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && python -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5001:5001 --name flask-container $IMAGE_NAME'
            }
        }

        stage('Post Build Cleanup') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                sh 'docker rmi $IMAGE_NAME || true'
            }
        }
    }

    post {
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build failed. Check logs for details.'
        }
    }
}
