debt = 1000
interest = .015
cnt = 0
py = 0
mth_py = float(input("Enter the monthly payment:\n"))
while debt > 0:
    cr_int = debt * interest
    debt = (debt - mth_py) + cr_int
    cnt = cnt + 1
    py = py + mth_py
    print(f"Month: {cnt}     balance: {debt} total payments: ${py}")
fn_py = py + debt
print(f"Total payments: ${fn_py}")