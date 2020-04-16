import requests
import os
import json

class RocketChatLiveChatMessages:

    def __init__(self, api_url, visitor_token, platform):
        self.api_url = api_url
        self.token = visitor_token
        self.platform = platform

    # def create_visitor_get_room(self, name, username, platform):
        # # Checking if already exists room for this visitor
        # check_file = os.path.isfile('/tmp/'+self.token+'.session')
        # if check_file:
        #     f = open('/tmp/'+self.token+'.session', "r")
        #     if f.mode == 'r':
        #         room_id = f.read()
        #         if room_id != "":
        #             # Return Room ID if exists
        #             return room_id        
        #         else:
        #             print("Failure to read room_id")
        #             exit(code=1)
        # else:
            # body = { "visitor": { "name":name, "token":str(self.token), "username":username, 
            #                 "customFields": [{ "key": "platform", "value":self.platform, "overwrite": True }] }}
            # headers = {'Content-Type': 'application/json'}
            # # Getting Visitor
            # r = requests.post(url=self.api_url+'/api/v1/livechat/visitor', headers=headers, json=body)
            # json_visitor = json.loads(r.content) 
            # if json_visitor['success'] == True:
            #     # Getting Room
            #     r = requests.get(url=self.api_url+'/api/v1/livechat/room?token='+self.token)   
            #     json_room = json.loads(r.content)
            #     if json_room['success'] == False:
            #         print(json_room)
            #         exit(code=1)
            #     else:
            #         room_id = json_room['room']['_id']
            #         f = open('/tmp/'+self.token+'.session', "w")
            #         f.write(room_id)
            #         f.close
            #         return room_id
            # else:
            #     print(json_visitor)
            #     exit(code=1)

    def send_message(self,rid,message):
        body = { "token": str(self.token), "rid": str(rid), "msg": message }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=self.api_url+'/api/v1/livechat/message', headers=headers, json=body)
        json_message = json.loads(r.content)
        if json_message['success'] == False:
            print(json_message)
            exit(code=1)
        else:
            return json_message

