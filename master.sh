#!/bin/bash

if [ $1 == "updateDB" ]
then
    if [ $2 ] 
    then 
        python3 update_db.py $2
    else
        echo "Usage: ./master.sh updateDB <path_to_json>"
    fi
fi