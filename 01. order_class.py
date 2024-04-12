class Customer:
    def __init__(self, name : str, address: str) -> None:
        self.__name = name
        self.__address = address

    def __str__(self) -> str:
        return f"customer name={self.__name}, address={self.__address}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Customer):
            return self.__name == __value.__name
        else:
            return False
        
class Product:
    def __init__(self, productid: int, product_name: str, price:float) -> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price

    @property
    def productid(self) -> float:
        return self.__productid

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price) -> None:
        self.__price = price

    def __str__(self) -> str:
        return f" Product id={self.__productid}, product name={self.__product_name}, price={self.__price}"

    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Product):
            return self.__productid == __value.__productid
        else:
            return False

class orderitem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity
    
    def get_total(self) -> float:
        return self.__product.price * self.__quantity
    
    @property
    def product(self) -> Product:
        return self.__product
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity) -> None:
        self.__quantity = quantity

    def __str__(self) -> str:
        return f"Order Item: product={self.__product}, quantity={self.__quantity}"
    
    def __repr__(self) -> str:
        return "\n" + str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, orderitem):
            return self.__product == __value.__product
        else:
            return False


class Order:
    def __init__(self, orderid: int, customer: Customer) -> None:
        self.__orderid = orderid
        self.__customer = customer


        # List of order items
        self.__order_items: list[orderitem] = []

    def add_item(self, product: Product, quantity: int) ->None:
    # check if item is in the list of order item
        found = False
        for item in self.__order_items:
            if item.product == product:
                item.quantity += quantity
                found = True
                break
        if found is False:
            self.__order_items.append(orderitem(product, quantity))

    def remove_item(self, productid: int) -> None:
    # findthe itemand then remove it
        for i in range(len(self.__order_items)):
            if self.__order_items[i].product.productid == productid:
                self.__order_items.pop(i)
                break

    def find_largest_item(self) -> orderitem:
        max: orderitem = self.__order_items[0]
        for item in self.__order_items:
            if item.get_total() > max.get_total():
                max = item
        return max

    def get_total(self) -> float:
        total = 0
        for item in self.__order_items:
            total += item.get_total()
        return total

#example, discounted_rate is 20% off
    def get_discount_value(self, discounted_rate: float) -> float:
        return self.get_total() * (100-discounted_rate) / 100

    def __str__(self) -> str:
        return f"order orderid={self.__orderid}, customer={self.__customer}\norder items:{self.__order_items}"

    def __repr__(self) ->str:
        return str(self)

    def __eq__(self,__value: object) -> bool:
        if isinstance(__value, Order):
            return self.__orderid == __value.__orderid
        else:
            return False


def main():
    p1 = Product(111, "Hammer\t", 25.99)
    p2 = Product(222, "Screw Driver\t", 15.99)
    p3 = Product(333, "Saw\t", 28.99)
    c = Customer("Peter", "123 Mission Blvd")
    

    order = Order(1234, c)
    order.add_item(p1, 100)
    order.add_item(p2, 200)
    order.add_item(p3, 300)
    order.add_item(p1, 250)

    # print(order)
    # order.remove_item(222)
    
    print(f"====== Initail Order ======\n{order}")
    order.remove_item(222)
    print (f"\n===== Order Details after remove items =====\n{order}")

    print("\n==>The larget item:\n", order.find_largest_item())
    print("\n===== Price Calculation =====\nThe original total:", order.get_total())
    print("The discount total:", order.get_discount_value(20))

if __name__ == "__main__":
    main()