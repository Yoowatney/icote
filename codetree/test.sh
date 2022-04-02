#!/bin/bash


FILE=test
if [ -e "$FILE" ];then 
	rm -rf test
	echo "test file is deleted"
else
	echo "test file is not deleted"
fi
