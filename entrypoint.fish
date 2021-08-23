#!/usr/bin/env fish

# Define cleanup procedure

if test (id -u) -eq 0
  echo "Container initializing..."
  /home/$DOCKER_USER/.docker_files/init.py
  chown -R $DOCKER_USER:$DOCKER_USER /home/$DOCKER_USER
  runuser --login --shell=/usr/bin/fish $DOCKER_USER
end

echo "Cleaning up..."


