pipeline{
    agent any
    stages{ 
        stage("Verify tooling"){
            steps{
                sh '''
                docker version
                docker info
                docker compose version
                kubectl version --client
                '''
            }

        }
        stage("Prune Docker data"){
            steps{
                sh 'docker system prune -a --volumes -f'
            }
        }
        stage("Buils images and push to docker-hub"){
            steps{
                sh 'docker compose up -d --no-color --wait'
            }
        }
        /** stage('Setup Python Virtual ENV'){
            steps {
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''}
            }   
        stage('Setup Gunicorn Setup'){
            steps{
            sh '''
            chmod +x gunicorn.sh
            ./gunicorn.sh
            '''
            }
        }
        stage('Setup NGINX'){
            steps{
            sh '''
            sh +x nginx.sh
            ./nginx.sh
            '''
            }
        } **/
    }
}