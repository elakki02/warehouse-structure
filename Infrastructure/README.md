**Port Mapping Explanation**: 
`docker run -p 8080:8080` maps host port 8080 → container port 8080, 
bridging the isolated Docker network to your laptop for http://localhost:8080/fhir/ access**
# HAPI FHIR Infrastructure
1. docker pull hapiproject/hapi:latest
2. docker run -p 8080:8080 hapiproject/hapi:latest
3. http://localhost:8080/fhir/
