from constants import PUB_SUB_PROJECT_ID, PUB_SUB_CREDS_JSON, TOPIC
from google_pubsub import GooglePubSub


class Publisher(GooglePubSub):
    def __init__(self, project_id, creds_json_path):
        super(Publisher, self).__init__(project_id, creds_json_path)

    def call_back_method(self):
        pass


if __name__ == '__main__':
    pub_obj = Publisher(PUB_SUB_PROJECT_ID, PUB_SUB_CREDS_JSON)

    pub_obj.publish(TOPIC, "This is a new message")
