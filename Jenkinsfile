pipeline {
    agent none
    stages {
        stage('Build') {
            stages {
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
        stage('Unit Tests') {
            stages {
                stage('Test UI') {
                    agent {
                        kubernetes {
                            yamlFile 'jenkins-worker-ui.yml'
                        }
                    }
                    options {
                        timeout(time: 3, unit: 'MINUTES')
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
                stage('Test Server') {
                    agent {
                        kubernetes {
                            yaml """
    spec:
      containers:
      - name: jenkins-worker-server
        image: gcr.io/flipperkid-default/antfarm-server:${env.BUILD_TAG}
        command:
        - cat
        tty: true
        env:
        - name: SECRET_KEY
          value: i76Qzd0s/A9Psn2hjqVRV15usy2iIvWXbLrQXNyXBRk=
    """
                        }
                    }
                    options {
                        timeout(time: 10, unit: 'MINUTES')
                        skipDefaultCheckout()
                    }
                    steps {
                        container('jenkins-worker-server') {
                            sh 'cd /usr/src/app; flake8 antfarm/training'
                            sh 'cd /usr/src/app; pylint -j 0 --load-plugins pylint_django antfarm'
                            sh 'cd /usr/src/app; python manage.py test antfarm.training'
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
    """
                        }
                    }
                    options {
                        timeout(time: 10, unit: 'MINUTES')
                        skipDefaultCheckout()
                    }
                    steps {
                        container('jenkins-worker-learning') {
                            sh 'cd /usr/src; flake8 environments runners examples'
                            sh 'cd /usr/src; pylint -j 0 --extension-pkg-whitelist=numpy environments runners'
                            sh 'cd /usr/src; pytest --durations=0 runners'                            
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