#!/bin/bash
# send a GET request with customized header
curl -s -X GET --header "X-School-User-Id: 98" "$1"
