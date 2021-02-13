from src import app as application
from src import (jwt , jwt_required, JWTManager, create_access_token)
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
@application.route('/<int:myuserid>/login/', methods=['GET'])
def myLogin(myuserid):
    for users in myUsers['users']:
        if myuserid == users['userid']:
            access_token = create_access_token(identity=myuserid)
            return jsonify({myuserid : access_token})
        else:
            newUser = {"userid": myuserid, "level": 0, "highscore": 0}
            myUsers['users'].append(newUser)
            print (myUsers)
            return jsonify({myuserid : "NewUserAdded"})
        
    
        

    #print(myUsers)

@application.route('/test', methods=['GET'])
@jwt_required
def test():
    return ("Authenticated via JWT")