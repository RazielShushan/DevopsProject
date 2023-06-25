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
                    def envFile = "web/.env"
                    // Retrieve credentials
                    def debug = credentials('DEBUG')
                    def superuserUsername = credentials('DJANGO_SUPERUSER_USERNAME')
                    def superuserPassword = credentials('DJANGO_SUPERUSER_PASSWORD')
                    def superuserEmail = credentials('DJANGO_SUPERUSER_EMAIL')
                    def secretKey = credentials('DJANGO_SECRET_KEY')
                    def mysqlReady = credentials('MYSQL_READY')
                    def mysqlDatabase = credentials('MYSQL_DATABASE')
                    def mysqlPassword = credentials('MYSQL_PASSWORD')
                    def mysqlUser = credentials('MYSQL_USER')
                    def mysqlHost = credentials('MYSQL_HOST')
                    def mysqlPort = credentials('MYSQL_PORT')
                    def mysqlRootPassword = credentials('MYSQL_ROOT_PASSWORD')
                    
                    // Build the environment variables content
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