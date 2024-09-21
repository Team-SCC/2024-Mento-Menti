from fastapi import FastAPI

app = FastAPI()     # FastAPI 객체 생성

# @ - 아래 코드를 명시
@app.get("/")       # CRUD 사용 시 여러 방식 중에 get 형식으로 request
async def root():
    return {"message": "Hello World"}

'''
@app.get("/{num_int}")   # 주소창의 / 뒤 숫자에 따라 다른 값을 출력
async def number_function(num_int: float) -> dict:
    response = {
        "status": "success",
        "number": num_int
    }
    
    return response
'''

'''
@app.get("/{num_float}")   # 주소창의 / 뒤 숫자에 따라 다른 값을 출력
async def float_function(num_float: float) -> dict:
    response = {
        "status": "success",
        "number": num_float
    }
    
    return response
'''

'''
@app.get("/{string}")   # 주소창의 / 뒤 문자에 따라 다른 값을 출력
async def string_function(string: str) -> dict:
    response = {
        "status": "success",
        "string": string
    }
    
    return response
'''

if __name__ == "__main__":
    import uvicorn   
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload = True)