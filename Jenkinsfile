pipeline {
    agent {
        label 'docker'
    }
    
    stages {
        stage('Build') {
            
                docker {
                    image 'python:2-alpine'
                }
            
            steps {
                sh 'python main.py'
        
            }
        }
        stage('Test') { 
         
                docker {
                    image 'qnib/pytest' 
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
