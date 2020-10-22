#!/bin/bash

echo "Creating the fastapi deployment and service..."

kubectl create -f ./k8s/fastapi-deployment.yml
kubectl create -f ./k8s/fastapi-service.yml

echo "Adding the ingress..."

minikube addons enable ingress
kubectl apply -f ./k8s/minikube-ingress.yml --validate=false

echo "DONE!"