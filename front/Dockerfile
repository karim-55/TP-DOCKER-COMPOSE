# Étape 1 : build (optionnel pour front statique simple)
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .

# Étape 2 : image finale avec Nginx
FROM nginx:alpine
COPY --from=builder /app /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
