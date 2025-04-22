
import uvicorn
from pysvc.handlers.rest import server


def run() -> None:
    uvicorn.run(server.run(), host="localhost", port=8000)

if __name__ == "__main__":
    run()





