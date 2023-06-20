# move to the directory the grammar exists in
cd testable/preamblecondensed

# check whether rule name to test was specified
if [[ $1 == "" ]]
then
    grun PreambleCondensed preamble -gui
else
    grun PreambleCondensed $1 -gui
fi

# // return to directory the script was run from
cd ../..