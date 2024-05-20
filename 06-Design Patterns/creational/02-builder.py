class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None

    def __str__(self):
        return f"Part A: {self.part_a}, Part B: {self.part_b}, Part C: {self.part_c}"


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_b = "Part B"

    def build_part_c(self):
        self.product.part_c = "Part C"

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


# Client code
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_result()
print(product)