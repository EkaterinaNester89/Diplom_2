from data.common import CommonUrls


class UserData:
    USER_CREATE_URL = (f"{CommonUrls.MAIN_API_URL}/auth/register", "POST")

    USER_CREATE_ALREADY_EXISTS_ERROR_403 = {
        "success": False,
        "message": "User already exists",
    }
    USER_CREATE_MISSING_FIELD_ERROR_403 = {
        "success": False,
        "message": "Email, password and name are required fields",
    }
    USER_LOGIN_URL = (f"{CommonUrls.MAIN_API_URL}/auth/login", "POST")
    USER_LOGIN_MISSING_FIELD_ERROR_401 = {
        "success": False,
        "message": "email or password are incorrect",
    }
