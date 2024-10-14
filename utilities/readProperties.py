import configparser


config = configparser.ConfigParser()
config.read("C:/Users/91990/PycharmProjects/python-selenium-automation/Configurations/config.ini")


# print(config.getuserEmail())


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        baseURL = config.get('common info', 'baseURL')
        return baseURL

    @staticmethod
    def getuserEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getuserPassword():
        password = config.get('common info', 'password')
        return password


# print(ReadConfig.getuserEmail())
# with open("C:/Users/91990/PycharmProjects/python-selenium-automation/Configurations/config.ini", 'r') as f:
#     print(f.read())
