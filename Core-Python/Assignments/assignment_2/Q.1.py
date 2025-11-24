#1. Convert the time entered in hh,min and sec into seconds.
hrs=float(input("Enter hours:"))
min=float(input("Enter the minutes:"))
sec=float(input("Enter the seconds:"))
total_sec=(hrs*3600)+(min*60)+(sec)
print("Total time in seconds:",total_sec)