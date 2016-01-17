import json
import octohatrack
import bottle
import os

ipr_limit = 5

app = bottle.Bottle()

# Because Docker, apparently
print(bottle.TEMPLATE_PATH)
bottle.TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))
print(bottle.TEMPLATE_PATH)


@app.get('/')
def helloworld(): 
  return("Enter a URL to do the thing. e.g. /labhr/octohatrack")

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
  return bottle.template('template', result=result)

# Gotta Catch Em All
@app.get('/<filename:path>')
def static(filename):
        print(filename)
        return static_file(filename, root="./")


if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=8080, debug=True)
