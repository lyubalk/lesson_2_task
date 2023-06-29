def bank():
    deposit = int(input("Введите сумму вклада >>> "))
    deposit_term = int(input("Введите срок вклада >>> "))

    for i in range(deposit_term):
        deposit += deposit * 0.1
        print(deposit)


bank()
