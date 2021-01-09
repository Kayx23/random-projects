from flask import Flask, request
from redis import Redis
from rq import Queue
import time  # to create a delay with time.sleep()

app = Flask(__name__)

q = Queue(connection=Redis())


def background_task(n):
    delay = 2
    print("Task running")
    print(f"Simulating {delay} second delay")
    time.sleep(delay)
    print(len(n))
    print("Task complete")
    return len(n)


@app.route('/')
def hello():

    if request.args.get("n"):
        # i.g. http://localhost:5000/?n=whatever
        job = q.enqueue(background_task, request.args.get("n"))
        return f"Task {job.id} added to queue at ({job.enqueued_at}). {len(q)} tasks in the queue"
    return "No value for n"