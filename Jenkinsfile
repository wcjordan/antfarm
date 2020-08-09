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
                    request: file('ui/cloudbuild.yaml')
                    // substitutions: [
                    //     _CUSTOM1: message,
                    //     _CUSTOM2: "Lorem ipsum, dolor sit amet."
                    // ]
                // script {
                //     def dockerImage = docker.build("antfarm:${env.BUILD_TAG}", "./ui")
                //     dockerImage.inside {
                //         sh 'yarn run build'
                //         sh 'yarn jest'
                //     }
                // }
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