from queries import clean_username, validate_username


def main():
    print("=" * 40)
    print(" Telegram OSINT Tool")
    print("=" * 40)

    username = input("\nEnter a Telegram username: ")

    if not validate_username(username):
        print("\n[-] Invalid username format.")
        print("    Use 5-32 letters, numbers, or underscores.")
        return

    username = clean_username(username)

    print(f"\n[+] Valid username: @{username}")


if __name__ == "__main__":
    main()