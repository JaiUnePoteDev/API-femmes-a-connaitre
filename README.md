# API-femmes-a-connaitre

Une API réalisée avec FastAPI (Python) listant une centaine de femmes inventrices, chercheuses, autrices, sportives, astronautes, astronomes, aviatrices, ...

Elles sont extrêmement nombreuses, cette liste n'est donc bien sûr pas exhaustive. 

C'est une excellente manière de découvrir des figures invisibilisées, voire carrément effaçées.

Raviver cette mémoire à travers des projets est impératif !

## Lancer le projet en local :

### 1. Installer les dépendances :

```shell
pip install -r requirements.txt
```

### 2. Lancer le projet :

Le projet se lancera sur le port 8000 : [http://127.0.0.1:8000](http://127.0.0.1:8000)

```shell
python -m run uvicorn main:app --reload
```

## Lancer le projet avec Docker :

### 1. Construire l'image Docker :

```shell
docker build -t api-femmes-a-connaitre .
```

### 2. Lancer le projet :

Le projet se lancera sur le port 8000 : [http://127.0.0.1:8000](http://127.0.0.1:8000)

```shell
docker run -p 8000:80 api-femmes-a-connaitre
```

## Lancer le projet avec Docker Compose :

### 1. Lancer le projet :

Le projet se lancera sur le port 8000 : [http://127.0.0.1:8000](http://127.0.0.1:8000)

```shell
docker-compose up
```

## Documentation de l'API

La documentation de l'API est disponible sur [http://127.0.0.1/docs](http://127.0.0.1/docs)

## Instance de démo

* [https://api-de-femmes-a-connaitre.onrender.com](https://api-de-femmes-a-connaitre.onrender.com)

 * Documentation sur : [https://api-de-femmes-a-connaitre.onrender.com/docs](https://api-de-femmes-a-connaitre.onrender.com/docs)
