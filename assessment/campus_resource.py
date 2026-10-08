resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


def find_resource(resource_id):
    for resource in resources:
        if resource["id"].upper() == resource_id.upper():
            return resource

    return None


def add_resource():
    resource_id = input("Enter resource ID: ").strip()

    if find_resource(resource_id) is not None:
        print("Error: Resource ID already exists.")
        return

    name = input("Enter resource name: ").strip()
    category = input("Enter resource category: ").strip()

    try:
        total = int(input("Enter total units: "))

        if total <= 0:
            print("Error: Total units must be greater than 0.")
            return

    except ValueError:
        print("Error: Total units must be a whole number.")
        return

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(resource)

    print("Resource added successfully.")


def list_resources():
    print("\n--- RESOURCE INVENTORY ---")

    if len(resources) == 0:
        print("No resources found.")
        return

    for resource in resources:
        print(
            f'{resource["id"]} | '
            f'{resource["name"]} | '
            f'{resource["category"]} | '
            f'Total: {resource["total"]} | '
            f'Available: {resource["available"]}'
        )


def borrow_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID not found.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            return

    except ValueError:
        print("Error: Quantity must be a whole number.")
        return

    if quantity > resource["available"]:
        print(
            f'Error: Only {resource["available"]} '
            f'{resource["name"]} unit(s) are available.'
        )
        return

    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource["id"],
        "quantity": quantity
    })

    print(
        f'{fellows[fellow_id]} borrowed '
        f'{quantity} {resource["name"]}(s) successfully.'
    )


def return_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID not found.")
        return

    try:
        quantity = int(input("Enter quantity to return: "))

        if quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            return

    except ValueError:
        print("Error: Quantity must be a whole number.")
        return

    borrowed = 0

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource["id"]
        ):
            borrowed += record["quantity"]

    if quantity > borrowed:
        print(
            f"Error: {fellows[fellow_id]} currently has only "
            f"{borrowed} unit(s) of this resource on loan."
        )
        return

    remaining = quantity

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource["id"]
            and remaining > 0
        ):
            amount = min(record["quantity"], remaining)

            record["quantity"] -= amount
            remaining -= amount

    borrow_records[:] = [
        record for record in borrow_records
        if record["quantity"] > 0
    ]

    resource["available"] += quantity

    print(
        f'{fellows[fellow_id]} returned '
        f'{quantity} {resource["name"]}(s) successfully.'
    )


def search_resources():
    search = input("Enter resource name to search: ").strip().lower()

    found = False

    print("\n--- SEARCH RESULTS ---")

    for resource in resources:
        if search in resource["name"].lower():
            print(
                f'{resource["id"]} | '
                f'{resource["name"]} | '
                f'{resource["category"]} | '
                f'Available: {resource["available"]}'
            )
            found = True

    if not found:
        print("No matching resources found.")


def filter_by_category():
    category = input("Enter category: ").strip().lower()

    found = False

    print("\n--- CATEGORY RESULTS ---")

    for resource in resources:
        if resource["category"].lower() == category:
            print(
                f'{resource["id"]} | '
                f'{resource["name"]} | '
                f'{resource["category"]} | '
                f'Available: {resource["available"]}'
            )
            found = True

    if not found:
        print("No resources found in that category.")


def generate_report():
    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("\n--- RESOURCE REPORT ---")
    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")

    print("\nLow stock resources:")

    low_stock_found = False

    for resource in resources:
        if resource["available"] < 3:
            print(
                f'- {resource["name"]} '
                f'({resource["available"]} available)'
            )
            low_stock_found = True

    if not low_stock_found:
        print("None")

    borrowed_by_resource = {}

    for record in borrow_records:
        resource_id = record["resource_id"]

        if resource_id not in borrowed_by_resource:
            borrowed_by_resource[resource_id] = 0

        borrowed_by_resource[resource_id] += record["quantity"]

    if borrowed_by_resource:
        highest = max(borrowed_by_resource.values())

        print("\nMost borrowed resource:")

        for resource_id, quantity in borrowed_by_resource.items():
            if quantity == highest:
                resource = find_resource(resource_id)

                print(
                    f'- {resource["name"]} '
                    f'({quantity} currently borrowed)'
                )
    else:
        print("\nMost borrowed resource: None")


def show_menu():
    print("\n==============================")
    print(" CAMPUS RESOURCE MANAGEMENT")
    print("==============================")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Generate report")
    print("0. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            generate_report()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid menu option.")


main()