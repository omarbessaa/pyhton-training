from flask import Flask , abort , request
import shop

shop.Shop.add_product('ux nana ni nana na', ['yellow','red'], [], 'new product very great' , 20.3)
shop.Shop.add_category('test')
shop.Shop.add_product_to_category(1 , 1)

# the flask app
# start the app
app = Flask(__name__)

@app.route('/myshop' , methods = ['GET'])
def show_products() :
    products = shop.Shop.get_products()
    d = {}
    for product_id , product in products :
        d[product_id] = {
            'name' : product.name, 
            'colors' : product.colors, 
            'sizes' : product.sizes, 
            'description' : product.description ,
            'price' : product.price 
        }

    return str(d)

@app.route('/myshop/<int:product_id>' , methods = ['GET'])
def gt_product(product_id) :
    # product_id = int(product_id)
    if product_id in shop.Shop.PRODUCTS.keys() :
        product = shop.Shop.get_product(product_id)
        d = {}
        d[product_id] = {
                'name' : product.name, 
                'colors' : product.colors, 
                'sizes' : product.sizes, 
                'description' : product.description ,
                'price' : product.price 
            }

        return str(d)
    else :
        abort(404)

@app.route('/myshop/<int:product_id>' , methods = ['DELETE'])
def del_product(product_id) :
    # product_id = int(product_id)
    # products = shop.Shop.get_products()
    # ids = [key for key , product in products]
    if product_id in shop.Shop.PRODUCTS.keys() :
        shop.Shop.delete_product(product_id)
        return 'ok'
    else :
        abort(400)

# satrt running the app
app.run(debug = True)
