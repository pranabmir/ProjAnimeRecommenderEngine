pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'mlops-new-447207'
        GCLOUD_PATH = "/usr/lib/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
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
                    sh """
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
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
                        sh """
                        . ${VENV_DIR}/bin/activate
                        export GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}
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
        //                 sh """
        //                 export PATH=\$PATH:${GCLOUD_PATH}
        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
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
        //                 sh """
        //                 export PATH=\$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
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
