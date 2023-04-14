#!/bin/bash

REDIS_PROCESS=$(ps aux | grep '[r]edis-server')

if [ -z "${REDIS_PROCESS}" ]; then
	  echo "Redis is not running. Starting Redis..."
	    /usr/local/redis/src/redis-server &
    else
	      echo "Redis is already running."
fi

