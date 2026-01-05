import httpx
import asyncio
import time
from django.http import HttpResponse

async def fetch_url(client, url):
    resp = await client.get(url)
    return resp.status_code

async def async_view(request):
    start_time = time.perf_counter()
    
    urls = ["https://httpbin.org/get" for _ in range(3)]
    
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    return HttpResponse(f"Resultados: {results} | Tempo total: {total_time:.2f} segundos")

def sync_view(request):
    start_time = time.perf_counter()
    
    results = []
    for _ in range(3):
        r = httpx.get("https://httpbin.org/get")
        results.append(r.status_code)
        
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    return HttpResponse(f"Resultados: {results} | Tempo total: {total_time:.2f} segundos")