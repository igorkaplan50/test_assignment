docker network create test_network
docker run --name central_service --network test_network -d -p8081:8081 central_service
docker run --name words_count_service --network test_network -d -p8083:8083 words_count_service
docker run --name sentiment_service --network test_network -d -p:8082:8082 sentiment_service
docker run --name entity_recognition_service --network test_network -d -p8084:8084 entity_recognition_service
