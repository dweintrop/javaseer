# An instrumentation of the java compiler command to log compilation requets on a remote server 

# run javac with the full list of arguments,
# capturing STDERR (2) to STDOUT (&1)
# and store the STDOUT (i.e., the compiler output) in the variable RESULT
RESULT=$(javac $@ 2>&1)

JAVA_CALL="$*"

# read in java file contents
JAVA_PROGRAM="`cat $1`"
shift
while [[ $# -ge 1 ]]
do
  JAVA_PROGRAM="$JAVA_PROGRAM
  
  ---EOF---

  `cat $1`"
  shift
done



# post the data to the server
# note STUDENT_NAME and STUDENT_ID are environment vars set by setup.sh
curl --request POST "$JAVASEER_URL/javaseer/" \
		--data-urlencode "student_id=$STUDENT_ID" \
		--data-urlencode "student_name=$STUDENT_NAME" \
		--data-urlencode "javacCall=$JAVA_CALL" \
		--data-urlencode "javaProgram=$JAVA_PROGRAM" \
		--data-urlencode "javaCompilerOutput=$RESULT"

# display the compiler output to the user
echo "$RESULT"
