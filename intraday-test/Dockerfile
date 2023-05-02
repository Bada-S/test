FROM prefecthq/prefect:2-python3.7
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY *.py /modules/
COPY requirements.txt .
# COPY goog_keyfile.json .
ENV PYTHONPATH=$PYTHONPATH:modules/
RUN pip install -r requirements.txt