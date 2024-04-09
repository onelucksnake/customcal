#!/bin/sh
cd $(
    cd "$(dirname "$0")"
    pwd
)

rm -rf ./workenv
mkdir -p workenv/run
cp ../setup.py ./workenv
cp ../testScript.py ./workenv/run
cp -r ../customcal ./workenv/customcal
rm -rf ./workenv/customcal/build ./workenv/customcal/dist ./workenv/customcal/*.egg-info
find ./workenv/customcal -type d -name '__pycache__' -exec rm -rf {} +

docker image build -t test_customcal:build .
docker run --rm -it test_customcal:build
# docker rmi test_customcal:build
