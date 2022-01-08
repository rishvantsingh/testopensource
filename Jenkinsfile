pipeline {
    agent none
    
    stages {
        stage('Build') {
            agent {
                label 'docker'
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python main.py'
        
            }
        }
        stage('Test') { 
            agent {
                label 'docker'
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml tests/test_hello_world.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}
