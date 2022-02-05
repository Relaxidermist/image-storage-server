#!/bin/bash

echo "running server"

PROJECT_PATH=/home/pi/code/image-storage-server/

cd $PROJECT_PATH

. image-server-env/bin/activate

export FLASK_APP=image_server

flask run --host 0.0.0.0