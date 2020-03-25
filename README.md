Setup
-----
Copy .env_default to .env
Generate secret key running:
python -c "from django.utils.crypto import get_random_string; chars = 'abcdefghijklmnopqrstuvwxyz0123456789\!@#$%^&\*(-\_=+)'; print(get_random_string(50,chars))"
set SECRET_KEY in .env

To prevent docker conflicting with the corporate subnet
As root, create /etc/docker/daemon.json with the content
{
  "bip": "10.1.10.1/24"
}

Copy Schrodinger suite to schrodinger_suite/suite/
rsync -a /scr/suite/2018-3 schrodinger_suite/suite/

Create superuser
`docker-compose run server python manage.py createsuperuser`

Running docker & dev servers
----------------------------

// Build docker services
docker-compose build

// Start docker services
docker-compose up
docker-compose up -d  // detached mode
docker-compose -f production.yml up  // Start for production

// Start JS dev server
yarn start

// Stop docker services
docker-compose stop  // pause container when running in detached mode
docker-compose down  // tear down containers


Misc Tools
----------

// Docker compose
docker-compose ps                           // List docker services
docker-compose run server env               // List environment variables
docker-compose logs                         // Output docker logs

// Pg admin panel
psql -h 0.0.0.0 -p 5432 -U postgres --password

// Django admin shell (import django; django.setup())
docker-compose run --rm server python manage.py shell

// Cleanup unused Docker resources
docker system prune

// Running older experiments
// TODO integrate w/ server & UI
docker build -t antfarm .
// TODO support running w `-u $(id -u):$(id -g)` without breaking bash history
docker run --shm-size=10g -p 5920:5920 -v "$(pwd)"/bash/.bashrc:/root/.bashrc -v "$(pwd)"/bash:/root/bash -it antfarm /bin/bash