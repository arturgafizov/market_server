### How to use:

#### Clone the repo:

    git clone https://github.com/arturgafizov/market_server.git
    

#### Before running create your superuser email/password and project name in docker/prod/env/.data.env file

    docker-compose exec alan python manage.py createsuperuser

#### Run the local develop server:

    docker-compose up -d --build
    docker-compose logs -f
    
##### Server will bind 8080 port. You can get access to server by browser [http://localhost:8002](http://localhost:8002)


#### Configuration for develop stage at 8002 port:
    docker-compose -f docker-compose.prod.yml up -d --build

  
### My app is deployed to address:


docker run -it -p 84:80 -e APP=test.com -e CERBOT_EMAIL=djangoblog.artur@gmail.com -d --name alan-front --restart always alan-front
