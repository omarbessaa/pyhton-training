class Product():
    def __init__(self, name, colors, sizes, description , price) :
        #self.id = pid
        #self.typeid = ptypeid
        self.name = name
        self.description = description
        self.price = price
        self.colors = colors
        self.sizes = sizes

class Category() :
    def __init__ (self , name) :
        self.name = name
        self.items = []

class Shop() :

    PRODUCTS = {}
    CATEGORIES = {}

    @classmethod
    def add_product(cls, name, colors, sizes, description , price) :
        p = Product(name, colors, sizes, description , price)
        product_id = len(cls.PRODUCTS) + 1
        cls.PRODUCTS[product_id] = p

    @classmethod
    def add_category(cls , name) :
        c = Category(name)
        category_id = len(cls.CATEGORIES) + 1
        cls.CATEGORIES[category_id] = c

    @classmethod
    def add_product_to_category(cls, product_id , category_id) :
        if category_id in cls.CATEGORIES.keys() :
            cls.CATEGORIES[category_id].items.append(product_id)
        else :
            raise ValueError('id category doesn\'t exist')

    @classmethod
    def get_products(cls) :
        return list(cls.PRODUCTS.items())

    @classmethod
    def get_product(cls, product_id) :
        return cls.PRODUCTS[product_id]


    @classmethod
    def update_product(cls, product_id, **pars) :
        p = cls.PRODUCTS[product_id]
        for par in pars.keys() :
            setattr(p, par, pars[par])

    @classmethod
    def delete_product(cls, product_id) :
        cls.PRODUCTS.pop(product_id)
