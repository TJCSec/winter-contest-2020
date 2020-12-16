FROM node:14-buster-slim

WORKDIR /home/app

COPY package.json package-lock.json /home/app/

ENV NODE_ENV production
RUN npm i

EXPOSE 3000

COPY . .

CMD ["npm", "start"]
