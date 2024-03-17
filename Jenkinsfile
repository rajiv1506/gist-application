pipeline {
    agent any
    stages{
        stage('Checkout'){
            steps{
                git url: 'https://github.com/rajiv1506/gist-application.git', branch: 'main'
            }
        }
        stage("Build Tag"){
            steps{
                sh 'pwd'
            }
        }
        
    }
}

def generateTag() {
    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
    return "commit-${commitId}"
}