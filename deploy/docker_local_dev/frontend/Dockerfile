FROM node:8.10.0-alpine
RUN mkdir /app
WORKDIR /app
RUN apk update && apk upgrade && apk add git
ADD . /app/
RUN npm install
RUN npm run build
ENV HOST 0.0.0.0
EXPOSE 3000
CMD [ "npm", "start" ]