#!/bin/bash
set -e

# Build the project
echo ""
echo "Create namespace project..."
echo ""
kubectl apply -f kenbot.yml
sleep 2
echo ""
echo "Create namespace Done !"
sleep 1
echo ""
echo "Create ingress project..."
echo ""
kubectl apply -f ingress.yml
sleep 4
echo ""
echo "Create ingress Done !"
sleep 1
echo ""
echo "Create service project..."
echo ""
kubectl apply -f service.yml
echo ""
echo ""
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
echo "Create service Done !"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
echo ""
echo "Create deployment project..."
echo ""
kubectl apply -f deployment.yml
echo ""
echo "Create deployment Done !"
echo "5"
sleep 1
echo "4"
sleep 1
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
kubectl get ingress
kubectl get services
kubectl get pods


echo ""
echo "Done building project!"
echo ""
