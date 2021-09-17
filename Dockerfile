FROM ubuntu:hirsute
ENV GITHUB_TOKEN=
ENV DOCKER_USER="zhoujc999"
ENV DOCKER_PASSWORD="password"
ENV NAME="Jingchao Zhou"
ENV EMAIL="zhoujc999@gmail.com"
ENV TZ="America/Los_Angeles"
ARG DEBIAN_FRONTEND="noninteractive"
COPY --chown=$USER [".", "/home/$DOCKER_USER/.docker_files/"]
RUN ["/bin/bash", "-c", "/home/$DOCKER_USER/.docker_files/setup.sh"]
RUN ["/bin/bash", "-c", "/home/$DOCKER_USER/.docker_files/setup.py"]
ENTRYPOINT ["/bin/bash", "-c", "/home/$DOCKER_USER/.docker_files/entrypoint.fish"]
