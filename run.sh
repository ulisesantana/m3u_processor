#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./run_command.sh <command>"
    exit 1
fi

command=$1

case $command in
    "test")
        echo "Running tests verbosely..."
        python -m unittest discover -v
        ;;
    *)
        echo "Invalid command. Available commands: test"
        exit 1
        ;;
esac
