import requests

api_key = ''
headers = {'X-Auth-Token': api_key}

# 获取所有比赛列表
url = 'https://api.football-data.org/v4/competitions/'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    competitions = response.json()['competitions']
    for comp in competitions:
        name = comp['name']
        comp_id = comp['id']
        # 打印包含 "World" 或 "Qual" 的比赛
        if 'World' in name or 'Qual' in name:
            print(f"ID: {comp_id}, Name: {name}, Area: {comp['area']['name']}")
else:
    print(f"Error: {response.status_code}")