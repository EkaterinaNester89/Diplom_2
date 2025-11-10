from data.common import CommonUrls


class OrderData:
    ORDER_CREATE_URL = (f"{CommonUrls.MAIN_API_URL}/orders", "POST")
    ORDER_CREATE_NO_INGREDIENT_ERROR_400 = {
        "success": False,
        "message": "Ingredient ids must be provided",
    }
