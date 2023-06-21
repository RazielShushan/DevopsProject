pipeline{
    agent any
    stages{ 
        stage("Verify tooling"){
            steps{
                sh '''
                docker version
                docker info
                docker compose version
                '''
            }

        }
        stage("Prune Docker data"){
            steps{
                sh 'docker system prune -a --volumes -f'
            }
        }
        stage("start container"){
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