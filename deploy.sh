#!/bin/bash
set -e

echo "Pushing to origin master..."
git push origin master

echo "Deploying to orac..."
ssh death916@orac "cd /home/death916/prod/deathsite && git pull origin master && sudo systemctl restart deathsite && sudo systemctl is-active deathsite"

echo "Deploy complete!"
