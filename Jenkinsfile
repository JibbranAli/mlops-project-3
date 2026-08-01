pipeline {
	agent any
	stages {
		stage ('checkout'){
			steps{
				checkout scm
			}
		}
		
		stage('Build Docker Image'){
			steps{
				sh 'sudo docker build -t student-api:latest .'
			}
		}
		stage ('Stop Old container'){
			steps {
				sh '''sudo docker stop student-api || true
					  sudo docker rm student-api || true 
					'''
				}	
		}
		
		stage ('Run NEw Container'){
			steps{
				sh '''
				sudo docker run -d \
				--name student-api \
				-p 8000:8000 \
				student-api:latest			
				'''
			}
		}	
	}
}