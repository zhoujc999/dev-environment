#!/bin/env bash

# Define cleanup procedure
cleanup() {
    echo "Container stopped, performing cleanup..."
}

# Trap SIGTERM
trap 'true' SIGTERM

# Execute command
fish

# Cleanup
cleanup
