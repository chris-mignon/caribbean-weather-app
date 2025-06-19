#!/bin/bash

# Set your project root directory
PROJECT_ROOT="caribbean-weather-app"

# Create directories
mkdir -p $PROJECT_ROOT/{data,templates,static/css,static/js,tests}

# Create empty files (or with template content if you wish)
touch $PROJECT_ROOT/app.py
touch $PROJECT_ROOT/requirements.txt
touch $PROJECT_ROOT/Dockerfile
touch $PROJECT_ROOT/README.md
touch $PROJECT_ROOT/data/cities.json
touch $PROJECT_ROOT/templates/index.html
touch $PROJECT_ROOT/static/css/custom.css
touch $PROJECT_ROOT/static/js/main.js
touch $PROJECT_ROOT/tests/test_app.py

echo "Project structure created under $PROJECT_ROOT/"