# test_assignment

This repo contains 4 services to emulate the distributed system and
micro-service architecture.

## Description.

In this repo we implement 4 services:
cenntral_service: The main service, which acts as a as microservice manager
and services driver
It has the following configured endpoints:
* get /services: retrieves the list of defined services
* post /services: Adds the service to the list of defined services
* delete /services: deletes the service name from the list of defined services.

### Example:

To add the service we might use the following curl command:

``` bash
curl -X POST "http://localhost:8081" -H "Content-Type: application/json" -d '{"service": "wordscount", "text": "some_text_to_input"}'
```

Please see the services.json file for the list of configured services.

## Usage:

1. All services are dockerized, so you will need the linux or other
operating system with docker configured.

2. Install the pytest as following:

``` bash
pip install pytest
```

3 clone the following repo:

``` bash
git clone https://github.com/igorkaplan50/test_assignment
```

4. There are 4 dockerfiles inside that repo, build them all using the
provided script:

``` bash
./build.sh
```

5. After docker builds are successful run them on the background using
run.sh script. This script will create a virtual network to make sure
containers can communicate with each other and attach all containers to that
network Please watch for any errors during run process. The script will run
all containers on the background, in case of success it will display just
container ids.

6.Usekill.sh script to stop and remove all containers and delete the virtual
network.

## End to end test

The repo also includes the end2end test for all services. To run the test go
to test/e2e directory and run the test as following:

``` bash
pytest -v -s
```

