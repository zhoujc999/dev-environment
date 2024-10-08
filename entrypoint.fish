#!/usr/bin/env fish

# Initialize
if test (id -u) -eq 0
  echo "Initializing container..." \
  && /home/$DOCKER_USER/.docker_files/init.py \
  && chown -R $DOCKER_USER:$DOCKER_USER /home/$DOCKER_USER \
  && runuser --login --shell=/usr/bin/fish $DOCKER_USER
end

# Clean up
echo "Cleaning up..."


