#!/bin/bash

echo ""
echo "---------------"
echo "SPACETOWER PYTHON CLIENT GENERATOR"
echo "---------------"
echo ""

echo ""
echo "---------------"
echo "OpenAPI spec downloader"
echo "---------------"
echo ""

read -p "OpenAPI spec URL: " OPENAPI_SPEC

echo "Selected OpenAPI spec: $OPENAPI_SPEC"
sleep 2
echo ""
echo "Downloading API docs..."

# try to download API docs, if not successful, exit
if ! curl $OPENAPI_SPEC -o fds.yaml; then
  echo "Failed to download OpenAPI spec."
  read -p "Press enter to exit"
  exit 1
fi
echo "Done!"

# Print space
echo ""
echo "---------------"
echo "CODE GENERATION"
echo "---------------"
echo ""
# Open yaml file and get API version (it is in info/version)
# PROJECT_VERSION=$(awk '/version/{print $2}' fds.yaml)
PACKAGE_NAME='spacetower_python_client'
PROJECT_NAME='spacetower-python-client'

read -p "Project version: " PROJECT_VERSION


echo "Project name: $PROJECT_NAME"
echo "Project version: $PROJECT_VERSION"
echo "Package name: $PACKAGE_NAME"
echo ""
read -p "Press enter to continue"

echo "Generating API client (version $PROJECT_VERSION)..."

# Generate FDS API client
openapi-generator-cli generate \
  -i ./fds.yaml \
  -g python \
  -o . \
  --skip-validate-spec \
  --http-user-agent \ "spacetower-sdk/python/$PROJECT_VERSION" \
  --additional-properties="projectName=$PROJECT_NAME,packageName=$PACKAGE_NAME,packageVersion=$PROJECT_VERSION"
echo ""
echo "Done!"
echo ""


read -p "Press enter to exit"
