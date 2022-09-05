from fastapi import FastAPI
prefix ="/sms"

app = FastAPI(title="sms API", description="sms API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

@app.get("/sms/")
async def root():
    return {'message': 'Hello World From sms'}
