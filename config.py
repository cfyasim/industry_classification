from pydantic import BaseSettings
import os

ROOT_DIR = os.path.join("..")


class BertClassifierSettings(BaseSettings):
    BERT_CLASSIFICATION_USERNAME: str = ''
    BERT_CLASSIFICATION_PASSWORD: str = ''
    INDUSTRY_MODEL_FILE_NAME = ''
    TOPIC_MODEL_FILE_NAME = ''
    INF_INDUSTRY_MODEL_FILE_NAME = ''
    INF_TOPIC_MODEL_FILE_NAME = ''
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'logs/cfy_bert_classification.log',
                'level': 'DEBUG',
                'formatter': 'simple',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 7
            },
        },
        'loggers': {
            '1': {
                'handlers': ['file_handler'],
                'level': 'DEBUG',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
        },
    }

    class Config:
        env_file = ".env"