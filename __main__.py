import os

if __name__ == "__main__":
    import uvicorn

    is_debug = os.getenv("DEBUG") == "True"

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        debug=is_debug,
        access_log=True,
        reload=is_debug,
    )
