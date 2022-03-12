##
## Run app
`python -m flask`
### Run in development mode
```
export FLASK_ENV=development`
python -m flask
```
## Run tests
`python -m unittest discover -s tests/classes`

##
`curl http://127.0.0.1:5000/new -X POST -H 'Content-Type: application/json' -d '{"link":"http://test1"}`