from project.product import Product

class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for x in self.products:
            if x.name == product_name:
                return x

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
