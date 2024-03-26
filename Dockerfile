FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    build-essential


# copy
COPY . /app
WORKDIR /app


# install req.txtx
RUN pip3 install -r requirements.txt

CMD ["python3", "frame_processing.py"]
