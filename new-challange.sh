#!/bin/sh

CHALLANGE_NAME=$1
CAP_CHALLANGE_NAME="$(tr '[:lower:]' '[:upper:]' <<< ${CHALLANGE_NAME:0:1})${CHALLANGE_NAME:1}"
UNDERSCORES_CAP_CHALLANGE_NAME=`echo $CHALLANGE_NAME | sed "s/-/_/g"`
CAMELCASE_CHALLANGE_NAME="ToDo"
PASCALCASE_CHALLANGE_NAME="ToDo"

LANGUAGE="Python3"

if [[ -e ${TARGET} ]]; then
    echo "Target directory already exists: ${TARGET}"
    exit 3
fi

echo "Creating new directory: " $CHALLANGE_NAME
mkdir $CHALLANGE_NAME
echo "Using: " $LANGUAGE
cp -r _solution-template/ $CHALLANGE_NAME/
${SED} -i "" -e "s/%%CHALLANGE_NAME%%/${CHALLANGE_NAME}/g" ${CHALLANGE_NAME}/README.md
${SED} -i "" -e "s/%%CHALLANGE_NAME%%/${CHALLANGE_NAME}/g" ${CHALLANGE_NAME}/solution.py
${SED} -i "" -e "s/%%CHALLANGE_NAME%%/${CHALLANGE_NAME}/g" ${CHALLANGE_NAME}/test.py