from icecream import ic

def my_method(request, request_data):
    ic(request, request_data)
    for header_name, header_value in request.headers.items():
        ic(header_name, header_value)
    ic("This is supposed to run before grpc method call")
    # Modify the password in request_data
    request_data["password"] = "Password@123"
