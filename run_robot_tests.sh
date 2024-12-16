#!/bin/bash

# Muuttujat
FLASK_PORT=5001
FLASK_URL="http://localhost:$FLASK_PORT"
TEST_COMMAND="poetry run robot --variable HEADLESS:true src/tests"

echo "Running tests"

# käynnistetään Flask-palvelin taustalle
poetry run python3 src/index.py &
FLASK_PID=$!

echo "started Flask server"

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w '%{http_code}' $FLASK_URL)" != "200" ]];
  do sleep 1;
done

echo "Flask server is ready"

# suoritetaan testit
$TEST_COMMAND

status=$?

# pysäytetään Flask-palvelin portissa 5001
kill $FLASK_PID

exit $status
