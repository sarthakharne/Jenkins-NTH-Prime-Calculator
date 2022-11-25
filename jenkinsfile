pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/MnCSSJ4x/Jenkins-Calculator.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Calculator.py"
                sh "python3 Calculator.py"
            }
        }
        stage('Test Set 1 (supposed to pass) ') {
            steps {
                sh "chmod u+x unit_tests1.py"
                sh "./unit_tests1.py"
            }
        }
        stage('Test Set 2 (supposed to fail)') {
            steps {
                sh "chmod u+x unit_tests2.py"
                sh "./unit_tests2.py"
            }
        }
    } 
}
