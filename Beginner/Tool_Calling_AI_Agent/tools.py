from datetime import datetime


def get_time():

    return {
        "status": "success",
        "time": str(datetime.now())
    }


def add(a, b):

    return {
        "status": "success",
        "result": a + b
    }


def multiply(a, b):

    return {
        "status": "success",
        "result": a * b
    }