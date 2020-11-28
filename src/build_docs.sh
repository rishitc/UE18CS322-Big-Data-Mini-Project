#!/bin/bash

# This command generates the documentation for the project
# NOTE: Ignore the PEP-224 UserWarnings
pdoc3 --html --force . --output-dir ./documentation/

