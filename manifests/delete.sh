#!/bin/bash

# Supprimer le déploiement
kubectl delete deployment text-generation

# Attendre que les pods soient supprimés
while kubectl get pods | grep text-generation; do
  echo "En attente de la suppression des pods..."
  sleep 5
done

# Supprimer le service
kubectl delete service text-generation

# Supprimer la règle Ingress
kubectl delete ingress text-generation-ingress

# Supprimer le namespace
kubectl delete namespace kenbot
