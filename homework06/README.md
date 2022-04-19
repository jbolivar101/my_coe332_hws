# KUBERNEATES
## Overview
Through kubernetes we are able to attach different server like applications such as redis and flask apis in order to keep data and work up to date. This can also be used in other circumstances that would require multiple people to access a single script from different positions and different jobs.
## Scripts
The scripts we are using are the past app.py and dockerfile as well as new yml files that set up the deployments, services, and pvc for the redis and api flask. It requires connecting them through naming and different port numbers/IP addresses.
## Instructions
### 1)
In order to run the redis and flask yml files we must apply them within kubernetes with the following commands:
```BASH
kubectl jbolivar-test-redis-deployment.yml
kubectl jbolivar-test-redis-service.yml
kubectl jbolivar-test-redis-pvc.yml

kubectl apply -f jbolivar-test-api-deployment.yml
kubectl apply -f jbolivar-test-api-service.yml

kubectl get all
```

With and expected output of:
```BASH
NAME                                                       READY   STATUS             RESTARTS       AGE
pod/hw06-jbolivar-test-redis-deployment-6dd57664b9-xnklp   1/1     Running            0              28m
pod/hw06-test-flask-85d486665-9xkdb                        0/1     CrashLoopBackOff   10 (81s ago)   28m
pod/hw06-test-flask-85d486665-pj45x                        0/1     CrashLoopBackOff   10 (74s ago)   28m

NAME                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/hw06-flask-test-service   ClusterIP   10.111.132.199   <none>        5000/TCP   28m
service/redis-test-service        ClusterIP   10.97.26.170     <none>        6379/TCP   3h47m

NAME                                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/hw06-jbolivar-test-redis-deployment   1/1     1            1           28m
deployment.apps/hw06-test-flask                       0/2     2            0           28m

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/hw06-jbolivar-test-redis-deployment-6dd57664b9   1         1         1       28m
replicaset.apps/hw06-test-flask-85d486665                        2         2         0       28m
```

### 2)
Next we want to execute into the flask api deployment and curl the commands we want to input into the app.py file:
```BASH
kubectl exec -it hw06-test-flask-85d486665-pj45x -- /bin/bash

curl 10.111.132.199:5000/data -X POST
curl 10.111.132.199:5000/data
```
With the expected output of:
```BASH
{
    "name": "Jennifer",
    "id": "10299",
    "recclass": "L5",
    "mass (g)": "539",
    "reclat": "-84.0579",
    "reclong": "69.9994",
    "GeoLocation": "(-84.0579, 69.9994)"
  },
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
```
