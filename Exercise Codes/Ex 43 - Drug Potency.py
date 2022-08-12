drg_ptn = 100
rate = .96
cnt = 0
exp = ""
print(f"Month: {cnt}     effectiveness: {drg_ptn} {exp}")
while drg_ptn > 50:
    drg_ptn = drg_ptn * rate
    cnt = cnt + 1
    if drg_ptn < 50:
        exp = "DISCARDED"
    print(f"Month: {cnt}     effectiveness: {drg_ptn} {exp}") 