#!/bin/bash

set -euo pipefail

echo 'export WINLAIC_DEVICE_NAME='\"${DEVICE_NAME}\" >> ~/.bashrc
echo 'export WINLAIC_CLI_ROOT='$(realpath $(dirname $0)) >> ~/.bashrc
echo 'export PATH=${PATH}:'$(realpath $(dirname $0))/bin >> ~/.bashrc



