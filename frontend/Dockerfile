FROM node:20-alpine

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    g++ \
    cairo-dev \
    jpeg-dev \
    pango-dev \
    giflib-dev \
    python3

COPY package*.json ./
RUN yarn install
COPY . .

EXPOSE 3000

RUN yarn run build
CMD ["yarn", "start"]
