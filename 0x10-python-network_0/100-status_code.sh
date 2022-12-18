#!/bin/bash
# displays only the status code
curl -si -o /dev/NULL -w "%{http_code}" "$1"
