def tracker():
    spent=0.0
    print('----Welcome to Expense Tracker----')
    print('\nenter your expenses one by one.When it is over type \'exit\'.')
    while True:
        user=input('\nenter expenses: ').strip()
        if user.lower()=='exit':
            break
        try:
            expense=float(user)
            if expense<0:
                print('enter positive number')
            spent+=expense
            print(f"\ntotal spent amount is Rs.{spent:.2f}")
        except error:
            print('invalid input.')
    print('-----------------------------------------------')
    print(f"Expense is Rs.{spent:.2f}")
    print('-----------------------------------------------')
if __name__=="__main__":
    tracker()
