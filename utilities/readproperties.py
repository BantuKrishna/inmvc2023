import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def gettitle():
        title = config.get('common info','title')
        return title

    @staticmethod
    def getdesc():
        desc = config.get('common info','desc')
        return desc

    @staticmethod
    def getmeetlink():
        meetlink = config.get('common info','meetlink')
        return meetlink

    @staticmethod
    def getadd():
        add = config.get('common info','add')
        return add