from os import environ


class TestInfo:
    URL = {
        'MAIN': 'https://gvw-qa.illuminarean.com/',
        'LOGIN': "https://gvw-qa.illuminarean.com/login",
        'MY_PAGE' : "https://gvw-qa.illuminarean.com/my-page"
    }

    userInfo = {
        'privateID': 'seungtae.bang@illuminarean.com',
        'privatePW': '!qkdtmd753'
    }



    SEND_REPORT = True
    REPORT_ERROR_ONLY = False

    # test
    SLACK_BOT_TOKEN = "xoxb-6002864500356-5985888273975-h5Zq1tGPxsSMjQkpMqnpfV3i"
    SLACK_CHANNEL_NAME = 'gvw-test-bang'
    SLACK_CHANNEL_CODE = 'C065517QQJD'
