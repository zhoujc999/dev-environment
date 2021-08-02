ARG USER="zhoujc999"
ARG PW="docker"

FROM ubuntu:groovy

ENV DEBIAN_FRONTEND="noninteractive"
ENV LC_ALL="en_US.UTF-8"
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US.UTF-8"

COPY [".", "/home/"]
RUN ["/home/install.sh"]
RUN ["locale-gen", "en_US.UTF-8"]
CMD ["fish"]
