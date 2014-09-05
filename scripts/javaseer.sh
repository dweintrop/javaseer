# An instrumentation of the java compiler command to push to a remote server

# find javac
# if [ -e /usr/gcc ]; then GCC=/usr/gcc; fi;
# if [ -e /usr/bin/gcc ]; then GCC=/usr/bin/gcc; fi;
# if [ -e /usr/local/gcc ]; then GCC=/usr/local/gcc; fi;
# if [ -e /usr/local/bin/gcc ]; then GCC=/usr/local/bin/gcc; fi;

# echo $STUDENT_ID

# run javac with the full list of arguments,
# capturing STDERR (2) to STDOUT (&1)
# and store the STDOUT (i.e., the compiler output) in the variable RESULT
# RESULT=$($GCC $@ 2>&1)
RESULT=$(javac $@ 2>&1)

DATA = "--data \"student_id=$STUDENT_ID\" --data \"student_name=$STUDENT_NAME\""
DATA = "$DATA --data java_command=\"$*\" --DATA \"java_program= \" --data \"java_output=$RESULTS\""

curl --request POST 'http://localhost/Service' "$DATA"

# display the compiler output to the user
echo "$RESULT"
