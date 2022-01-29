#!/bin/bash

echo "running server"

. image-server-env/bin/activate

export FLASK_APP=image_server

flask run --host 0.0.0.0