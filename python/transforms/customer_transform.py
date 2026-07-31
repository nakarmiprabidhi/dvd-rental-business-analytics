def select_customer_columns(df):
    customer_report = df[
        [
            "First Name",
            "Email",
            "Active",
            "Store"
        ]
    ]

    customer_report = customer_report[
        customer_report["Store"] == 1
    ]

    return customer_report