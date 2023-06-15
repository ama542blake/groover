# move to the directory the grammar exists in
cd testable/preamble

# check whether rule name to test was specified
if [[ $1 == "" ]]
then
    grun Preamble preamble -gui
else
    grun Preamble $1 -gui
fi

# // return to directory the script was run from
cd ../..