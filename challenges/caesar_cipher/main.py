from cipher_encoder.encoder import Encoder
from interface.ascii import LOGO


def clear_terminal():
    print("\033[H\033[J", end="")


def main():
    encoder = Encoder()

    while True:
        clear_terminal()
        print(LOGO)
        print("Do you want to encode or decode a messsage?")
        operation = input('Type "encode" or "decode":\n').strip().lower()

        if operation not in ["encode", "decode"]:
            print("\nThe operation selected is not available.")
            break

        message = input("\nWrite your message below:\n").strip().lower()
        shift = int(input("What is the shift number: "))

        match operation:
            case "encode":
                encoder.encode(message, shift)
            case "decode":
                encoder.decode(message, shift)

        print(f"\nThe {operation}d result is this:\n{encoder.message}")

        keep_running = input('\nDo you want to continue? "Y" or "N": ').upper()
        if keep_running == "N":
            break


if __name__ == "__main__":
    main()
