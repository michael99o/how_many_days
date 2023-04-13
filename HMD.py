#указываем кол-во секунд, получаем кол-во дней, часов, минут, секунд
sec_per_day = 86400
sec_per_hour = 3600
sec_per_min = 60

D = None
HH = None
MM = None
S = None

seconds = int(input('Input amount of seconds: '))
sec_ost = seconds

if seconds // sec_per_day == 0:
    D = 0
else:
    D = seconds // sec_per_day
    sec_ost = seconds - (D * sec_per_day)

if sec_ost // sec_per_hour == 0:
    HH = 0
else:
    HH = sec_ost // sec_per_hour
    sec_ost = sec_ost - (HH * sec_per_hour)

if sec_ost // sec_per_min == 0:
    MM = 0
    S = sec_ost
else:
    MM = sec_ost // sec_per_min
    sec_ost = sec_ost - (MM * sec_per_min)
    S = sec_ost
print("%d:%02d:%02d:%02d" % (D, HH, MM, S))
print(f"Days {D}, hours {HH}, minuts {MM}, seconds {S}")