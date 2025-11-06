from data.common import CommonUrls


class OrderData:
    ORDER_CREATE_URL = (f"{CommonUrls.MAIN_API_URL}/orders", "POST")
    ORDER_CREATE_NO_INGREDIENT_ERROR_400 = {
        "success": False,
        "message": "Ingredient id must be provided",
    }
    # ingredients key
    # name, order/number, success: True
    # 500 ingredients not exists
    # 400 ingredients not present

    # not auth redirect to login.
    # auth set headers
    # auth redirect to /
