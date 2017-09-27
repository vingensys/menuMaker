#! /home/vinod/neuralnetw/python_rest/restapi/bin/python3
# Run a test server.
from MenuMaker import app
app.run(host='127.0.0.1', port=8080, debug=True)
