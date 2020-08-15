pipeline {
    agent any
    tools {
        dockerTool 'latest'
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            options {
                timeout(time: 20, unit: 'MINUTES')
            }
            steps {
                echo 'Starting to build docker image'
                googleCloudBuild \
                    credentialsId: 'flipperkid-default',
                    source: local('ui'),
                    request: file('ui/cloudbuild.yaml'),
                    substitutions: [
                        _BUILD_TAG: ${env.BUILD_TAG}
                    ]
            }
            echo 'Done building docker image'
        }
        stage('Test') {
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            script {
                def uiImage = docker.image("gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}")
                uiImage.inside {
                    sh 'yarn run build'
                    sh 'yarn jest'
                }
            }
        }
    }
}