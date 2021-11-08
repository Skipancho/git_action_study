import os
from datetime import datetime
from pytz import timezone
from crawling_exchange import parsing_bs, extract_data
from github_utils import get_github_repo, upload_github_issue

dollor_url = "https://finance.naver.com//marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page=1"
jpy_url = "https://finance.naver.com//marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_JPYKRW&page=1"

urls = [dollor_url, jpy_url]
labels = ["US 달러","일본 엔"]


if __name__=="__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repo_name = 'git_action_study'

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    upload_contents = '출처 - <a href = "https://finance.naver.com/">네이버 금융</a>'
    
    issue_title = f"{today_date}  환율 정보"
    
    for i, url in enumerate(urls):
        soup = parsing_bs(url)
        contents = extract_data(soup)
        label = labels[i]

        upload_contents = f"{upload_contents}\n{label} - {contents}"
    
    repo = get_github_repo(access_token, repo_name)
    upload_github_issue(repo, issue_title, upload_contents)
    
    print("Success")



