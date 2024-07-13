FROM node

WORKDIR /frontend

RUN npm install -g live-server

COPY . .

CMD ["live-server", "--cors", "--port=8001", "--open=index.html"]