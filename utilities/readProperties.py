import configparser
# from Configurations import config

config = configparser.ConfigParser()
config.read('config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getuserEmail():
        email = config.get("common info", "email")
        return email

    @staticmethod
    def getuserPassword():
        password = config.get("common info", "password")
        return password
# import configparser
#
# config = configparser.ConfigParser()
# config.read('config.ini')
#
# baseURL = config.get('common info', 'baseURL')
# email = config.get('common info', 'email')
# password = config.get('common info', 'password')