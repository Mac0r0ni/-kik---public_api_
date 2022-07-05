if chat_message.body.lower() == "cat facts":                                       # this check to see if the message recieved is the trigger "cat facts"
            try:
                url = "https://meowfacts.herokuapp.com/"  "?fields=data,query"    # opens up the MEOW FACTS api
                response = requests.get(url).json()                               # This request the content from the meow facts website that was called above.
                client.send_chat_message(chat_message.from_jid,                    # This sends the message to the user who called it!
                                         "Cat Fact:\n\n" + str(
                                             response['data']))
