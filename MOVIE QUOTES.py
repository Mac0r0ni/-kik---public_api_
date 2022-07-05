 if chat_message.body.lower() == "show quote":
            try:
                url = "https://movie-quote-api.herokuapp.com/v1/quote/" + "?fields=quote,role,show,query"
                response = requests.get(url).json()
                client.send_chat_message(chat_message.group_jid,
                                         "Movie/Show Quote: " '\n\n' + "Quote: " + str(
                                             response['quote']) + '\n\n' + "Role: " + str(
                                             response['role']) + '\n\n' + "From movie/show: " + str(
                                             response['show']))
