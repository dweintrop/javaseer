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

# figure out how to read in java files
JAVA_PROGRAM="program"

# post the data to the server
curl --request POST 'http://localhost:8000/javaseer/' \
		--data-urlencode "student_id=$STUDENT_ID" \
		--data-urlencode "student_name=$STUDENT_NAME" \
		--data-urlencode "javacCall=$*" \
		--data-urlencode "javaProgram=$JAVA_PROGRAM" \
		--data-urlencode "javaCompilerOutput=$RESULTS"

# display the compiler output to the user
echo "$RESULT"
