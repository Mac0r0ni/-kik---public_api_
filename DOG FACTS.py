if chat_message.body.lower() == "dog facts":
            try:
                url = "https://dog-api.kinduff.com/api/facts"  "?fields=facts,query"
                response = requests.get(url).json()
                client.send_chat_message(chat_message.from_jid,
                                         "Dog Fact:" '\n\n' + "Dog Fact: " + str(
                                             response['facts']))
