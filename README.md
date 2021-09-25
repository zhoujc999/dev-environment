# dev_environment


Figure out: Run command as user

1. To build the image:

Run `docker build -t dev .`

2(a). To pass GitHub token to the container:

Run `docker run -it --rm -p 55555:55555 -e GITHUB_TOKEN=<github-token> dev`

2(b). To authenticate via `https://github.com/login/device`:

Run `docker run -it --rm -p 55555:55555 dev`

2(c). To remove container after stopping:

Run `docker run -it -p 55555:55555 dev`

3. To start a stopped container:

Run `docker start <container-id>` followed by `docker attach <container-id>`
