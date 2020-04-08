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
ENV DEBIAN_FRONTEND noninteractive
# For Open AI Baselines - cmake libopenmpi-dev python3-dev zlib1g-dev
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     cmake libopenmpi-dev python3-dev zlib1g-dev \
#     python-opengl \
#     && rm -rf /var/lib/apt/lists/*
    # vim git \  # Dev tools
    # ffmpeg xvfb x11vnc \  # VNC

# RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
# RUN dpkg-reconfigure --frontend noninteractive tzdata

# RUN pip install --upgrade --no-cache-dir pip
# RUN pip install --upgrade --no-cache-dir gym pytest
# RUN pip install --upgrade --no-cache-dir gym[atari]
# RUN pip install --upgrade --no-cache-dir numpy matplotlib

# Install requirements
COPY requirements.txt /usr
RUN pip install --no-cache-dir -r /usr/requirements.txt

# Install gym_builder from wheel
COPY --from=gym_builder /usr/build /usr/build/
RUN ls /usr/build/dist/
RUN pip install /usr/build/dist/*.whl

# RUN git clone https://github.com/openai/baselines.git
# WORKDIR /usr/src/baselines
# RUN git checkout tf2

# Install by copying files to container
COPY server /usr/src/server/
COPY examples /usr/src/examples/
