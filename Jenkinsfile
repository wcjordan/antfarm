pipeline {
    agent any
    stages {
        stage('Unit Test') {
            agent {
                kubernetes {
                    yamlFile 'jenkins-worker-ui.yml'
                }
            }
            options {
                timeout(time: 4, unit: 'MINUTES')
            }
            steps {
                container('jenkins-worker-ui') {
                    dir('ui/js') {
                        sh 'yarn install --pure-lockfile'
                        sh 'yarn jest'
                    }
                }
            }
        }
        stage('Build') {
            parallel {
                stage('Build UI') {
                    agent {
                        kubernetes {
                            yamlFile 'jenkins-worker-dind.yml'
                        }
                    }
                    options {
                        timeout(time: 4, unit: 'MINUTES')
                    }
                    steps {
                        container('dind') {
                            withDockerRegistry(credentialsId: 'gcr:flipperkid-default', url: 'https://gcr.io/flipperkid-default') {
                                sh "docker build -f ui/Dockerfile -t gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG} ui"
                                sh "docker push gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}"
                            }
                        }
                    }
                }
                stage('Build Server') {
                    agent {
                        kubernetes {
                            yamlFile 'jenkins-worker-dind.yml'
                        }
                    }
                    options {
                        timeout(time: 4, unit: 'MINUTES')
                    }
                    steps {
                        container('dind') {
                            withDockerRegistry(credentialsId: 'gcr:flipperkid-default', url: 'https://gcr.io/flipperkid-default') {
                                sh "docker build -f server/Dockerfile -t gcr.io/flipperkid-default/antfarm-server:${env.BUILD_TAG} server"
                                sh "docker push gcr.io/flipperkid-default/antfarm-server:${env.BUILD_TAG}"
                            }
                        }
                    }
                }
                stage('Build Learning') {
                    agent {
                        kubernetes {
                            yamlFile 'jenkins-worker-dind.yml'
                        }
                    }
                    options {
                        timeout(time: 4, unit: 'MINUTES')
                    }
                    steps {
                        container('dind') {
                            withDockerRegistry(credentialsId: 'gcr:flipperkid-default', url: 'https://gcr.io/flipperkid-default') {
                                sh "docker build -f learning/Dockerfile -t gcr.io/flipperkid-default/antfarm-learning:${env.BUILD_TAG} learning"
                                sh "docker push gcr.io/flipperkid-default/antfarm-learning:${env.BUILD_TAG}"
                            }
                        }
                    }
                }
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