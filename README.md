# dev_environment

1. Set environment variables:
    * `GITHUB_TOKEN`
    * `DOCKER_USER`
    * `DOCKER_PASSWORD`
    * `NAME`
    * `EMAIL`

2. Build the image:
   Run `docker build -t dev .`

3. Start the container:
    * Run `docker run -it --rm -p 55553:55553 dev`

4. To start a stopped container:
    1. Run `docker start <container-id>`
    2. Run `docker attach <container-id>`

TODO: Figure out venv

