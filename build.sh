#!/bin/bash
# Packages the app and dependencies into a deployable zip for Lambda
rm -rf package lambda.zip
pip install -r requirements.txt -t package
cp -r app package/
cd package
zip -r ../lambda.zip .
cd ..
