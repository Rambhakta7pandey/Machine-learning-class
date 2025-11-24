class Searching:
    def __init__(self, arr):
        self.arr = arr

    # ---------- Linear Search ----------
    def linear_search(self, key):
        for i in range(self.arr_len()):
            if self.arr[i] == key:
                return i
        return -1

    # ---------- Binary Search ----------
    def binary_search(self, key):
        low = 0
        high = self.arr_len() - 1

        while low <= high:
            mid = (low + high) // 2

            if self.arr[mid] == key:
                return mid
            elif key < self.arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def arr_len(self):
        return len(self.arr)


# =====================================================
#              SAFE INPUT FUNCTION
# =====================================================
def get_array():
    while True:
        try:
            raw = input("Enter array elements (comma or space separated): ")

            # replace commas with spaces
            raw = raw.replace(",", " ")

            # split and convert to int
            arr = list(map(int, raw.split()))

            return arr

        except ValueError:
            print("⚠️ Invalid input! Please enter only numbers.")
            continue


# =====================================================
#                    MAIN PROGRAM
# =====================================================
def main():
    print("\n=== SEARCHING PROGRAM ===")

    arr = get_array()
    search_obj = Searching(arr)

    while True:
        print("\n1. Linear Search")
        print("2. Binary Search")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            key = int(input("Enter element to search: "))
            pos = search_obj.linear_search(key)

            if pos != -1:
                print(f"✔️ Found at index {pos}")
            else:
                print("❌ Not found")

        elif choice == "2":
            # Binary search needs sorted array
            arr.sort()
            print("Sorted Array:", arr)

            key = int(input("Enter element to search: "))
            pos = search_obj.binary_search(key)

            if pos != -1:
                print(f"✔️ Found at index {pos}")
            else:
                print("❌ Not found")

        elif choice == "3":
            print("Bye!")
            break

        else:
            print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    main()
