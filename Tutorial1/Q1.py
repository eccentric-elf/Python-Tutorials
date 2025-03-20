def soln(secs):
    hrs=secs//3600
    mins=(secs%3600)//60
    secs=secs%60
    return f"Formatted Time= {hrs:02}:{mins:02}:{secs:02}"

secs=int(input("Enter the time in seconds: "))
formatted_time=soln(secs)
print(formatted_time)