
import uvicorn
from pysvc.entrypoints.rest import server


def run() -> None:
    uvicorn.run(server.run(), host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()





