from fastapi.responses import (
    JSONResponse
)


async def generic_exception_handler(
    request,
    exc
):

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc)
        }
    )