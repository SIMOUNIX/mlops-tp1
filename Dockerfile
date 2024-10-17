FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install "fastapi[standard]" joblib

# copy the api file to the container
COPY api.py /
COPY regression.joblib /
COPY models_utils.py /

CMD ["fastapi", "run", "api.py", "--port", "80"]