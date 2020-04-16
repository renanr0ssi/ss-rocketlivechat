import requests
import json
from st2common.runners.base_action import Action

from sender.rc_livechat_sendMessage import RocketChatLiveChatMessages

class RCLiveChatSendMessageAction(Action):
    def run(self, visitor_token, name, platform, username, message):

        room_id = None

        session = self.action_service.get_value(platform + '.session.' + visitor_token, local=False)
        if session:
            session = json.loads(session)
            room_id = session['roomId']

        # Validating the Room ID
        if room_id:
            # rid=room_id
            pass
        else:
            body = { "visitor": { "name":name, "token":str(visitor_token), "username":username, 
                            "customFields": [{ "key": "platform", "value":platform, "overwrite": True }] }}
            headers = {'Content-Type': 'application/json'}
            # Getting Visitor
            r = requests.post(url=self.config['api_url']+'/api/v1/livechat/visitor', headers=headers, json=body)
            json_visitor = json.loads(r.content) 
            if json_visitor['success'] == True:
                # Getting Room
                r = requests.get(url=self.config['api_url']+'/api/v1/livechat/room?token='+visitor_token)   
                json_room = json.loads(r.content)
                if json_room['success'] == False:
                    print(json_room)
                    exit(code=1)
                else:
                    room_id = json_room['room']['_id']
                    # f = open('/tmp/'+self.token+'.session', "w")
                    # f.write(room_id)
                    # f.close
                    payload={"name": username, "roomId": room_id, "token": visitor_token}
                    self.action_service.set_value(name=platform + '.session.' + visitor_token, value=json.dumps(payload), ttl=None, local=False, encrypt=False)
                    # rid=room_id
            else:
                print(json_visitor)
                exit(code=1)

        livechat = RocketChatLiveChatMessages(api_url=self.config['api_url'],visitor_token=visitor_token,platform=platform)
        # rid = livechat.create_visitor_get_room(name=name,username=username,platform=platform)
        m = livechat.send_message(rid=room_id,message=message)
        return m
