from src import app as application
from flask import request, jsonify


# My User Json:
myUsers = {
	"users": [{
			"userid": 100,
			"level": 1,
			"highscore": 10
		},
		{
			"userid": 101,
			"level": 2,
			"highscore": 5
		}
	]
}

# 4.1 Login
@application.route('/login/', methods=['GET'])
def myLogin():
       

    return jsonify({"userid" : "123"})
