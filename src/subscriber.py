import json

from constants import PUB_SUB_PROJECT_ID, PUB_SUB_CREDS_JSON, SUBSCRIBER
from google_pubsub import GooglePubSub
from logger import log


class Subscriber(GooglePubSub):
    def __init__(self, project_id, creds_json_path):
        super(Subscriber, self).__init__(project_id, creds_json_path)

    def call_back_method(self, message):
        log("Called subscriber callback")

        try:
            try:
                pub_message = message.data and json.loads(message.data)
            except ValueError:
                pub_message = message.data

            if pub_message:
                print pub_message
            else:
                log("No message found")

            log("Subscriber callback successful")
        except Exception as e:
            log("Error occurred in subscriber : {0}  {1}".format(e, message))
        finally:
            message.ack()


if __name__ == '__main__':
    sub_obj = Subscriber(PUB_SUB_PROJECT_ID, PUB_SUB_CREDS_JSON)
    sub_obj.run_subscriber_as_service(SUBSCRIBER)
