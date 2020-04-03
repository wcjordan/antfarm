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
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim git \
    ffmpeg xvfb x11vnc \
    cmake libopenmpi-dev python3-dev zlib1g-dev \
    python-opengl \
    && rm -rf /var/lib/apt/lists/*

RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN pip install --upgrade --no-cache-dir pip
RUN pip install --upgrade --no-cache-dir gym pytest
RUN pip install --upgrade --no-cache-dir gym[atari]
RUN pip install --upgrade --no-cache-dir numpy matplotlib

# Install gym_builder from wheel
COPY --from=gym_builder /usr/build /usr/build/
RUN ls /usr/build/dist/
RUN pip install /usr/build/dist/*.whl

# RUN git clone https://github.com/openai/baselines.git
# WORKDIR /usr/src/baselines
# RUN git checkout tf2

# Install by copying files to container
COPY entrypoint.sh /usr/src/
COPY examples /usr/src/examples/

ENV DISPLAY :20
EXPOSE 5920

ENTRYPOINT ["/usr/src/entrypoint.sh"]
