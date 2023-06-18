pipline{
    agent any
    stages{ 
        stage('Setup Python Virtual ENV')
        {
            sh '''
            chmod +x envsetup.sh
            ./envstepup.sh
            '''
        }
        stage('Setup Gunicorn Setup'){
            sh '''
            chmod +x gunicorn.sh
            ./gunicorn.sh
            '''
        }
        stage('Setup NGINX'){
            '''
            sh +x nginx.sh
            ./nginx.sh
            '''
        }
    }
}