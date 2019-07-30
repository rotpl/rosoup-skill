from mycroft import MycroftSkill, intent_file_handler


class Rosoup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rosoup.intent')
    def handle_rosoup(self, message):
        abrv = message.data.get('abrv')

        self.speak_dialog('rosoup', data={
            'abrv': abrv
        })


def create_skill():
    return Rosoup()

