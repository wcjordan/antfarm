node {
    checkout scm

    def dockerImage = docker.build("antfarm:${env.BUILD_TAG}", "./ui")
    dockerImage.inside {
        sh 'yarn run build'
        sh 'yarn jest'
    }
}