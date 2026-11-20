import csv
from datetime import date

today = date.today() 
csv_filename = "expense.csv"

#Initial Balance to record expenses
total_balance = 1000
print(f"Initial Balance: {total_balance}")

#Expense to deduct from the Balance to show reduction
amount = float(input("Enter Amount to Record: "))
try :
    if amount < 0 :
        print("expenses cannot be Negative")
        exit()
except ValueError:
        print("Invalid Input")
        exit()
#Deduct the amount from Total
total_balance -= amount

print("\n")
#Type of category to record expense 
print("NOTE - 'G' for Groceries , 'PE' for Personal Expenses , 'HE' for HouseHold Expenses ")
print("\n")
#conditional function for selecting Category
category = str(input("Enter type of Category: ")).strip().upper()

icategory = {
      'G':'Groceries',
      'PE':'Personal Expenses',
      'HE':'HouseHold Expenses'
}
category_fullname = category in icategory
if category_fullname == 'G':
    print(f"Groceries ({category}) - {amount}  | Date: {today}")
elif category_fullname == 'PE':
    print(f"Personal Expenses ({category}) - {amount} | Date: {today}")
elif category_fullname == 'HE':
        print(f"HouseHold Expenses ({category}) - {amount} | Date: {today}")
else:
    print("Invalid Input")

print(f"Total Balance: {total_balance}")

try:
    try:
         with open(csv_filename, mode='r') as f:
               file_exists = True
    except FileNotFoundError:
         file_exists =False


    with open(csv_filename ,mode='a', newline='', encoding= 'utf-8-sig') as file:
            writer =csv.writer(file)


            if not file_exists:
                    writer.writerow(['Date','input Category','Category','Amount','Total Balance'])

            writer.writerow([today,icategory,category_fullname,amount,total_balance])
    print(f"Records inserted Successfully to {csv_filename}")

except Exception as e:
      print(f"Error occured whilst saving file")