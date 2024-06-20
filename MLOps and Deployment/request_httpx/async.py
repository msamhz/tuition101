import asyncio
import httpx

results = [] 


async def log_request(request):
    print(F"Requesting {request.url!r} {request.method}")
    
async def log_response(response):
    request = response.request
    print(f"Response: {request.method} {request.url!r} - {response.status_code}")
    

async def get_episode(ep_id: int): 
    async with httpx.AsyncClient(event_hooks= {'request': [log_request], 'response': [log_response]}) as client:
        response = await client.get(f"https://rickandmortyapi.com/api/episode/{ep_id}")
        results.append(response.json()['url'])
        return 
    
async def main():
    tasks = []
    for ep_id in range(1, 11):
        tasks.append(get_episode(ep_id))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    print(results)
    print(len(results))
    
    
    
    
    