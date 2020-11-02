import configparser

config = configparser.RawConfigParser()

config.read('.\\Configurations\\config.ini')

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'URL')
        return url
        
    @staticmethod
    def getApplicationgoogle_url():
        url = config.get('common info', 'google_url')
        return url