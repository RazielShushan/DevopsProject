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
                 script {
                    // Set environment variables 
                    env.IMAGE_TAG = "latest"
                    env.DEBUG = credentials('DEBUG')
                    env.DJANGO_SUPERUSER_USERNAME = credentials('DJANGO_SUPERUSER_USERNAME')
                    env.DJANGO_SUPERUSER_PASSWORD = credentials('DJANGO_SUPERUSER_PASSWORD')
                    env.DJANGO_SUPERUSER_EMAIL = credentials('DJANGO_SUPERUSER_EMAIL')
                    env.DJANGO_SECRET_KEY = credentials('DJANGO_SECRET_KEY')
                    env.MYSQL_READY = credentials('MYSQL_READY')
                    env.MYSQL_DATABASE = credentials('MYSQL_DATABASE')
                    env.MYSQL_PASSWORD = credentials('MYSQL_PASSWORD')
                    env.MYSQL_USER = credentials('MYSQL_USER')
                    env.MYSQL_HOST = credentials('MYSQL_HOST')
                    env.MYSQL_PORT = credentials('MYSQL_PORT')
                    env.MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
                    print(DJANGO_SUPERUSER_USERNAME)

                    // Build and push images
                    sh '''
                    docker-compose up -d --no-color --build
                    docker-compose push
                    '''
                }
            }
        }
    }
}