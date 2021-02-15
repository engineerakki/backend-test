from src import app as application
from src import (jwt , jwt_required, JWTManager, create_access_token, get_jwt_identity)
from flask import request, jsonify
import datetime as dt

###################################################
######### User model for the problem ##############
###################################################


user_model = {
	"users": [{
			"userid": 100,
			"level": 1,
            "score": 5,
		},
		{
			"userid": 101,
			"level": 2,
            "score": 5,
		},
        {
			"userid": 100,
			"level": 2,
            "score": 5,
		},
        {
			"userid": 103,
			"level": 1,
            "score": 2,
		}
	]
}

##############################################
######### Model for High Scores ##############
##############################################
high_scores = {
    "0" : 0,
    "1" : 5
}


#####################################################
############# 4.1 Login and Auth Key ################
#####################################################


@application.route('/<int:currentUserId>/login/', methods=['GET'])
def login_function(currentUserId):

    # If user exists, generate and issue token for the user for 10mins
    # Else , Append user to our temporary user_model and issue token for 10mins
    if check_if_user_exists(currentUserId):
        access_token = create_access_token(identity=currentUserId, expires_delta=dt.timedelta(seconds=600))
        return jsonify({currentUserId : access_token})
    else:
        newUser = {"userid": currentUserId, "level": 0, "score": 0}
        user_model['users'].append(newUser)
        access_token = create_access_token(identity=currentUserId, expires_delta=dt.timedelta(seconds=600))
        return jsonify({currentUserId : access_token})


############################################################
############# 4.2 Post Users score to Level ################
############################################################

@application.route('/<int:levelid>/score', methods=['POST'])
@jwt_required
def post_scores(levelid):

    currentUser = get_jwt_identity()

    #currentUser = 100 

    score_data = request.get_json()

    if check_if_level_exists_for_user(currentUser, levelid):

        for item in user_model['users']:
            if (item['userid'] == currentUser and item['level'] == levelid):
                
                # Update High score if posted score is more than current high score.
                if score_data['score'] > high_scores.get(str(levelid)):
                    newHighScore = {str(levelid) : score_data['score']}
                    high_scores.update(newHighScore)

                # Update our temporary data strucuture with new entry.
                item.update({"userid": currentUser, "level": levelid, "score": score_data['score']})

        return jsonify({"status" : "Score Updated for the user"})    
        
        # Else if User and Level does not exist,
    else:
        # As there is no entry for this level and user, the posted score will be an highscore.
        newHighScore = {str(levelid) : score_data['score']}
        high_scores.update(newHighScore)

        # Append the new entry in the list.
        newScore = {"userid": currentUser, "level": levelid, "score": score_data['score']}
        user_model['users'].append(newScore)

        return jsonify({"status" : "Created level and added Score for user"})



############################################################
#############   4.3 Retrieve High Scores      ##############
############################################################

@application.route('/<int:levelid>/highscorelist', methods=['GET'])
@jwt_required
def get_high_scores(levelid):
    
    high_score_user = 0 
    for item in user_model['users']:
        print (item['score'])
        if (item['level'] == levelid and item['score'] == high_scores.get(str(levelid))):
            high_score_user = item['userid']
        
    if high_score_user:
        return {"user": high_score_user, "score": high_scores.get(str(levelid))}
    else:
        return {"status": "High Score is still 0"}



############################################################
#############   4.4 Get our User model    ##############
############################################################
@application.route('/get_user_model', methods=['GET'])
def get_user_model():
    return jsonify(user_model)
    


##########################
#### Common Functions#####
##########################

# Function to check if user exists in our temporary user_model
def check_if_user_exists(currentUserId):
    for users in user_model['users']:
        #print(users['userid'])
        if currentUserId == users['userid']:
            return True
    return False

# Function to check if level already exists in our temporary user model for a given user
def check_if_level_exists_for_user(userid, level):
    for users in user_model['users']:
        if userid == users['userid']:
            if users['level'] == level:
                return True
        else:
            pass
    return False

