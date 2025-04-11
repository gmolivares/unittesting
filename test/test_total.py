def calculate_total(products,discount=None):
    total=0
    for product in products:
        total += product["price"]
    if discount is not None:
        return total*(discount/100)
    return total
    
def test_calculate_total_with_empty_list():
    assert calculate_total([])==0

def test_calculate_total_with_single_product():
    products=[{
        "name":"Notebook","price":5
    }]
    
    assert calculate_total(products,10) == 0.5

def test_calculate_total_with_multiple_product():
    products=[{
        "name":"Notebook","price":10
    },
    {
        "name":"Book","price":2
    }
    ]
    
    assert calculate_total(products) == 12

if __name__== "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()