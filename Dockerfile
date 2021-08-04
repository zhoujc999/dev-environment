ARG USER="zhoujc999"
ARG PW="docker"
ARG DEBIAN_FRONTEND="noninteractive"

FROM ubuntu:groovy

ENV LC_ALL="en_US.UTF-8"
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US.UTF-8"

COPY [".", "/home/"]
RUN ["/home/install.sh"]
ENTRYPOINT ["/home/entrypoint.sh"]
