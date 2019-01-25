FROM node:8.15.0-onbuild as building
MAINTAINER lizhuliang<lizhuliang@quancheng-ec.com>

RUN mkdir -p /root/
WORKDIR /root/

COPY build /root/build/
COPY config /root/config/
COPY src /root/src/
COPY static /root/static/
COPY test /root/test/
COPY index.html package-lock.json package.json .postcssrc.js .eslintrc.js .eslintignore /root/

RUN npm i
RUN npm run build


FROM nginx:1.14
MAINTAINER lizhuliang<lizhuliang@quancheng-ec.com>

COPY --from=building /root/dist /usr/share/nginx/html
