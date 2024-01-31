# move to the directory the grammar exists in
cd testable/independent

# check whether rule name to test was specified
if [[ $1 == "" ]]
then
    grun Independent groove -gui
else
    grun Independent $1 -gui
fi

# // return to directory the script was run from
cd ../..