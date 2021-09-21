# dev_environment


1. Figure out local hosts and ports

`docker build -t dev .`

`docker run -it --rm -p 55555:55555 -e GITHUB_TOKEN=<github-token> dev`

`docker start <container-id>`

`docker attach <container-id>`
