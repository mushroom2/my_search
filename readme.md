# My search
![alt text][logo]

[logo]: https://media.giphy.com/media/Lr4BQSMAOJfV2TYEmT/giphy.gif "Demo Gif"

## Application to help you search similar sentences in your texts based on word2vec method

### Stack

#### BackEnd
- Python 3.6
- Django 2.2
- DRF
- Elasticsearch 7.3
- Tensorflow
- NLTK

#### FrontEnd

- VueJs 
- Vuetify
- Nuxt
- Vuex

### Requriements

- Docker 
- Docker-compose v3.2+

### Setup

- Clone this repo
- cd ./my_search/docker_local_dev
```bash
docker-compose up
```
- in new terminal tab
```bash
docker exec -it my_search_backend python manage.py fetch_vectorizer
docker exec -it my_search_backend python manage.py reindex_items
```
- Go to ```127.0.0.1``` in your browser
- Enjoy!


#### Road map

- Implement Tensorflow REST server
- Elasticsearch pagination
- Tests

