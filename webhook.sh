#!/bin/bash

# This should return a link to a log-stream relating to the re-pulling of the image and restarting the app
curl -dH -X POST $WEBHOOK_URL
 