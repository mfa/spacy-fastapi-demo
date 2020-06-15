# spacy fastapi demo

this demo was for [Python Meetup Stuttgart 2020-06-19](https://www.meetup.com/python-stuttgart/events/270978918/)

## about

Spacy API using fastapi.

## development

```
docker-compose up web
```

url is http://localhost:8021/


## run on google cloud run

info: this needs 1G memory for the spacy model!

```
gcloud builds submit --tag eu.gcr.io/<PROJECT_ID>/spacydemo
gcloud run deploy spacydemo1 --image eu.gcr.io/<PROJECT_ID>/spacydemo --allow-unauthenticated --memory=1G
```
