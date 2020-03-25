# Django container
FROM python:3
WORKDIR /usr/src/app

# Assorted posts recommend setting PYTHONUNBUFFERED but I'm not 100% on the consequences
ENV PYTHONUNBUFFERED 1

# Install system packages.  We need postgresql-client for database backups
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> /etc/apt/sources.list.d/pgdg.list && \
    apt-get -yqq update && \
    apt-get -yqq install postgresql-client-11 && \
    rm -rf /var/lib/apt/lists/*

# Install Django app by copying files to container
COPY requirements.txt /usr
RUN pip install --no-cache-dir -r /usr/requirements.txt

# Install Django app by copying files to container
COPY . /usr/src/app

CMD ["/usr/src/app/launch_server.sh", "--reload"]