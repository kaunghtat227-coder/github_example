from product import Product


class StoreFront:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n--- Store Menu ---")
            print("1. View Products (ပစ္စည်းများကြည့်ရန်)")
            print("2. Add Product (ပစ္စည်းအသစ်ထည့်ရန်)")
            print("3. Exit (ထွက်ရန်)")

            choice = input("ရွေးချယ်ပါ (1/2/3): ")

            if choice == '1':
                products = self.manager.get_products()
                if not products:
                    print("ကုန်ပစ္စည်း မရှိသေးပါ။")
                else:
                    for i, p in enumerate(products):
                        print(f"[{i}] Name: {p.name}, Price: {p.price}")

            elif choice == '2':
                name = input("ပစ္စည်းအမည် ထည့်ပါ: ")
                price = int(input("ဈေးနှုန်း ထည့်ပါ: "))
                new_product = Product(name, price)
                msg = self.manager.create_product(new_product)
                print(msg)

            elif choice == '3':
                print("ပရိုဂရမ် ရပ်နားပါပြီ။")
                break

            else:
                print("မှားယွင်းနေပါသည်။ ပြန်ရွေးပါ။")