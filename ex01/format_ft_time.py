from datetime import datetime

now = datetime.now()
seconds_now = now.timestamp()

start = datetime(1970, 1, 1, 0, 0, 0)
seconds_start = start.timestamp()

time_diff = seconds_now - seconds_start

print(f"Seconds since {start.strftime('%B %d, %Y')}: {time_diff:,.4f} or {time_diff:e} in scientific notation")
print(now.strftime("%b %d %Y"))
#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$