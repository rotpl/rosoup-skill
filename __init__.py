from mycroft import MycroftSkill, intent_file_handler
import pickle
import cryptography


class Rosoup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        with open('/home/pi/fernet_key.txt', 'r', encoding='utf-8') as k:
            key = k.read()
        f = cryptography.Fernet(key)
        with open('/opt/mycroft/skills/rosoup-skill/enc_soup.pickle', 'r',
                encoding='utf-8') as k:
            token = f.decrypt(k.read().encode('utf-8'))
        self.soup = pickle.loads(token)

    @intent_file_handler('rosoup.intent')
    def handle_rosoup(self, message):
        abrv = message.data.get('abrv')
        response = self.soup[abrv]
        self.speak_dialog('rosoup', data={
            'abrv': abrv, 'response': response
        })


def create_skill():
    return Rosoup()
