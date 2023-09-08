from cli import find_product_by_name 


def find_product(product_name):
    find_product_by_name()
    
    
    
    
    
    
    
    
    
def main():
    choice = 1
    while choice != 4:
        print("=" * 10 + " Running Dog Adoption App " + "=" * 10)
        print("1) Interact with Facilities")
        print("2) Interact with Adopters")
        print("3) Interact with Dogs")
        print("4) quit!")

        choice = int(input(">>>"))

        

if __name__ == "__main__":
    main()