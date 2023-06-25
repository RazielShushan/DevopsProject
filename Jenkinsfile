pipeline{
    agent any
    environment {
        debug = credentials('DEBUG')
        superuserUsername = credentials('DJANGO_SUPERUSER_USERNAME')
        superuserPassword = credentials('DJANGO_SUPERUSER_PASSWORD')
        superuserEmail = credentials('DJANGO_SUPERUSER_EMAIL')
        secretKey = credentials('DJANGO_SECRET_KEY')
        mysqlReady = credentials('MYSQL_READY')
        mysqlDatabase = credentials('MYSQL_DATABASE')
        mysqlPassword = credentials('MYSQL_PASSWORD')
        mysqlUser = credentials('MYSQL_USER')
        mysqlHost = credentials('MYSQL_HOST')
        mysqlPort = credentials('MYSQL_PORT')
        mysqlRootPassword = credentials('MYSQL_ROOT_PASSWORD')
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