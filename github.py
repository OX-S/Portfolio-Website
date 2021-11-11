import requests


class Github:

    @staticmethod
    def get_repo(owner, repo):
        token = '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'
        params = {
            "state": "open",
        }
        headers = {'Authorization': f'token {token}'}
        query_url = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.get(query_url, headers=headers, params=params)
        r.json()
        return r

    @staticmethod
    def get_language(r):
        return r.json()["language"]

    @staticmethod
    def get_stars(r):
        return r.json()["stargazers_count"]

    @staticmethod
    def get_forks(r):
        return r.json()["forks_count"]

    @staticmethod
    def get_name(r):
        return r.json()["name"]

    @staticmethod
    def get_desc(r):
        return r.json()["description"]
