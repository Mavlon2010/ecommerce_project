import json

import requests

from bot.app import WEB_URL


class BotAPI:
    def __init__(self):
        self.categories = f'{WEB_URL}/api/v1/category/'
        self.subcategory = f'{WEB_URL}/api/v1/subcategory/'
        self.products = f'{WEB_URL}/api/v1/product/'

    def json_loads(self, url):
        return json.loads(requests.get(url).text)

    def get_categories(self, cat_id=None):
        if cat_id:
            url = f"{self.categories}{cat_id}"
            return self.json_loads(url)

        return self.json_loads(self.categories)

    def get_subcateogries(self, sub_id=None):
        if sub_id:
            url = f"{self.subcategory}{sub_id}"
            return self.json_loads(url)

    def get_product(self, prod_id=None):
        if prod_id:
            url = f"{self.products}{prod_id}"
            return self.json_loads(url)

    def create_order(product_id, quantity, user_id):
        # Bu yerda APIga so'rov yuborish logikasi
        # Misol uchun:
        # response = requests.post(
        #     f"{BASE_URL}/orders/",
        #     json={"product": product_id, "quantity": quantity, "user": user_id}
        # )
        # return response.json()
        pass


api_response = BotAPI()

if __name__ == '__main__':
    api_response = BotAPI()
    print(api_response.get_categories(1))
