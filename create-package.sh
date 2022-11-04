#!/bin/bash

mkdir src
cp main.py src/lambda_function.py
cp -R handlers src/handlers
cp config.py src/
pip install --target ./src aiogram googletrans==3.1.0a0
cd src
zip -r bot.zip .
cd ..
mv src/bot.zip .
rm -rf src