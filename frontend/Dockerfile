FROM node:18-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:1.25-alpine

COPY --from=builder /app/dist /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

RUN apk add --no-cache bash && \
    rm -rf /var/cache/apk/* /tmp/* && \
    chown -R nginx:nginx /usr/share/nginx/html

EXPOSE 80