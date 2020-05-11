from mycroft import MycroftSkill, intent_file_handler


class Feedshira(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('feedshira.intent')
    def handle_feedshira(self, message):
        self.speak_dialog('feedshira')


def create_skill():
    return Feedshira()

