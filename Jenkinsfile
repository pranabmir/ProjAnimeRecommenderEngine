// pipeline {
//     agent any

//     environment {
//         VENV_DIR = 'venv'
//         // GCP_PROJECT = 'mlops-new-447207'
//         // GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
//         // KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
//     }

//     stages{

//         stage("Cloning from Github...."){
//             steps{
//                 script{
//                     echo 'Cloning from Github...'
//                     checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token2', url: 'https://github.com/pranabmir/ProjAnimeRecommenderEngine.git']])
//                 }
//             }
//         }

//         stage("Making a virtual environment...."){
//             steps{
//                 script{
//                     echo 'Making a virtual environment...'
//                     sh '''
//                     python -m venv ${VENV_DIR}
//                     . ${VENV_DIR}/bin/activate
//                     pip install --upgrade pip
//                     pip install -e .
//                     pip install  dvc
//                     '''
//                 }
//             }
//         }


//         stage('DVC Pull'){
//             steps{
//                 withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
//                     script{
//                         echo 'DVC Pul....'
//                         sh '''
//                         . ${VENV_DIR}/bin/activate
//                         dvc pull
//                         '''
//                     }
//                 }
//             }
//         }


        // stage('Build and Push Image to GCR'){
        //     steps{
        //         withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
        //             script{
        //                 echo 'Build and Push Image to GCR'
        //                 sh '''
        //                 export PATH=$PATH:${GCLOUD_PATH}
        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
        //                 gcloud config set project ${GCP_PROJECT}
        //                 gcloud auth configure-docker --quiet
        //                 docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
        //                 docker push gcr.io/${GCP_PROJECT}/ml-project:latest
        //                 '''
        //             }
        //         }
        //     }
        // }


        // stage('Deploying to Kubernetes'){
        //     steps{
        //         withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
        //             script{
        //                 echo 'Deploying to Kubernetes'
        //                 sh '''
        //                 export PATH=$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
        //                 gcloud config set project ${GCP_PROJECT}
        //                 gcloud container clusters get-credentials ml-app-cluster --region us-central1
        //                 kubectl apply -f deployment.yaml
        //                 '''
        //             }
        //         }
        //     }
        // }
//     }
// }

pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        // GCP_PROJECT = 'mlops-new-447207'   // uncomment when using GCP stages
    }

    stages {

        stage("Clone from GitHub") {
            steps {
                script {
                    echo 'Cloning repository...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: '.']],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token2',
                            url: 'https://github.com/pranabmir/ProjAnimeRecommenderEngine.git'
                        ]]
                    )
                }
            }
        }

        stage("Setup Virtual Environment") {
            steps {
                script {
                    echo 'Setting up virtual environment...'
                    sh """
                        python -m venv ${VENV_DIR}
                        ${VENV_DIR}/bin/pip install --upgrade pip
                        ${VENV_DIR}/bin/pip install -e .
                        ${VENV_DIR}/bin/pip install dvc
                    """
                }
            }
        }

        stage("DVC Pull") {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_KEY_FILE')]) {
                    script {
                        echo 'Running DVC pull...'
                        sh """
                            export GOOGLE_APPLICATION_CREDENTIALS=$GCP_KEY_FILE
                            echo "Using credentials at: \$GOOGLE_APPLICATION_CREDENTIALS"
                            ls -la .
                            ${VENV_DIR}/bin/dvc pull -v
                        """
                    }
                }
            }
        }


        // stage("Build and Push Image to GCR") {
        //     steps {
        //         withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script {
        //                 echo 'Building and pushing Docker image...'
        //                 sh """
        //                     gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
        //                     gcloud config set project ${GCP_PROJECT}
        //                     gcloud auth configure-docker --quiet
        //                     docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
        //                     docker push gcr.io/${GCP_PROJECT}/ml-project:latest
        //                 """
        //             }
        //         }
        //     }
        // }

        // stage("Deploy to Kubernetes") {
        //     steps {
        //         withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script {
        //                 echo 'Deploying to Kubernetes...'
        //                 sh """
        //                     gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
        //                     gcloud config set project ${GCP_PROJECT}
        //                     gcloud container clusters get-credentials ml-app-cluster --region us-central1
        //                     kubectl apply -f deployment.yaml
        //                 """
        //             }
        //         }
        //     }
        // }
    }
}
