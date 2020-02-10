This readme descripes all steps for starting web app.

##### SETUP  BACKEND

* [Install docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Install docker-compose](https://docs.docker.com/compose/install/)
* `docker-compose build`
* `chmod +x start.sh`
* `./start.sh`
* wait until ALL containers are up
* `chmod +x migrate.sh`
* `./migrate.sh`
##### Backend address 
* http://0:0:0:0:8000