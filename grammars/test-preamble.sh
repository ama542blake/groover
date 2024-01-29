OPTIND=1
START_RULE=preamble

while getopts ":s:t:" opt ; do
    case $opt in
        t)
            TEST_FILE="$(pwd)/${OPTARG}"
            echo "Parsing ${TEST_FILE}..."
            ;;
        s)
            START_RULE=$OPTARG
            echo "Start with rule ${START_RULE}"
            ;;
        ?)
            echo "Invalid option: -${opt}."
            exit -1
            ;;
        :)
            echo "Option -${opt} requires an argument."
            exit -1
            ;;
    esac
done

# move to the directory the grammar exists in
cd testable/preamble

# takes input from std in if there's no test file specified
grun Preamble $START_RULE -gui $TEST_FILE

# // return to directory the script was run from
cd ../..
unset START_RULE
unset TEST_FILE