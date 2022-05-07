def main():
    name = "This is a string"
    print(name.title())  # Returns a string in CamelCase
    print(name.islower())
    print(name.count("a"))
    print(name.casefold())
    print(name.find("a"))
    print(name.expandtabs())
    print(name.isdecimal())
    print(name.ljust(4))


if __name__ == "__main__":
    main()
