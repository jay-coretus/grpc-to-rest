from icecream import ic

def my_method(request, request_data):
    ic(request, request_data, request.headers)
    ic("This is supposed to run before grpc method call")
    # Modify the password in request_data
    request_data["password"] = "WrongPassword@123"
    