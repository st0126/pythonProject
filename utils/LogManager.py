import atexit
from datetime import datetime
from utils.TestInfo import TestInfo
from slack_sdk import WebClient


txt_log = []
txt_error_log = []


def log(test_id: str, test_result: bool, comment=''):
    if test_result:
        temp_log = f"{test_id} : [PASS] {comment}"
    else:
        temp_log = f"{test_id} : [FAIL] {comment}"

    print(temp_log)
    txt_log.append(temp_log)

    if not test_result:
        txt_error_log.append(temp_log)


def send_msg(msg, file_name):
    client = WebClient(token=TestInfo.SLACK_BOT_TOKEN)

    client.files_upload_v2(
        # 파일 전송은 채널명 말고 코드 사용
        channel=TestInfo.SLACK_CHANNEL_CODE,
        file=file_name,
        initial_comment=msg
    )


def save_log():
    line = "\n"
    daytime = datetime.today()

    file_log = f"logs/log_{daytime.strftime('%y%m%d_%H%M%S')}.txt"
    file_errorlog = f"logs/errorlog_{daytime.strftime('%y%m%d_%H%M%S')}.txt"

    a_log = line.join(txt_log)
    e_log = line.join(txt_error_log)

    msg = f"{daytime.strftime('%y.%m.%d')} GVW 모니터링 로그(방승태) \n 테스트 케이스 수 : {len(txt_log)} \n 에러 케이스 수: {len(txt_error_log)}"

    if len(txt_log) > 0:
        fs = open(file_log, "w")
        fs.write(a_log)
        fs.close()
        if TestInfo.SEND_REPORT and not TestInfo.REPORT_ERROR_ONLY:
            send_msg(msg, file_log)

    if len(txt_error_log) > 0:
        fs = open(file_errorlog, "w")
        fs.write(e_log)
        fs.close()
        if TestInfo.SEND_REPORT and TestInfo.REPORT_ERROR_ONLY:
            send_msg(msg, file_errorlog)


# 프로그램 종료 시점에 로그 저장
atexit.register(save_log)

