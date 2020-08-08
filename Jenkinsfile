pipeline {
    agent any
    tools {
        docker 'latest'
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
                script {
                    def dockerImage = docker.build("antfarm:${env.BUILD_TAG}", "./ui")
                    dockerImage.inside {
                        sh 'yarn run build'
                        sh 'yarn jest'
                    }
                }
                echo 'Done building docker image'
            }
            post {
                always {
                    echo 'Finalize!'
                }
            }
        }
    }
}