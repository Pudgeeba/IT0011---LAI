class Pastry:
    def __init__(self, pastry_id, name, description, price):
        self.pastry_id = pastry_id
        self.name = name
        self.description = description
        self.price = price

class PastryInventory:
    def __init__(self):
        self.pastries = []

    def add_pastry(self):
        print("\n--- Add New Pastry ---")
        pastry_id = input("Enter Pastry ID: ")
        if self.find_pastry_by_id(pastry_id):
            print("❌ Pastry ID already exists. Try again.")
            return
        name = input("Enter Pastry Name: ")
        description = input("Enter Description: ")
        try:
            price = float(input("Enter Price: "))
            if price < 0:
                print("❌ Price cannot be negative.")
                return
        except ValueError:
            print("❌ Invalid price. Must be a number.")
            return

        new_pastry = Pastry(pastry_id, name, description, price)
        self.pastries.append(new_pastry)
        print("✅ Pastry successfully added!")

    def view_pastries(self):
        if not self.pastries:
            print("\nNo pastries available.")
            return
        print("\n--- Pastry Menu ---")
        print(f"{'ID':<10}{'Name':<20}{'Description':<30}{'Price':>10}")
        print("-" * 70)
        for pastry in self.pastries:
            print(f"{pastry.pastry_id:<10}{pastry.name:<20}{pastry.description:<30}{pastry.price:>10.2f}")

    def update_pastry(self):
        print("\n--- Update Pastry ---")
        pastry_id = input("Enter Pastry ID to update: ")
        pastry = self.find_pastry_by_id(pastry_id)
        if not pastry:
            print("❌ Pastry not found.")
            return
        pastry.name = input("Enter new Pastry Name: ")
        pastry.description = input("Enter new Description: ")
        try:
            new_price = float(input("Enter new Price: "))
            if new_price < 0:
                print("❌ Price cannot be negative.")
                return
            pastry.price = new_price
            print("✅ Pastry updated successfully!")
        except ValueError:
            print("❌ Invalid price input. Update cancelled.")

    def delete_pastry(self):
        print("\n--- Delete Pastry ---")
        pastry_id = input("Enter Pastry ID to delete: ")
        pastry = self.find_pastry_by_id(pastry_id)
        if pastry:
            self.pastries.remove(pastry)
            print("✅ Pastry deleted successfully!")
        else:
            print("❌ Pastry not found.")

    def find_pastry_by_id(self, pastry_id):
        return next((p for p in self.pastries if p.pastry_id == pastry_id), None)

def run_pastry_shop():
    inventory = PastryInventory()
    while True:
        print("\n====== Pastry Shop Inventory ======")
        print("[1] Add Pastry")
        print("[2] View Pastries")
        print("[3] Update Pastry")
        print("[4] Delete Pastry")
        print("[5] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            inventory.add_pastry()
        elif choice == '2':
            inventory.view_pastries()
        elif choice == '3':
            inventory.update_pastry()
        elif choice == '4':
            inventory.delete_pastry()
        elif choice == '5':
            print("✅ Exiting Pastry Shop... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    run_pastry_shop()
