FROM python:3.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y sudo
RUN sudo apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN sudo apt install openssl
RUN chmod 755 .
COPY . .