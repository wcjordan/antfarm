# Multistage - gym_tictactoe build container
FROM python:alpine AS gym_builder
WORKDIR /usr/build

COPY environments /usr/build
RUN python setup.py bdist_wheel

# Multistage - Reinforcment learning runtime
FROM tensorflow/tensorflow:1.15.0-py3
WORKDIR /usr/src

# Assorted posts recommend setting PYTHONUNBUFFERED but I'm not 100% on the consequences
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY requirements.txt /usr
RUN pip install --no-cache-dir -r /usr/requirements.txt

# Install gym_builder from wheel
COPY --from=gym_builder /usr/build /usr/build/
RUN ls /usr/build/dist/
RUN pip install /usr/build/dist/*.whl

# Install by copying files to container
COPY webservice /usr/src/webservice/
COPY runners /usr/src/runners/
COPY examples /usr/src/examples/
