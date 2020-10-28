class ClientConfig(object):
    #public key for py updater (option)
    PUBLIC_KEY = 'pyupdater key HERE'
    #name will show on window title
    APP_NAME = 'Login Base' 
    #version show next to name
    APP_VERSION = '1.0.0' 
    #developer name on file info
    COMPANY_NAME = 'Buck and Moncey Devs' 
    HTTP_TIMEOUT = 30
    MAX_DOWNLOAD_RETRIES = 3
    #S3Bucket remove the "FirebaseprojectName" replace with your project name (option if you use pyupdater)
    UPDATE_URLS = ['https://FirebaseprojectName.s3.us-east-2.amazonaws.com'] 