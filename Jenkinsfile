pipeline {
  agent any
  stages {
    stage('error') {
      environment {
        SQLALCHEMY_DATABASE_URL = 'sqlite:////tmp/dev.sqlite'
      }
      steps {
        sh 'sudo docker-compose up'
      }
    }
  }
}