pipeline{
  agent any

  stages{
    stage("Clean un"){
      steps{
        deleteDir()
      }
    }
    stage("Clone repo"){
      steps{
        sh "git clone https://github.com/MohamedAmineDev/scrapping_times_jobs.git "
      }
    }
    stage("Generate python application image"){
      steps{
        dir("scrapping_times_jobs"){
          sh "docker build -t scrapper2 ."
        }
      }
    }
    stage("Run docker compose"){
      steps{
        dir("scrapping_times_jobs"){
          sh "docker compose up -d"
        }
      }
    }
  }
}