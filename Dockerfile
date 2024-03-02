FROM python:3.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python.exe -m pip install --upgrade pip && pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .