## CICD - Build Docker image and push it to Github Container Registry

1. Create a new workflow from the Actions menu of the repository. 
    In this case, the workflow name is docker-image-build-push-example.yml created in .github/workflows folder

    This workflow gets triggered whenever there is a code checkin happens in cicd folder in the main branch.

2. Create two github secrets

    <p>GHCR_PASSWORD - Use this secret to publish the docker images to the github docker container registry. The personal access token associated with this secret has read, write and delete packages permissions.
    <p>GHCR_PULL_PASSWORD - Use this secret in APIs, airflow to pull images from the container registry. The personal access token associated with this secret has read packages permissions.

3.  Create a kubernetes secret that connects to github docker container registry to pull the images

    Note: Make sure you create the secret in spark-apps namespace
    The following instructions provide steps to create the secret from command line using kubectl
    
    a. Set the context to spark-apps namespace
        kubectl config set-context --current --namespace=spark-apps

    b. Create the secret
        kubectl create secret docker-registry {give a name such as github-pull-image-secret} --docker-server=https://ghcr.io --docker-username={github username} --docker-password={personal access token that has got packages read permission} --docker-email={email of the github user}

4. Use the kubernetes secret in the config overrides section

    config_overrides={
        "type": "Python",
        "sparkVersion": "3.2.0",
        "imagePullSecrets": ["github-pull-image-secret"],
        "image": "ghcr.io/{path to image}",
        ......
        }


## CICD - Build Docker image and push it to Azure Container Registry

1. Create an Azure DevOps pipeline 

    This pipeline gets triggered whenever there is a code checkin happens in cicd folder in the main branch.
    The pipeline builds and pushes the docker image to Azure Container Registry

2. Create a service principal
    Assign AcrPull role to this service principal 
    
3.  Create a kubernetes secret that connects to Azure container registry to pull the images

    Note: Make sure you create the secret in spark-apps namespace
    The following instructions provide steps to create the secret from command line using kubectl
    
    a. Set the context to spark-apps namespace
        kubectl config set-context --current --namespace=spark-apps

    b. Create the secret
        kubectl create secret docker-registry {give a name such as acr-pull-image-secret} --docker-server={Your ACR Login server name which looks like oceansparkdemo.azurecr.io} --docker-username={service principal client ID} --docker-password={service principal secret}

4. Use the kubernetes secret in the config overrides section

    config_overrides={
        "type": "Python",
        "sparkVersion": "3.2.0",
        "imagePullSecrets": ["acr-pull-image-secret"],
        "image": "ghcr.io/{path to image}",
        ......
        } 

 5. Submitting a spark job from Azure Data Factory

    a. Use Web Activity in an Azure Data Factory pipeline
    b. Set the URL as https://api.spotinst.io/ocean/spark/cluster/{your ocean spark cluster id}/app?accountId={your spot account ID}   
    c. Method as POST
    d. Add the following two headers: 
            Name                Value
            Content-Type        application/json
            Authorization       Bearer {your spot token}
    e. Add the following in the body
        {
            "jobId": "spark-acr-adf",
                    "configOverrides": {
                    "type": "Python",
                    "sparkVersion": "3.2.0",
                    "imagePullSecrets": ["acr-pull-image-secret"],
                    "image": "{your acr name}.azurecr.io/{your image name}", 
                    "mainApplicationFile": "local:///opt/application/main.py",
                    "executor": {
                        "cores": 2,
                        "instances": 1
                    }
                }
            }



