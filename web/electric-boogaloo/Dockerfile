FROM node:15-buster-slim AS build

WORKDIR /app

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  python3 && \
  rm -rf /var/lib/apt/lists/*

COPY package.json /app/

RUN yarn

COPY . .

FROM node:15-buster-slim

WORKDIR /app

ENV NODE_ENV production
ENV FLAG flag{5h0uld_h4v3_h1r3d_g1nk01d}

COPY --from=build /app /app

EXPOSE 3000

CMD ["node", "/app/index.js"]
