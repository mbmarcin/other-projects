import requests
import pandas as pd
import datetime


def get_list_repos(lang: str = 'python') -> pd.DataFrame:
    """
    Get info from GitHub about repos by language.
    """
    today = datetime.date.today()
    y = int(today.year)

    url = f'https://api.github.com/search/repositories?q=language:{lang}&sort=stars&order=desc'

    res = requests.get(url)
    res_dict = res.json()

    repos = res_dict['items']
    # print(len(repos))

    del res_dict['items']
    # print(res_dict)

    repo_df = pd.DataFrame(repos)

    repo_df = repo_df[
        ['name', 'full_name', 'html_url', 'created_at', 'stargazers_count', 'watchers', 'forks', 'open_issues',
         'language']]
    repo_df['created_at'] = pd.to_datetime(repo_df['created_at'])
    repo_df['created_year'] = repo_df['created_at'].dt.year
    repo_df['years_on_github'] = y - repo_df['created_at'].dt.year

    return repo_df


#df = get_list_repos()

if __name__ == "__main__":
    print(get_list_repos())
