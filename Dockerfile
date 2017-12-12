FROM python:3.6.3
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential \
  cmake \
  pkg-config \
  libx11-dev \
  libatlas-base-dev \
  libgtk-3-dev \
  libboost-python-dev \
  libopencv-dev \
  python-opencv

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN pip install ./
