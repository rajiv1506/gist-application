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
                dir('./gist-application-deployment') {
                    script {
                        generateTag()
                    }
                }

            }
        }
        
    }
}

def generateTag() {
    def commitId = bat(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
    return commitId
}