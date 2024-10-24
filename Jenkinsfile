pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: '154-DevOps', url: 'https://github.com/Sharukg/time-tracker.git'
            }
        }
        stage('Build') {
            steps {
                // Commands for building your project, e.g.:
                sh './gradlew build'
            }
        }
        stage('Test') {
            steps {
                // Commands for running tests, e.g.:
                sh './gradlew test'
            }
        }
        stage('Deploy') {
            steps {
                // Commands for deployment (if any)
                echo 'Deploying...'
            }
        }
    }
}
