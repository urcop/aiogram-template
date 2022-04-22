from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")
DB_HOST = env.str('ip')
DB_NAME = env.str('db_name')
DB_PASS = env.str('db_pass')
DB_USER = env.str('db_user')
DB_PORT = '5432'
