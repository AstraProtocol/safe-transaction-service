#!/bin/bash

set -euo pipefail

if [ ${RUN_APP:-0} = 1 ]; then
    exec docker/web/run_web.sh
fi

if [ ${RUN_APP:-0} = 2 ]; then
    exec docker/web/celery/worker/run.sh
fi

if [ ${RUN_APP:-0} = 3 ]; then
    exec docker/web/celery/worker/run.sh
fi

if [ ${RUN_APP:-0} = 4 ]; then
    exec docker/web/celery/worker/run.sh
fi

if [ ${RUN_APP:-0} = 5 ]; then
    exec docker/web/celery/scheduler/run.sh
fi


if [ ${RUN_APP:-0} = 6 ]; then
    exec docker/web/celery/flower/run.sh
fi
