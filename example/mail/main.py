from fastapi import FastAPI
prefix ="/mail"

app = FastAPI(title="mail API", description="mail API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

@app.get("/mail/")
async def root():
    return {'message': 'Hello World From mail'}
