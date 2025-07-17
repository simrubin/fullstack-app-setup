FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN rm -rf node_modules package-lock.json
RUN npm install --force
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]