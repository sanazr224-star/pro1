def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0):
        f2 = 29
    else:
        f2 = 28
    
    # محاسبه روزهای گذشته از سال میلادی
    k_days = g_d_m[gm-1] + gd
    if gm > 2 and (gy % 4 == 0 and gy % 100 != 0 or gy % 400 == 0):
        k_days += 1
        
    if k_days <= 79:
        jy = gy - 622
        jm = (k_days + 286) // 30
        jd = (k_days + 286) % 30
    else:
        jy = gy - 621
        k_days -= 79
        if k_days <= 186:
            jm = (k_days - 1) // 31 + 1
            jd = (k_days - 1) % 31 + 1
        else:
            jm = (k_days - 187) // 30 + 7
            jd = (k_days - 187) % 30 + 1
            
    return jy, jm, jd

# حالا اینجا از کاربر ورودی بگیر:
year = int(input("سال میلادی را وارد کن: "))
month = int(input("ماه میلادی را وارد کن: "))
day = int(input("روز میلادی را وارد کن: "))

# صدا زدن تابع:
y, m, d = gregorian_to_jalali(year, month, day)

print(f"تاریخ شمسی شما: {y}/{m}/{d}")
