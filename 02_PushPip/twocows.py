import argparse
import cowsay


def display_cows(first_message, second_message, first_cow, second_cow, first_eyes, second_eyes, tongue, width, first_wrap, second_wrap):
    first_cow_output = cowsay.cowsay(first_message, cow=first_cow, eyes=first_eyes, tongue=tongue, wrap_text=first_wrap, width=width).split("\n")
    second_cow_output = cowsay.cowsay(second_message, cow=second_cow, eyes=second_eyes, tongue=tongue, wrap_text=second_wrap, width=width).split("\n")
    max_width = max(len(line) for line in first_cow_output + second_cow_output)

    lines_first_cow = len(first_cow_output)
    lines_second_cow = len(second_cow_output)

    final = []
    
    for i in range(max(lines_first_cow, lines_second_cow)):
        part_one = first_cow_output[lines_first_cow - i - 1] if i < lines_first_cow else ""
        part_two = second_cow_output[lines_second_cow - i - 1] if i < lines_second_cow else ""
        combined_line = part_one + " " * (max_width - len(part_one)) + part_two + "\n"
        final.append(combined_line)
        
    print(*final[::-1])


def main():
    parser = argparse.ArgumentParser(description='Display two cows with different messages')

    parser.add_argument("-e", "--first_eyes", default="oo", help="Eyes for the first cow")
    parser.add_argument("-f", "--first_cow", default="default", help="Choose first cow")
    parser.add_argument("-n", "--first_wrapper", action="store_true", help="Wrap text for first cow")
    parser.add_argument("-T", "--tongue", default="  ", help="Tongue for both cows")
    parser.add_argument("-W", "--width", type=int, default=40, help="Width for text wrapping")
    parser.add_argument("first_message", nargs="?", default=None, help="Message for the first cow")

    parser.add_argument("-E", "--second_eyes", default="oo", help="Eyes for the second cow")
    parser.add_argument("-F", "--second_cow", default="default", help="Choose second cow")
    parser.add_argument("-N", "--second_wrapper", action="store_true", help="Wrap text for second cow")
    parser.add_argument("second_message", nargs="?", default=None, help="Message for the second cow")

    args = parser.parse_args()

    display_cows(
        first_message=args.first_message,
        second_message=args.second_message,
        first_cow=args.first_cow,
        second_cow=args.second_cow,
        first_eyes=args.first_eyes,
        second_eyes=args.second_eyes,
        tongue=args.tongue,
        width=args.width,
        first_wrap=args.first_wrapper,
        second_wrap=args.second_wrapper
    )


if __name__ == '__main__':
    main()
