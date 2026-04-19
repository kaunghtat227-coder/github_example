from store_manager import StoreManager
from store_front import StoreFront

manager = StoreManager("products.txt")

front = StoreFront(manager)
front.run()
