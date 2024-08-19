#!/usr/bin/bash
#manim --disable_caching -qh -p bayesian.py
set -e
source .venv/bin/activate
manim -qh -p apptainer.py
manim-slides convert --to html -c progress=true -c controls=true -cslide_number=true "Apptainer" "Apptainer.html"
./node_modules/html-inject-meta/cli.js < Apptainer.html  > index.html
firefox index.html
