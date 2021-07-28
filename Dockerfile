FROM ubuntu:latest
COPY [".", "/home/"]
ENV USER="zhoujc999"
RUN ["chmod", "700", "-R", "/home/"]
RUN ["/home/install.sh"]
CMD ["fish"]
