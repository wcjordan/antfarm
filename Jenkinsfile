pipeline {
    agent none
    stages {
        stage('Build') {
            parallel {
                stage('UI') {
                    stages {
                        stage('Build UI') {
                            agent {
                                kubernetes {
                                    yamlFile 'jenkins-worker-dind.yml'
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
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
                        stage('Test UI') {
                            agent {
                                kubernetes {
                                    yamlFile 'jenkins-worker-ui.yml'
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
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
                    }
                }
                stage('Server') {
                    stages {
                        stage('Build Server') {
                            agent {
                                kubernetes {
                                    yamlFile 'jenkins-worker-dind.yml'
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
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
                        stage('Test Server') {
                            agent {
                                kubernetes {
                                    yamlFile 'jenkins-worker-python.yml'
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
                            }
                            steps {
                                container('jenkins-worker-python') {
                                    dir('server') {
                                        sh 'pip install --no-cache-dir -r requirements.txt'
                                        sh 'flake8 antfarm/training'
                                        sh 'pylint -j 0 --load-plugins pylint_django antfarm'
                                        // TODO (jordan) requires a running DB
                                        // sh 'python manage.py test antfarm.training'
                                    }
                                }
                            }
                        }
                    }
                }
                stage('Learning') {
                    stages {
                        stage('Build Learning') {
                            agent {
                                kubernetes {
                                    yamlFile 'jenkins-worker-dind.yml'
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
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
                        stage('Test Learning') {
                            agent {
                                kubernetes {
                                    yaml """
                                        spec:
                                          containers:
                                          - name: jenkins-worker-learning
                                            image: gcr.io/flipperkid-default/antfarm-learning:${env.BUILD_TAG}
                                            command:
                                            - cat
                                            tty: true
                                            resources:
                                              requests:
                                                cpu: "150m"
                                        """
                                }
                            }
                            options {
                                timeout(time: 10, unit: 'MINUTES')
                            }
                            steps {
                                container('jenkins-worker-learning') {
                                    dir('learning') {
                                        sh 'flake8 environments examples' // TODO (jordan) include "runners"
                                        sh 'pylint -j 0 --extension-pkg-whitelist=numpy environments' // TODO (jordan) include "runners"
                                        sh 'pytest --durations=0 runners'
                                    }
                                }
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
                          - name: jenkins-worker-antfarm
                            image: gcr.io/flipperkid-default/antfarm-ui:${env.BUILD_TAG}
                            resources:
                              requests:
                                cpu: "150m"
                        """
                }
            }
            options {
                timeout(time: 3, unit: 'MINUTES')
                skipDefaultCheckout()
            }
            steps {
                container('jenkins-worker-antfarm') {
                    sh 'curl http://127.0.0.1/static/index.html'
                }
            }
        }
    }
}