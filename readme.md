# Flask demo app

Simple Flask based demonstration about making frontend and backend application. 
Designed to work in container environments.

## Docker

```
docker-compose up
```

## Kubernetes / openshift

Made with [CSC Rahti contrainer cloud](https://rahtiapp.fi) in mind. 

```
oc login <snip>
kubectl apply -f ./frontend-k8s.yaml
kubectl apply -f ./backend-k8s.yam
```