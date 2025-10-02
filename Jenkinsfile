pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'mlops-new-447207'
        GCLOUD_PATH = "C:\\Program Files (x86)\\Google\\Cloud SDK\\google-cloud-sdk\\bin"
        KUBECTL_AUTH_PLUGIN = "C:\\Program Files (x86)\\Google\\Cloud SDK\\google-cloud-sdk\\bin"
    }

    stages {

        stage("Cloning from Github") {
            steps {
                script {
                    echo 'Cloning from Github...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token2',
                            url: 'https://github.com/pranabmir/ProjAnimeRecommenderEngine.git'
                        ]]
                    )
                }
            }
        }

        stage("Setting up Virtual Environment") {
            steps {
                script {
                    echo 'Creating virtual environment and installing dependencies...'
                    bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install "dvc[gcs]"
                    """
                }
            }
        }

        stage("DVC Pull") {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Pulling data with DVC...'
                        bat """
                        call %VENV_DIR%\\Scripts\\activate
                        set GOOGLE_APPLICATION_CREDENTIALS=%GOOGLE_APPLICATION_CREDENTIALS%
                        dvc pull
                        """
                    }
                }
            }
        }

        // stage("Build and Push Docker Image to GCR") {
        //     steps {
        //         withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script {
        //                 echo 'Building and pushing Docker image to GCR...'
        //                 bat """
        //                 set PATH=%PATH%;${GCLOUD_PATH}
        //                 gcloud auth activate-service-account --key-file=%GOOGLE_APPLICATION_CREDENTIALS%
        //                 gcloud config set project ${GCP_PROJECT}
        //                 gcloud auth configure-docker --quiet
        //                 docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
        //                 docker push gcr.io/${GCP_PROJECT}/ml-project:latest
        //                 """
        //             }
        //         }
        //     }
        // }

        // stage("Deploying to Kubernetes") {
        //     steps {
        //         withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script {
        //                 echo 'Deploying to Kubernetes...'
        //                 bat """
        //                 set PATH=%PATH%;${GCLOUD_PATH};${KUBECTL_AUTH_PLUGIN}
        //                 gcloud auth activate-service-account --key-file=%GOOGLE_APPLICATION_CREDENTIALS%
        //                 gcloud config set project ${GCP_PROJECT}
        //                 gcloud container clusters get-credentials ml-app-cluster --region us-central1
        //                 kubectl apply -f deployment.yaml
        //                 """
        //             }
        //         }
        //     }
        // }
    }
}
