memory = []


def add(a, b):

    result = a + b

    operation = f"{a} + {b}"

    memory.append(
        {
            "operation": operation,
            "result": result
        }
    )

    return {
        "status": "success",
        "operation": operation,
        "result": result
    }


def subtract(a, b):

    result = a - b

    operation = f"{a} - {b}"

    memory.append(
        {
            "operation": operation,
            "result": result
        }
    )

    return {
        "status": "success",
        "operation": operation,
        "result": result
    }


def multiply(a, b):

    result = a * b

    operation = f"{a} * {b}"

    memory.append(
        {
            "operation": operation,
            "result": result
        }
    )

    return {
        "status": "success",
        "operation": operation,
        "result": result
    }


def divide(a, b):

    if b == 0:

        return {
            "status": "error",
            "message": "Cannot divide by zero"
        }

    result = a / b

    operation = f"{a} / {b}"

    memory.append(
        {
            "operation": operation,
            "result": result
        }
    )

    return {
        "status": "success",
        "operation": operation,
        "result": result
    }


def show_memory():

    return {
        "status": "success",
        "memory": memory
    }