def import_account(dic_accs, filename = 'accounts.csv'):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            add_to_account(account, row)
    return account


def export_account(dic_accs, filename = 'accounts.csv'):
    account_list = []
    for key, val in account.items():
        for i in range(val):
            account_list.append(key)
    with open(filename, 'w') as csvfile:
        for element in account_list:
            if account_list[-1]:
                csvfile.write(element)
            else:
                csvfile.write(element + ',')


def create_account(dic_accs):
    login = input('Enter login: ')
    password = input('Enter password: ')
    return dic_accs[login] = password
