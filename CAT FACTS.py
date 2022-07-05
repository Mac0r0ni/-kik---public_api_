if chat_message.body.lower() == "cat facts":                                 
            try:
                url = "https://meowfacts.herokuapp.com/"  "?fields=data,query"    
                response = requests.get(url).json()                               
                client.send_chat_message(chat_message.from_jid,                   
                                         "Cat Fact:\n\n" + str(
                                             response['data']))
