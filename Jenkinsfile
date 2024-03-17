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
                        def tag = "${generateTag()}"
                        env.tag = tag
                    }
                }
            }
        }
        stage("Build Docker Image") {
            steps  {
                dir('./gist-application-deployment') {
                    script {
                        bat "docker build -t gist-application:${env.tag} ."
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