FROM alpine:3.19

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

RUN python3 -m venv pyenv
COPY requirements.txt ./
RUN pyenv/bin/pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "pyenv/bin/python3", "bot.py" ]
