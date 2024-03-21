pipeline {
    agent any
    environment{ TAG = generateTag() }
    stages{
        stage('Checkout'){
            steps{
                git url: 'https://github.com/rajiv1506/gist-application.git', branch: 'main'
            }
        }
        stage("Build Tag and Image"){
            steps{
                dir('./gist-application-deployment') {
                    script {
                        powershell "docker build -t gist-application:${env.Tag} ."
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