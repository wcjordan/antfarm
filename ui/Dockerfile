# Multistage build for JS artifacts
FROM node:13-alpine as js_app
WORKDIR /js_app

# Install React dependencies
COPY js/yarn.lock .
COPY js/package.json .
RUN yarn install --pure-lockfile

# Install React app
COPY js/.prettierrc .
COPY js/public ./public
COPY js/tsconfig.json .
COPY js/.storybook ./.storybook
COPY js/src ./src

# Build React app
RUN yarn build

# Multistage - nginx container
FROM nginx:alpine

# Copy over nginx configuration
RUN rm -f /etc/nginx/conf.d/*
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY conf.d/app.conf /etc/nginx/conf-includes/app.conf
COPY conf.d/server.conf /etc/nginx/conf-includes/server.conf

# Copy over built JS files from React app
COPY --from=js_app /js_app/build/* /www/client/

CMD ["nginx", "-g", "daemon off;"]
