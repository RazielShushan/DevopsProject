pipeline{
    agent any
    environment {
        debug = $DEBUG
        superuserUsername = "$JANGO_SUPERUSER_USERNAME"
        superuserPassword = "$DJANGO_SUPERUSER_PASSWORD"
        superuserEmail = "$DJANGO_SUPERUSER_EMAIL"
        secretKey = "$DJANGO_SECRET_KEY"
        mysqlReady = "$MYSQL_READY"
        mysqlDatabase = "$MYSQL_DATABASE"
        mysqlPassword = "$MYSQL_PASSWORD"
        mysqlUser = "$MYSQL_USER"
        mysqlHost = "$MYSQL_HOST"
        mysqlPort = "$MYSQL_PORT"
        mysqlRootPassword = "$MYSQL_ROOT_PASSWORD"
    }
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
                    def envFile = "web/.env"
                    def envContent = "DEBUG=${debug}\n" +
                                     "DJANGO_SUPERUSER_USERNAME=${superuserUsername}\n" +
                                     "DJANGO_SUPERUSER_PASSWORD=${superuserPassword}\n" +
                                     "DJANGO_SUPERUSER_EMAIL=${superuserEmail}\n" +
                                     "DJANGO_SECRET_KEY=${secretKey}\n" +
                                     "MYSQL_READY=${mysqlReady}\n" +
                                     "MYSQL_DATABASE=${mysqlDatabase}\n" +
                                     "MYSQL_PASSWORD=${mysqlPassword}\n" +
                                     "MYSQL_USER=${mysqlUser}\n" +
                                     "MYSQL_HOST=${mysqlHost}\n" +
                                     "MYSQL_PORT=${mysqlPort}\n" +
                                     "MYSQL_ROOT_PASSWORD=${mysqlRootPassword}\n"
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