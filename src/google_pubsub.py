import json
import os
import time
import types
from abc import ABCMeta, abstractmethod

from google.cloud import pubsub_v1

from constants import *
from logger import log


class GooglePubSub:
    __metaclass__ = ABCMeta

    def __init__(self, project_id, creds_json):
        os.environ[PUB_SUB_CREDS_ENV_KEY] = creds_json

        self.project_id = project_id
        self.publisher_client = pubsub_v1.PublisherClient()
        self.subscriber_client = pubsub_v1.SubscriberClient()

    def publish(self, topic_name, message):
        if not message:
            log("Message passage is empty")
            return

        if not topic_name:
            raise Exception("Topic name is required")

        topic = TOPIC_PATH.format(project_id=self.project_id, topic_name=topic_name)

        if types.StringType != type(message):
            message = json.dumps(message, indent=1).encode('utf-8')

        self.publisher_client.publish(topic, message)

        log("Successfully published the message")

    def subscriber(self, subscriber_name, call_back_method):
        subscriber_name = SUBSCRIBER_PATH.format(project_id=self.project_id, subscriber_name=subscriber_name)
        self.subscriber_client.subscribe(subscriber_name, call_back_method)

    @abstractmethod
    def call_back_method(self):
        pass

    def run_subscriber_as_service(self, subscriber_name):
        self.subscriber(subscriber_name, self.call_back_method)

        while True:
            log("Subscriber is waiting...")
            time.sleep(5)
