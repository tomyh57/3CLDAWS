# Rapport : Projet Final AWS de FIGAROLI Romain

Date : 19/02/2025 

Créé par : KADI Soulaymane, HOMBOURGER Tomy, BERNARD Jonathan, AHMADI Rateb et FIGAROLI Romain


# Partie 1 : Configuration sur AWS 

## Création du VPC : 
### Qu'est ce qu'un VPC
Un VPC (Virtual Private Cloud) sur AWS est un réseau virtuel dédié à ton compte AWS, dans lequel tu peux déployer tes ressources (serveurs EC2, bases de données RDS, etc.) de manière isolée et sécurisée. Il fonctionne comme un réseau privé dans le cloud, similaire à un réseau traditionnel dans un datacenter.

Il nous a servis à créer notre réseau pour notre projet avec les tables de routages ; sous-réseaux, gateway.

![image](https://github.com/user-attachments/assets/bb9d68e6-f875-49fe-99aa-d2fe516e7272)

## Sous-réseaux : 
### Qu'est ce qu'un sous-réseau
Un sous-réseau (subnet) est une subdivision d’un VPC sur AWS, permettant d’organiser et d’isoler les ressources. Chaque sous-réseau appartient à une zone de disponibilité (AZ) et peut être public (accessible depuis Internet) ou privé (isolé d’Internet).

![image](https://github.com/user-attachments/assets/4a433005-3fed-420f-ad9e-54a597e1e185)

## Table de routage publique :
### Qu'est ce qu'une table de routage
Une table de routage sur AWS est un ensemble de règles qui déterminent comment le trafic réseau est dirigé à l'intérieur d'un VPC. Elle associe des sous-réseaux à des destinations (Internet, autres sous-réseaux, VPN, etc.) via des routes définissant le chemin du trafic.

Nous avons créé des routes afin de diriger le trafic vers notre base de données ainsi qu'à notre instance de test.

![image](https://github.com/user-attachments/assets/72edd5d7-f748-4558-b965-fa61f0009e37)

## Table de routage private 1 :
Nous avons créé des routes afin de diriger le trafic vers notre instance public et vers la nat gateway.

![image](https://github.com/user-attachments/assets/ac9ebd96-60c1-4a54-9738-2e2c0cce8b40)

## NAT : 
### Qu'est ce qu'une NAT
Une NAT (Network Address Translation) sur AWS permet aux instances situées dans un sous-réseau privé d’accéder à Internet (pour télécharger des mises à jour, API, etc.) sans être directement exposées. Elle peut être déployée via une NAT Gateway (gérée par AWS) ou une NAT Instance (serveur EC2 configuré pour la translation d’adresses réseau).

![image](https://github.com/user-attachments/assets/a9f2d50d-480c-4004-b970-214b0d73409f)

## Passerelle internet : 
### Qu'est ce qu'une passerelle internet
Une passerelle Internet (Internet Gateway - IGW) sur AWS est un composant réseau qui permet aux instances d’un sous-réseau public de communiquer avec Internet. Elle assure la translation d’adresses IP (NAT) pour les instances disposant d’une IP publique ou Elastic IP.

![image](https://github.com/user-attachments/assets/f861904f-3ac8-46ea-a26f-8c7c74c0756f)

## Groupe de sécurité privé : 
### Qu'est ce qu'un groupe de sécurité privé
Un groupe de sécurité (Security Group) sur AWS est un pare-feu virtuel qui contrôle le trafic entrant et sortant des ressources (comme les instances EC2). Il fonctionne avec des règles autorisant ou bloquant le trafic basé sur les ports, protocoles et adresses IP.

Nous avons autorisé le port 22 afin de pouvoir se connecter en SSH à notre instance.

![image](https://github.com/user-attachments/assets/18cc92cc-b345-4331-b435-16677b12fc91)

## Groupe de sécurité public : 
Nous avons autorisé le port 22 afin de pouvoir se connecter en SSH à notre instance. Ainsi que le port 3306 qui est le port pour MySQL, le port 5085 qui est le port de notre application flask python. Aussi les ports 80 et 443 pour la connexion en HTTP et HTTPS.

![image](https://github.com/user-attachments/assets/839d03ea-30f3-451f-8783-700e04ceb67f)

## Création de la base de données : 
### Qu'est ce qu'une base de données
Une base de données est un système organisé permettant de stocker, gérer et récupérer des données de manière structurée. Elle peut être relationnelle (SQL, avec des tables) ou non relationnelle (NoSQL, avec des documents, graphes, etc.).

Dans notre cas, c'est une base de donnée relationnelle avec MySQL

![image](https://github.com/user-attachments/assets/6edb3f81-689c-43ac-94d6-d291828c1d6e)

## Groupe de sous-réseaux DB :
### Qu'est ce qu'un groupe de sous-réseaux
Un groupe de sous-réseaux (Subnet Group) sur AWS est un ensemble de sous-réseaux situés dans différentes zones de disponibilité (AZ). Il est utilisé principalement par des services comme Amazon RDS ou ElastiCache pour assurer la haute disponibilité et la répartition des ressources dans un VPC.

![image](https://github.com/user-attachments/assets/a52ed422-1cf0-4a26-b223-6207738acf8e)

## Règles des groupes de sécurité :
### Qu'est ce qu'une règle de groupe de sécurité
Une règle de groupe de sécurité sur AWS définit les autorisations de trafic entrant et sortant d’un groupe de sécurité. Chaque règle spécifie un protocole (TCP, UDP, etc.), un port, et une plage d’IP autorisée, permettant de contrôler l’accès aux ressources comme les instances EC2.

![image](https://github.com/user-attachments/assets/4ecf50b7-8070-4687-9c09-efb722acf9c3)

## Création de l'instance EC2 publique et privée
### Qu'est ce qu'une instance EC2
Une instance EC2 (Elastic Compute Cloud) sur AWS est un serveur virtuel dans le cloud qui permet d'exécuter des applications. Elle offre une capacité de calcul évolutive, avec un choix de types d’instances adaptés aux besoins en CPU, RAM et stockage.

### Publique :
![image](https://github.com/user-attachments/assets/0db8aea7-2b88-4124-957d-2d2b105d7dbf)
![image](https://github.com/user-attachments/assets/1575cd57-e7c2-44bc-8091-3cf3b9ff71f3)

### Cré&ation de la paire de clés
Une paire de clés pour une instance EC2 sur AWS est composée de deux éléments : une clé publique (stockée sur AWS) et une clé privée (que tu gardes). Elle sert à sécuriser l’accès à l’instance EC2 via SSH (Linux) ou RDP (Windows) sans avoir besoin de mots de passe.

![image](https://github.com/user-attachments/assets/0d024bc8-1a18-49bc-95aa-f5f04ed6b9bd)

### Privée :
![image](https://github.com/user-attachments/assets/fbea78f2-e709-474e-babf-1db41d4c65fe)

## Qu'est ce qu'un cloudinit pour les instance EC2
Cloud-init est un outil utilisé sur AWS (et d'autres plateformes cloud) pour automatiser la configuration initiale d'une instance EC2 lors de son démarrage. Il permet de déployer des scripts, installer des logiciels, configurer des paramètres réseau, créer des utilisateurs, etc., sans intervention manuelle, directement à partir des métadonnées de l'instance.

### Cloudinit à mettre dans la création de l'instance EC2

```
#!/bin/bash  
sudo apt update -y && sudo apt upgrade -y  
sudo apt install -y docker.io git default-mysql-client  
sudo systemctl start docker  
sudo systemctl enable docker  

sudo usermod -aG docker ubuntu  

git clone https://github.com/app-generator/flask-datta-able.git  

cd flask-datta-able  

docker build -t flask-datta-able . 

docker run -d -p 5085:5085 --name flask-app flask-datta-able
```
![image](https://github.com/user-attachments/assets/2b41ff51-3f0e-4b95-a8c7-bf4d5ac93e13)

# Partie 2 : Configuration sur la VM 

### Connexion en SSH sur le VM grâce à la clé générée 
Une connexion SSH (Secure Shell) est un protocole réseau sécurisé qui permet de se connecter à un serveur distant (comme une instance EC2) pour l’administrer à distance. Elle utilise une clé privée et un port spécifique pour assurer la confidentialité et la sécurité des échanges.

![image](https://github.com/user-attachments/assets/b699835e-d7e0-495b-b906-1919c41530d9)

Preuve de la connexion à l'instance en SSH :

![image](https://github.com/user-attachments/assets/c77094ca-8d38-47d6-bba2-5c63c8263507)

### Modification du fichier .env pour établir la connexion avec la base de données
Les informations DB_NAME, DB_USERNAME, DB_PASS, DB_PORT et DB_HOST ont été renseignées en fonction de notre base de données créée plus tôt.

![image](https://github.com/user-attachments/assets/6e3c4b2b-378d-4651-80ef-6f9e8e325050)

### Création de l'image : 
Nous avons créé l'image à l'aide de la commande : ```docker-compose up -d```

![image](https://github.com/user-attachments/assets/b81c0db5-29b9-4e83-8417-123cbc8133c9)

### Vérification de l'image : 
Nous avons vérifié l'image à l'aide de la commande : ```docker ps```

![image](https://github.com/user-attachments/assets/86041d11-767d-4f91-9d17-7a78d96cf3ac)

### Vérification de l'accès à l'application grâce à la commande curl et avec l'interface web
On peut constater que en faisant la commande ```curl http://54.202.208.199:5085```, notre application est accessible.

![commane curl](https://github.com/user-attachments/assets/79170b9d-bafa-4c87-8692-f758134c8b7c)

On accède également à notre application depuis l'URL : ```http://54.202.208.199:5085```.

![interface web](https://github.com/user-attachments/assets/9e2fd872-b2c8-4248-a1f6-b8b648bc3063)

# Partie 3 : Modification du virtual env pour connecter la DB et l'application

### Mettre à jour le config.py :
Dans le fichier config.py, il faut mettre les bonnes informations de notre base de donnés : DB_NAME, DB_USERNAME, DB_PASS, DB_PORT et DB_HOST

![image](https://github.com/user-attachments/assets/c6b27351-513f-489f-9d3e-7299c8649111)

### Création et activation d'un environnement virtuel Python : 
#### Pourquoi créer un environnement virtuel
La création et l’activation d’un environnement virtuel Python permettent d’isoler les dépendances d’un projet pour éviter les conflits avec d’autres projets ou avec les paquets installés globalement sur la machine.

Nous avons créé l'environnement virtuel python avec ces commande : 

```
bash 
CopierModifier 
python3 -m venv venv 
source venv/bin/activate 
```
![image](https://github.com/user-attachments/assets/e5d6e57b-1c74-4ddf-95d3-45fdf2b861f4)

### Modifier requirements.txt pour ajouter pymysql :
![image](https://github.com/user-attachments/assets/0fb4ca54-209a-4759-b930-3462b92d5361)

Ensuite lancer la commande : 
```
pip install -r requirements.txt
```

### À cause des erreurs d’environnements, on a dû installer :  

```
pip install flask-migrate 
```

### Mettre à jour pip, setuptools et wheel  

Cette commande : 
```pip install --upgrade pip setuptools wheel ``` 

remplace : python3-distutils qui est requit pour la migration 

nous  avons eu des erreurs car la python3-distutils n’était pas reconnu 

### Connexion de la DB et l'application
![image](https://github.com/user-attachments/assets/c5f2bbf7-c815-41f8-b087-4fa1ffce2335)
![image](https://github.com/user-attachments/assets/1d31abd6-1349-4b59-92a5-24162bd2f23c)
![image](https://github.com/user-attachments/assets/2d782320-5e33-4683-a40e-f7b2fdc9e683)

### Connexion à la DB et vérification de la base de donnés
Nous avons vérifié que noter base de donnés était présente avec la commande ```SHOW DATABASES```

![image](https://github.com/user-attachments/assets/db936769-8bb1-4b00-8080-5b6f8f833f5b)
![image](https://github.com/user-attachments/assets/8b1713ce-a8a5-4602-ac0b-dfae13062031)

# Partie 4 : Test de la connexion entre la DB et l'application

### Création d'un compte utilisateur sur l'interface web 

![image](https://github.com/user-attachments/assets/e37c8da1-7b04-4a70-9b20-cf51687dc182)

### Vérification de l'utilisateur créé en amont sur l'interface web
Nous avons vérifié que l'utilisateur créé sur l'interface web était présent dans la base de donnés avec la commande ```Select * FROM users;```

![image](https://github.com/user-attachments/assets/836dfe09-d5d8-42f3-994b-e5125f593b47)


# Partie 5 : Création du bucket S3
### Qu'est ce qu'un Bucket S3
Un bucket S3 sur AWS est un conteneur de stockage utilisé pour stocker des objets (fichiers, images, vidéos, backups, etc.) dans le service Amazon S3 (Simple Storage Service). Chaque bucket a un nom unique globalement, et tu peux gérer les autorisations, la version des fichiers et les règles de cycle de vie pour optimiser le stockage et la sécurité.

### Création du bucket S3
![image](https://github.com/user-attachments/assets/7ca8a8dd-77e8-4c5c-92bb-464d8bcb1ab3)

### Activation de l’hébergement de site web statique  
![image](https://github.com/user-attachments/assets/21abe861-275a-48c7-a724-caf2a812bdd5)

###  Autorisation de l’accès au public  
![image](https://github.com/user-attachments/assets/dc94255d-bf5a-48dd-a3bc-b690d4d9ad6f)

### Ajouter une politique de bucket S3 pour autoriser l'accès public 
![image](https://github.com/user-attachments/assets/1ea2d481-5939-4bee-a147-03585d53b25c)

### Installation de la dépendance ZIP
![image](https://github.com/user-attachments/assets/11a91f94-5681-44d5-b6d9-dac70cd949c9)

### ZIP de l’application flask-datta-able 
![image](https://github.com/user-attachments/assets/bee48548-c5fd-4fc1-a463-ff6bfbe4974d)

### Sauvegarde de la base de données en format SQL  
![image](https://github.com/user-attachments/assets/e9a1fa6f-142e-4ec3-8119-5b5f099fedb6)

### Sauvegarde de l’application et de la base données
![image](https://github.com/user-attachments/assets/d50328b3-6434-4e84-b479-e3de271603d4)

### Configuration de GIT pour importer notre projet et le télécharger en .zip
![image](https://github.com/user-attachments/assets/8395fba8-4b79-4c28-ad0f-989c46aa246b)
![image](https://github.com/user-attachments/assets/cf2c6f18-78d1-481e-8eda-7b381eccfc34)

### Ajouter l'URL du dépôt distant :  
![image](https://github.com/user-attachments/assets/0008be3a-6904-4c67-925b-08a02d2ba655)

### Initialiser le dépôt :  
![image](https://github.com/user-attachments/assets/49417294-3e50-449e-9464-c573e8dc8ff2)

### Ajouter les fichiers modifiés : 
![image](https://github.com/user-attachments/assets/f3bffbbd-cf9a-4312-baa5-acdc8ecc0362)

### Créer un commit :  
![image](https://github.com/user-attachments/assets/679044e0-b3c1-4afe-8160-7c6f8eb7500b)

### Mettre branch main en principal :  
![image](https://github.com/user-attachments/assets/037132f2-0b1e-4254-b4ed-93fd7f493c82)

### Push les changements 
![image](https://github.com/user-attachments/assets/92789df9-8e60-4470-ab83-0508fdb61510)
# Il faut générer un access token pour avoir la possibilité de push
![image](https://github.com/user-attachments/assets/2b5fb217-fc42-4313-8e56-22f9603a7108)

### Envoie du backup de l’application et de la base de données vers le bucket S3  
![image](https://github.com/user-attachments/assets/e4f2e64c-8aae-49d8-9e4e-79a2c9dbcff9)


# Partie 6 : Serveur de test

### Création du serveur de test

#### Le fichier .pem a été crée grâce à la commande : nano projet-final-roro-ect.pem.
Nous avons collé le contenu de la paire de clés sur l'instance public afin de se connecter sur l'instance de test depuis l'instance public.

![image](https://github.com/user-attachments/assets/cbf6036a-5e0a-4f55-a005-5878425087f4)

Nous arrivons à ping l'adresse de google depuis l'instance de test grâce à la NAT Gateway;

![image](https://github.com/user-attachments/assets/999f539f-8630-448e-8b26-7f7b384f7114)




