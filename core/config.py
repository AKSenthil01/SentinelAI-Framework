import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

def get_base_url(env="DEFAULT"):
    return config[env]["base_url"]