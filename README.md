Setup
-----
Copy .env_default to .env
Set SECRET_KEY & DB_PASS in .env
  These should be random secure strings
  e.g. head -c 32 /dev/urandom | base64

To prevent docker conflicting with the corporate subnet
As root, create /etc/docker/daemon.json with the content
{
  "bip": "10.1.10.1/24"
}

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
