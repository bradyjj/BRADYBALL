from ..celery_app import app

@app.task
def example_task():
    print("This is an example task for FBref service")