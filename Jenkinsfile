pipeline {
  agent any
  stages {
    stage('error') {
      environment {
        SQLALCHEMY_DATABASE_URL = 'sqlite:////tmp/dev.sqlite'
      }
      steps {
        sh '''sudo docker ps | awk \'{print $1}\' | xargs sudo docker kill
sudo docker-compose up'''
      }
    }
  }
}