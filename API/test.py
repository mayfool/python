from douyu.chat.room import ChatRoom

def on_chat_message(msg):
    print( '[%s]:%s' % (msg.attr('nn'), msg.attr('txt')))

def run():
    room = ChatRoom('70068')
    room.on('chatmsg', on_chat_message)
    room.knock()

if __name__ == '__main__':
     run()