pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Unit Test') {
            agent {
                kubernetes {
                    yamlFile 'jenkins-worker-nodejs.yml'
                }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
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
                googleCloudBuild \
                    credentialsId: 'flipperkid-default',
                    source: local('ui'),
                    request: file('ui/cloudbuild.yml'),
                    substitutions: [
                        _BUILD_TAG: "${env.BUILD_TAG}"
                    ]
            }
        }
        stage('System Test') {
            agent {
                kubernetes {
                    yaml """
spec:
  containers:
  - name: jenkins-antfarm-ui
    image: gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}
"""
                }
            }
            options {
                timeout(time: 3, unit: 'MINUTES')
            }
            steps {
                container('jenkins-antfarm-ui') {
                    sh 'curl http://127.0.0.1/static/index.html'
                }
            }
        }
    }
}