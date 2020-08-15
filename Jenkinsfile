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
        stage('Unit Test') {
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                agent {
                    kubernetes {
                        yamlFile 'jenkins-worker-nodejs.yml'
                    }
                }
                container('jenkins-worker-nodejs') {
                    dir('ui/js') {
                        sh 'yarn install --pure-lockfile'
                        sh 'yarn run build'
                        sh 'yarn jest'
                    }
                }
            }
        }
        stage('Build') {
            options {
                timeout(time: 5, unit: 'MINUTES')
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
    tty: true
"""
                }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                container('jenkins-antfarm-ui') {
                    sh 'curl http://127.0.0.1:8000/static/index.html'
                }
            }
        }
    }
}