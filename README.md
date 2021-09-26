# dev_environment

1. Environment variables to set:
    1 `GITHUB_TOKEN`
    2. `DOCKER_USER`
    3. `DOCKER_PASSWORD`
    4. `NAME`
    5. `EMAIL`

2. To build the image:

Run `docker build -t dev .`

3(a). To pass GitHub token to the container:

Run `docker run -it --rm -p 55555:55555 -e GITHUB_TOKEN=<github-token> dev`

3(b). To authenticate via `https://github.com/login/device`:

Run `docker run -it --rm -p 55555:55555 dev`

3(c). To remove container after stopping:

Run `docker run -it -p 55555:55555 dev`

4. To start a stopped container:
    1. Run `docker start <container-id>`
    2. Run `docker attach <container-id>`

TODO: Figure out venv

