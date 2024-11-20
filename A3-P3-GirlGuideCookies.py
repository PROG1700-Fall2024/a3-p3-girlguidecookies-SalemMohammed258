#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     
#Student Name:  


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
def get_guide_data(num_guides):
    """
    Collects the names and sales data for each guide.
    :param num_guides: int, number of guides
    :return: list of tuples [(name, boxes_sold), ...]
    """
    guides = []
    for i in range(1, num_guides + 1):
        name = input(f"Enter the name of guide #{i}: ")
        while True:
            try:
                boxes_sold = int(input(f"Enter the number of boxes sold by {name}: "))
                if boxes_sold < 0:
                    print("Sales cannot be negative. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        guides.append((name, boxes_sold))
    return guides


def calculate_prizes(guides):
    """
    Calculates prizes for each guide based on their sales.
    :param guides: list of tuples [(name, boxes_sold), ...]
    :return: tuple (average_sales, prize_list)
    """
    total_sales = sum(boxes_sold for _, boxes_sold in guides)
    average_sales = total_sales / len(guides) if guides else 0

    # Determine the highest sales
    highest_sales = max(guides, key=lambda x: x[1])[1] if guides else 0

    # Assign prizes
    prizes = []
    for name, boxes_sold in guides:
        if boxes_sold == highest_sales:
            prize = "Trip to Jamboree"
        elif boxes_sold > average_sales:
            prize = "Badge"
        elif boxes_sold > 0:
            prize = "Share Remaining Cookies"
        else:
            prize = "No Prize"
        prizes.append((name, boxes_sold, prize))

    return average_sales, prizes


def display_results(average_sales, prizes):
    """
    Displays the average sales and prizes for each guide.
    :param average_sales: float, the average sales
    :param prizes: list of tuples [(name, boxes_sold, prize), ...]
    """
    print(f"\nAverage Sales: {average_sales:.2f} boxes\n")
    print("Guide Results:")
    for name, boxes_sold, prize in prizes:
        print(f"{name} sold {boxes_sold} box(es) - Prize: {prize}")


def main():
    print("Welcome to the Girl Guide Cookie Sale Event!\n")
    while True:
        try:
            num_guides = int(input("How many guides participated in the event? "))
            if num_guides < 1:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    guides = get_guide_data(num_guides)
    average_sales, prizes = calculate_prizes(guides)
    display_results(average_sales, prizes)


if __name__ == "__main__":
    main()







    # YOUR CODE ENDS HERE

main()