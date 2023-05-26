# move to the directory the grammar exists in
cd testable/composite

# check whether rule name to test was specified
if [[ $1 == "" ]]
then
    grun Composite groove -gui
else
    grun Composite $1 -gui
fi

# // return to directory the script was run from
cd ../..