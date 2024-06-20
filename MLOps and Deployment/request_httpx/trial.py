import httpx 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://httpbin.org/headers'

with httpx.Client() as s:
    r = s.get(url, headers=headers)
    print(r.status_code,'\n', r.text)
