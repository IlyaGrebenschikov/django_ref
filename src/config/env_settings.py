import os

from dotenv import load_dotenv, find_dotenv


env_file = find_dotenv()
load_dotenv(env_file)

ENV_SECRET_KEY = os.environ.get('SECRET_KEY')

ENV_POSTGRES_USER = os.environ.get('POSTGRES_USER')
ENV_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
ENV_POSTGRES_DB = os.environ.get('POSTGRES_DB')
ENV_POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
ENV_POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
