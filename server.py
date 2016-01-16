import json
import octohatrack
from bottle import Bottle, request, response, run, static_file, template

ipr_limit = 5

app = Bottle()

@app.get('/')
def helloworld(): 
  return("Enter a URL to do the thing. e.g. /labhr/octohatrack")
#    return static_file("index.html", root="./")

@app.route('/data/<username>') 
def username(username):
  return("User %s, but require a repo too" % username)
  print("Got %s" % username)

@app.route('/<username>/<repo>')
def repo(username, repo):
  full_repo = "%s/%s" % (username, repo)
  con = octohatrack.get_code_contributors(full_repo)
  com = octohatrack.get_code_commentors(full_repo, ipr_limit)

  non = []
  for user in com:
    if user not in con:
      non.append(user)

  print(con)
  print(com)
  print(non)

  result = { "non": non, "con": con, "limit": ipr_limit, "repo": full_repo}
  return template('test', result=result)

# Gotta Catch Em All
@app.get('/<filename:path>')
def static(filename):
        print(filename)
        return static_file(filename, root="./")


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
