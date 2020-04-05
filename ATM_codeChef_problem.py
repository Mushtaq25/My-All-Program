x = float(input("ENter the amount you want to withdraw:-"))
y = float(input("Enter the total balance you have in your account:-"))

diff = (y-x) - 0.50
if x <= y:
    if x % 5 == 0:
        print("succesfull transaction:==")
        print(float(diff))
    else:
        print("incorrect witdrwal amount:==")
        print (float(y))
else:
    print("Insufficient Funds")
    print(float(y))
