#!/bin/bash

OUTPUT_CSV='output.csv'
INTERVAL=${INTERVAL:-1}

function handle_sigint() {
    echo -e "\nSIGINT received, exiting..."
    exit 0
}

trap handle_sigint SIGINT

function log_free_memory() {
    local timestamp=$(date --iso-8601=seconds)
    local free_memory=$(free --mega | awk '/^Mem:/{print $4}')
    echo "${timestamp},${free_memory}"
}
