pipeline{
    agent any
    stages{ 
        stage('Build Django docker  and Push to hub'){
            steps{
                sh '''
                    docker-compose up
                '''
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