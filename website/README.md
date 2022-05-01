# COMP90024_Assignment2_SM1_Group34

## To run the web application without docker:
- Make sure you are at uni/connected to the university VPN (otherwise we cannot connect to the CouchDB database hosted on MRC)
- Open two terminals, cd the first one into the client folder and the other one into the server folder
- In the server terminal, type and run "python3 server.py"
- In the client terminal, type and run "npm start"
- Navigate to "http://localhost:3000/" in your browser

## To run the web application using docker compose:
```
# install docker and docker-compose on your machine

docker-compose up -d
```