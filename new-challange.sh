#!/usr/bin/env bash

CHALLANGE_NAME=$1
./NameParser.py ${CHALLANGE_NAME} --outputFile _tempNameFile
PROPERCAP_NAME=$(cat _tempNames.json | jq --raw-output ".PROPERCAP")
PASCAL_NAME=$(cat _tempNames.json | jq --raw-output ".PASCAL")
UNDERCAP_NAME=$(cat _tempNames.json | jq --raw-output ".UNDERCAP")
CAMEL_NAME=$(cat _tempNames.json | jq --raw-output ".CAMEL")
LOWUNDER_NAME=$(cat _tempNames.json | jq --raw-output ".LOWUNDER")
KEBAB_NAME=$(cat _tempNames.json | jq --raw-output ".KEBAB")

LANGUAGE="Python3"

if [[ -e ${TARGET} ]]; then
    echo "Target directory already exists: ${TARGET}"
    exit 1
fi

echo "Creating new directory: " $CHALLANGE_NAME
mkdir $CHALLANGE_NAME
 

if [ "$LANGUAGE" == "Python3" ];
then
    echo "Using: " $LANGUAGE
    cp -r _python-template/ $CHALLANGE_NAME/

    sed -i "" -e "s/%%PROPERCAP_NAME%%/${PROPERCAP_NAME}/g" ${CHALLANGE_NAME}/README.md
    sed -i "" -e "s/%%KEBAB_NAME%%/${KEBAB_NAME}/g" ${CHALLANGE_NAME}/README.md

    sed -i "" -e "s/%%CAMELCASE_NAME%%/${CAMEL_NAME}/g" ${CHALLANGE_NAME}/solution.py

    sed -i "" -e "s/%%CAMELCASE_NAME%%/${CAMEL_NAME}/g" ${CHALLANGE_NAME}/test.py
    sed -i "" -e "s/%%PASCAL_NAME%%/${PASCAL_NAME}/g" ${CHALLANGE_NAME}/test.py

else
    echo "No language selected. Exiting"
    exit 2
fi