import random
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def visit_pages(self):
        urls = [
            "/index.php/shop/page/1322/",
            "/index.php/product/fugiat-14/",
            "/index.php/shop/page/1322/?add-to-cart=94808",
            "/index.php/shop/page/322/",
            "/index.php/product/autem-non-3/",
            "/index.php/shop/page/322/?add-to-cart=319488",
            "/index.php/shop/page/52/",
            "/index.php/product/ad-et-ab/",
            "/index.php/shop/page/52/?add-to-cart=94881",
            "/index.php/shop/page/198/",
            "/index.php/product/at-nulla/",
            "/index.php/shop/page/198/?add-to-cart=335343",
            "/index.php/shop/page/450/",
            "/index.php/product/cumque-5/",
            "/index.php/shop/page/450/?add-to-cart=90653",
            "/index.php/shop/page/866/",
            "/index.php/product/eos-172/",
            "/index.php/shop/page/866/?add-to-cart=319204",
            "/index.php/shop/page/1042/",
            "/index.php/product/et-non-10/",
            "/index.php/shop/page/1042/?add-to-cart=294423",
            "/index.php/shop/page/1311/",
            "/index.php/product/fuga-147/",
            "/index.php/shop/page/1311/?add-to-cart=331924",
            "/index.php/shop/page/1631/",
            "/index.php/product/iusto-22/",
            "/index.php/shop/page/1631/?add-to-cart=97245",
            "/index.php/shop/page/2431/",
            "/index.php/product/qui-iure-4/",
            "/index.php/shop/page/2431/?add-to-cart=307961",
            "/index.php/cart/",
            "/index.php/checkout/",
        ]

        for url in urls:
            self.client.get(url)