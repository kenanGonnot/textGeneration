#!/bin/bash
set -e

# Build the project
echo ""
echo "Building project..."
echo ""
#docker buildx build --platform linux/amd64 -t thekenken/ovo-mentor-qcm:latest . && docker push thekenken/ovo-mentor-qcm:latest
docker build -t thekenken/text-generation-demo:latest . && docker push thekenken/text-generation-demo:latest


echo ""
echo "Done building project!"
echo ""

# Deploy the project
echo ""
echo "Start project..."
echo ""
#docker run -it thekenken/text-generation-demo:latest

#kubectl delete -f manifests/qcm-ovo-deployment.yml
#kubectl apply -f manifests/qcm-ovo-deployment.yml


echo ""
echo "Done deploying project!"
sleep 1
echo "1"
sleep 1
echo "2"
sleep 1
echo "3"
sleep 1
echo "4"
sleep 1
echo "5"
kubectl get pods