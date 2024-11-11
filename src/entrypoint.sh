#!/bin/bash

cp -r /app/* /docs/

sed -i -e "s|{NAME}|${NAME}|g" /docs/conf.py
sed -i -e "s|{THEME}|${SPHINX_THEME}|g" /docs/conf.py

sphinx-autobuild . _build_html -H 0.0.0.0 --poll