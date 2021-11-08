import os
from datetime import datetime
from pytz import timezone
from crawling_dollor import parsing_bs, extract_data
from github_utils import get_github_repo, upload_github_issue


if __name__=="__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repo_name = 'git_action_study'

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    
    dollor_url = "https://finance.naver.com//marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page=1"

    soup = parsing_bs(dollor_url)

    issue_title = f"{today_date}  환율 정보"
    upload_contents = extract_data(soup)
    
    repo = get_github_repo(access_token, repo_name)
    upload_github_issue(repo, issue_title, upload_contents)
    
    print("Success")



