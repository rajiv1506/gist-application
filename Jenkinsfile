pipeline {
    agent any
    stages{
        stage('Checkout'){
            steps{
                git url: 'https://github.com/rajiv1506/gist-application.git', branch: 'main'
            }
        }
        stage('Test'){
            steps{
                script{
                    def tag = generateTag()
                    def tagversion = tagVersion()
                    echo "${tag}"
                    echo "${tagversion}"
                }
            }
        }
    }
}

def generateTag() {
    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true)
    return commitId
}

def tagVersion() {
    def tagversion = sh(script: 'git tag', returnStdout: true)
    return tagversion
}