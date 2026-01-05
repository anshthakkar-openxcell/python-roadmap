from fastapi import Header, HTTPException, status

async def verify_token(api_key: str = Header(...)):
    if api_key != "secret-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
