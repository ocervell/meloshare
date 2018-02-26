pipeline {
  agent any
  stages {
    stage('init') {
      environment {
        SQLALCHEMY_DATABASE_URL = 'sqlite:////tmp/dev.sqlite'
      }
      steps {
        sh '''sudo docker ps | awk \'{print $1}\' | xargs sudo docker kill || true
sudo docker-compose up -d'''
      }
    }
    stage('cURL tests') {
      parallel {
        stage('cURL tests') {
          steps {
            sh 'curl localhost:5000/ && echo "Home OK !"'
          }
        }
        stage('py tests') {
          steps {
            sh 'echo "OK"'
          }
        }
      }
    }
  }
}