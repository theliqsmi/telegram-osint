from queries import (
    clean_username,
    validate_username,
    generate_queries,
)

from report import save_report
from collectors.search import TavilySearchProvider

def main():
    print("=" * 45)
    print("       Telegram Public OSINT Tool")
    print("=" * 45)

    username = input("\nEnter a Telegram username: ")

    if not validate_username(username):
        print("\n[-] Invalid username format.")
        return

    username = clean_username(username)

     # feel free to remove this block
    while username == "cor299" or username == "naturalbornofvoid":
        username = input("\n You are not allowed to dig up Sadaf's digital footprint!\nOne of the key values to a healthy relationship is trust.\nEnter another username: ")
        username = clean_username(username)

    queries = generate_queries(username)

    print(f"\n[+] Username: @{username}")
    print(f"[+] Generated {len(queries)} queries")

    provider = TavilySearchProvider()
    all_results = []

    for query in queries:
        print(f"\n[*] Processing: {query}")

        try:
            results = provider.search(query)
            all_results.extend(results)

            print(f"[+] Found {len(results)} results")

        except RuntimeError as error:
            print(f"[-] {error}")

    
    print(f"\n[+] Collected {len(all_results)} sample results")

    filename = save_report(
        username,
        queries,
        all_results,
    )

    print(f"\n[+] Report saved: {filename}")


if __name__ == "__main__":
    main()