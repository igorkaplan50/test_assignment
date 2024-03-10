#!/bin/bash
docker build . -t central_service || exit 1
docker build . -f Dockerfile.entity_recognition_service -t entity_recognition_service || exit 1
docker build . -f Dockerfile.words_count_service -t words_count_service || exit 1
docker build . -f Dockerfile.sentiment_service -t sentiment_service || exit 1