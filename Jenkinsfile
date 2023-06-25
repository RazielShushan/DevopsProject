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
        stage("Create .env file"){
            steps{
                 script {
                    // Set environment variables
                    def envFile = ".env"
                    def envContent = "DEBUG=${credentials('DEBUG')}\n" +
                                     "DJANGO_SUPERUSER_USERNAME=${credentials('DJANGO_SUPERUSER_USERNAME')}\n" +
                                     "DJANGO_SUPERUSER_PASSWORD=${credentials('DJANGO_SUPERUSER_PASSWORD')}\n" +
                                     "DJANGO_SUPERUSER_EMAIL=${credentials('DJANGO_SUPERUSER_EMAIL')}\n" +
                                     "DJANGO_SECRET_KEY=${credentials('DJANGO_SECRET_KEY')}\n" +
                                     "MYSQL_READY=${credentials('MYSQL_READY')}\n" +
                                     "MYSQL_DATABASE=${credentials('MYSQL_DATABASE')}\n" +
                                     "MYSQL_PASSWORD=${credentials('MYSQL_PASSWORD')}\n" +
                                     "MYSQL_USER=${credentials('MYSQL_USER')}\n" +
                                     "MYSQL_HOST=${credentials('MYSQL_HOST')}\n" +
                                     "MYSQL_PORT=${credentials('MYSQL_PORT')}\n" +
                                     "MYSQL_ROOT_PASSWORD=${credentials('MYSQL_ROOT_PASSWORD')}\n"
                    
                    // Write the environment variables to .env file
                    sh "echo '''${envContent}''' > ${envFile}"
                }
            }
        }
        stage("Build images and push to docker-hub"){
            steps{
                    sh '''
                    docker-compose up -d --no-color --build
                    docker-compose push
                    '''
            }
        }
    }
}