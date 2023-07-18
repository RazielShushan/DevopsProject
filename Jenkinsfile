pipeline{
    agent any
    environment {
        debug = "$DEBUG"
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
        stage("Build images on dcoker-hub"){
            steps{
                    sh '''
                    cd .\web\ 
                    docker build --tag python-django .
                    cd ..\proxy\
                    docker build --tag django-proxy .
                    '''
            }
        }
        stage("Push images to minikube container"){
            steps{
                    sh '''
                    minikube image load django-proxy:latest
                    minikube image load python-django:latest
                    '''
            }
        }
        stage("Deploy k8s pods"){
            steps{
                    sh '''
                    kubectl apply -k deploy/
                    '''
            }
        }
    }
}