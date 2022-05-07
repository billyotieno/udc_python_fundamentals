# List, Tuples, Sets, Dictionaries, Compound Data Scructures
# List and membership operators

def main():
    months = ["January", "February", "March", "April", "May", "June"]
    print(months[0])
    print(months[-1])
    # print(months[50]) - Gives you an IndexError Exception

    # Slicing and dicing with list
    print(months[0:2])
    print("s" in "string")
    print("Sunday" in months)

    VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ',
             'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
    print(VINIX[0])

    print(len(VINIX))
    print(max(VINIX))
    print(min(VINIX))
    print(sorted(VINIX, reverse=True))

    print("\n".join(VINIX))
    VINIX.append("BILLY")
    print(VINIX)


if __name__ == "__main__":
    main()
