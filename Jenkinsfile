pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/Sharukg/time-tracker.git'
            }
        }
        stage('Build') {
            steps {
                // Commands for building the application
                echo 'Building the application...'
                sh 'mvn clean install'  // Assuming this is a Maven project
            }
        }
        stage('Test') {
            steps {
                // Commands for running tests
                echo 'Running tests...'
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Commands for deployment
                echo 'Deploying the application...'
                // You can add deployment steps here, for example:
                // sh 'bash deploy.sh'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
