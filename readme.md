# Plateforme de Streaming de Données en Temps Réel avec Apache Kafka

Groupe 7

- Thierry Pavone TCHOUAMOU PAYONG
- Paul-Henry NGANKAM NGOUNOU

## Description

Ce projet implémente une plateforme de streaming de données en temps réel utilisant Apache Kafka pour la gestion des flux de données. Pour ce projet, nous avons utilisé Python pour les producteurs et consommateurs de données, et Streamlit pour l'interface utilisateur.

### Backend avec Python

Le backend de notre application est développé avec Python, utilisant des bibliothèques comme kafka-python pour l'interaction avec Apache Kafka. Python est un langage flexible et puissant qui facilite la manipulation des données en temps réel et l'intégration avec divers outils de traitement et de stockage des données. Dans ce projet, Python est utilisé pour développer des producteurs qui envoient des données à Kafka, ainsi que des consommateurs qui traitent ces données en temps réel.

### Frontend avec Streamlit

Le frontend est développé avec Streamlit, une bibliothèque Python permettant de créer rapidement des applications web interactives et réactives. Streamlit permet de visualiser en temps réel les données collectées et traitées, offrant une interface utilisateur intuitive pour surveiller et analyser les flux de données.

![alt text](<Architecture globale.png>)

Cette architecture assure une séparation claire des responsabilités entre les différentes couches de l'application et permet de gérer efficacement les données pour différentes villes, assurant ainsi une scalabilité et une maintenabilité efficaces.

## Prérequis

- Docker
- Python
- Apache Kafka

## Installation

1. Cloner le dépôt

   ```bash
       git clone https://github.com/Paul-HenryN/tp-kafka-groupe-7.git
       cd tp-kafka-groupe-7
   ```

2. Installer les dépendances

   ```bash
       pip install -r requirements.txt
   ```

3. Lancer Docker pour kafka et la base de données

   ```bash
       docker-compose up -d
   ```

4. Lancer l'application

   ```bash
       python -m streamlit run live_weather.py
   ```

## Utilisation

Dans cette application, les utilisateurs interagissent avec l'interface utilisateur Streamlit en entrant le nom de la ville dont ils souhaitent les informations. Le backend, agissant en tant que producteur, utilise l'API IoT Weather pour récupérer en temps réel des données météorologiques telles que la température, l'humidité et la pression atmosphérique, en fonction de la ville spécifiée par l'utilisateur. Les consommateurs du backend Python se connectent aux topics de Kafka, récupèrent et traitent ces messages, puis renvoient les résultats du traitement à l'interface utilisateur. Les utilisateurs peuvent ainsi visualiser les données météorologiques en temps réel pour la ville de leur choix directement depuis l'interface Streamlit.
