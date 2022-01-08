pipeline {
    agent any
    stages {
        stage('Build') {
            
            steps {
                sh 'python main.py'
        
            }
        }
        stage('Test') { 
            
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
