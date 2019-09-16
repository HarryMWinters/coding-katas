#!/bin/sh
echo "Enter challenge directory name (convention is kebab-case)."
read CHALLANGE_NAME
rm -rf $CHALLANGE_NAME
echo "Creating new directory: " $CHALLANGE_NAME
mkdir $CHALLANGE_NAME
cp _solution-template/* $CHALLANGE_NAME/
find ./$CHALLANGE_NAME -type f | xargs sed -i " " "s/PROBLEM_NAME/$CHALLANGE_NAME/g" $CHALLANGE_NAME/*
echo "Wierd file shadowing going on."