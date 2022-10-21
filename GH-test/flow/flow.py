from prefect import flow, task


@task
def do_something():
    print("something")


@flow
def myflow():
    do_something()


if __name__ == "__main__":
    myflow()
