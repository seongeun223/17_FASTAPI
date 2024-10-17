from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수
# 웹 어플리케이션에서 URL 경로의 일부로 사용된다.
# 보통 클라이언트에서 서버에 요청할 때 특정 자원을 식별하는데 사용되는 값

@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}

# 타입이 있는 매개변수
# 파이썬 표준 타입을 사용할 수 있다.

@app.get('/items/type/{item_id}')
async def read_item_type(item_id: int):
    return {"item_id" : item_id}