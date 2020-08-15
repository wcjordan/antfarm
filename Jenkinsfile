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
                    request: file('ui/cloudbuild.yml'),
                    substitutions: [
                        _BUILD_TAG: "${env.BUILD_TAG}"
                    ]
                echo 'Done building docker image'
            }
        }
        stage('Test') {
            agent {
                kubernetes {
                    yaml """
spec:
  containers:
  - name: jenkins-antfarm-ui
    image: gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}
    command:
    - cat
    tty: true
"""
                }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                container('jenkins-antfarm-ui') {
                    sh 'yarn run build'
                    sh 'yarn jest'
                }
                // TODO delete jenkins-busybox.yml
                // script {
                //     def uiImage = docker.image("gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}")
                //     uiImage.inside {
                //         sh 'yarn run build'
                //         sh 'yarn jest'
                //     }
                // }
            }
        }
    }
}