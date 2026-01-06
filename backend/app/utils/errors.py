from fastapi import HTTPException, status

def not_found(resource: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource} not found"
    )

def bad_request(msg: str):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=msg
    )