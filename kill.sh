docker stop central_service
docker rm central_service

docker stop words_count_service
docker rm words_count_service

docker stop sentiment_service
docker rm sentiment_service

docker stop entity_recognition_service
docker rm entity_recognition_service

docker network rm test_network
