from read_config import ConfigRead

config_read_obj = ConfigRead('config', 'config.ini')
pub_sub_config = config_read_obj.get_config_section('PUSUB_SETTINGS')

PUB_SUB_PROJECT_ID = pub_sub_config.get('project_name')
TOPIC = pub_sub_config.get('topic_name')
SUBSCRIBER = pub_sub_config.get('subscription_name')
PUB_SUB_CREDS_JSON = pub_sub_config.get('cred_json_file_path')
PUB_SUB_CREDS_ENV_KEY = 'GOOGLE_APPLICATION_CREDENTIALS'

TOPIC_PATH = "projects/{project_id}/topics/{topic_name}"
SUBSCRIBER_PATH = "projects/{project_id}/subscriptions/{subscriber_name}"
