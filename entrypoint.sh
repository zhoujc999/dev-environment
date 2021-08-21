#!/bin/env bash

# Define cleanup procedure
cleanup() {
    echo "Container stopped, performing cleanup..."
}

# Trap SIGTERM
trap 'true' SIGTERM

# Execute command
/home/$USER/docker_files/initialization.py
fish

# Cleanup
cleanup
