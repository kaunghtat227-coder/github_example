from product import Product

class StoreFront:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n--- Store Menu ---")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Exit")

            choice = input("Choose an option (1/2/3/4/5): ")

            if choice == '1':
                products = self.manager.get_products()
                if not products:
                    print("No products available.")
                else:
                    for i, p in enumerate(products):
                        print(f"[{i}] Name: {p.name}, Price: {p.price}")

            elif choice == '2':
                name = input("Enter product name: ")
                try:
                    price = int(input("Enter product price: "))
                    new_product = Product(name, price)
                    msg = self.manager.create_product(new_product)
                    print(msg)
                except ValueError:
                    print("Please enter a valid number for the price.")

            elif choice == '3':
                products = self.manager.get_products()
                if not products:
                    print("No products available to update.")
                    continue
                
                # Show existing products first
                for i, p in enumerate(products):
                    print(f"[{i}] Name: {p.name}, Price: {p.price}")
                
                try:
                    index = int(input("Enter the product number [ ] to update: "))
                    if 0 <= index < len(products):
                        new_name = input("Enter new product name: ")
                        new_price = int(input("Enter new product price: "))
                        msg = self.manager.update_product(index, new_name, new_price)
                        print(msg)
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter valid numbers for index and price.")

            elif choice == '4':
                products = self.manager.get_products()
                if not products:
                    print("No products available to delete.")
                    continue
                
                for i, p in enumerate(products):
                    print(f"[{i}] Name: {p.name}, Price: {p.price}")
                
                try:
                    index = int(input("Enter the product number [ ] to delete: "))
                    msg = self.manager.delete_product(index)
                    print(msg)
                except ValueError:
                    print("Please enter a valid number for the index.")

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
