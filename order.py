orders = []


def add_order(items, total):

    order = {
        "items": items.copy(),
        "total": total,
        "payment": "Pending",
        "status": "Order Placed",
        "delivery_status": "Order Confirmed"
    }

    orders.append(order)

    print("ORDER SAVED")
    print("TOTAL ORDERS:", len(orders))

    return order