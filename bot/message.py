import requests

# This is the token that you generate for the page hooked up to your bot
params = {
    'access_token': "<REPLACE WITH YOUR PAGE ACCESS TOKEN!!!!>"
}

# Messenger request URL
url = "https://graph.facebook.com/v2.8/me/messages"

"""
    Messenger sends us batches of messages. Thus, the payload that we receive
    will have the following structure:

    {
      "object":"page",
      "entry":[
        {
          "id":"PAGE_ID",
          "time":1458692752478,
          "messaging":[
            {
              "sender":{
                "id":"USER_ID"
              },
              "recipient":{
                "id":"PAGE_ID"
              },
              "timestamp":1458692752478,
              "message":{
                "mid":"mid.1457764197618:41d102a3e1ae206a38",
                "text":"hello, world!",
              }
            }
            ...
          ]
        }
      ]
    }

    We see that "entry" is an array containing event data (interactions
        that our bot experiences).
    Each entry contains a "messaging" field, which is an array of
        objects related to messaging. In this bot, however, we will only
        handle receiving text messages. Thus, each "messaging" object will have
        a "text" field.
"""


def handle_entries(payload):
    """handle_entries

    This is the main handling function for responding to message entries.

    Ref: https://developers.facebook.com/docs/messenger-platform/webhook-reference
    """
    pass


def handle_message(message):
    """handle_message

    This function will handle and respond to messages.

    Note that the 'message' parameter will have the following structure:
        {
          "sender":{
            "id":"USER_ID"
          },
          "recipient":{
            "id":"PAGE_ID"
          },
          "timestamp":1458692752478,
          "message":{
            "mid":"mid.1457764197618:41d102a3e1ae206a38",
            "text":"hello, world!",
          }
        }
    """
    pass


def send_message(text, recipient):
    """send_message

    This function will send a text message to the recipient.

    Messenger expects the following format:

    {
      "recipient":{
        "id":"USER_ID"
      },
      "message":{
        "text":"hello, world!"
      }
    }

    Ref: https://developers.facebook.com/docs/messenger-platform/send-api-reference
    """
    pass
