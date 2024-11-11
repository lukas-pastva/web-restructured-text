#!/bin/bash

cp -r /docs-temp/..data/* /docs/
cp -r /app/* /docs/

sed -i -e "s|{NAME}|${NAME}|g" /docs/conf.py
sed -i -e "s|{THEME}|${SPHINX_THEME}|g" /docs/conf.py

#tail -F /dev/null
sphinx-autobuild . _build_html -H 0.0.0.0 --poll