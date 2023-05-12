#! /bin/bash


play=1
while [ $play -eq 1 ]
do
    echo ""
    echo "Would you like to play Rock-Paper-Scissors?"
    echo ""

    read response

    if [ $response == "yes" ] || [ $response == "y" ]
    then
        echo ""
        
        python3 ./rock_paper_scissors.py
    else
        echo "Ok, maybe next time."
        play=0
    fi
done
