FROM ubuntu:groovy
ARG USER="zhoujc999"
ENV GITHUB_TOKEN=
ARG DEBIAN_FRONTEND="noninteractive"
RUN ["/bin/bash", "-c", "useradd --create-home --shell /usr/bin/fish $USER"]
COPY --chown=$USER [".", "/home/$USER/docker_files/"]
RUN ["/bin/bash", "-c", "/home/$USER/docker_files/install.sh"]
USER $USER
WORKDIR /home/$USER
ENTRYPOINT ["/bin/bash", "-c", "$PWD/docker_files/entrypoint.sh"]
