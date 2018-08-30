import numpy as np



def provide_credit_amount(credit_amount):
    return credit_amount

def provide_interest_rate_of_credit(credit_rates):
    return credit_rates

def provide_credit_installment_rate(credit_installment):
    return (credit_installment)

def calculate_credit_interest_and_month(credit_amount,credit_rates,credit_installment):
    copy_of_credit_amount = credit_amount
    credit_remained=credit_amount
    months_number=0
    rate_sum=0
    while credit_remained > 0:
         months_number += 1
         monthly_rate = credit_remained * credit_rates / 100 / 12
         monthly_amount = credit_installment - monthly_rate
         credit_remained = credit_remained - monthly_amount
         rate_sum += monthly_rate
         print ("####### ### #######\n")
         print ("Month: {}".format(months_number))
         print ("Credit interests to pay: ", monthly_rate)
         print ("Credit capital to pay: ", monthly_amount)
         print ("Credit capital remaining: {}\n ".format(credit_remained))

    print("CREDIT RATE SUM: ", rate_sum)



def main():
    credit_amount = provide_credit_amount(input("Enter credit amount:"))
    credit_rates = int(input("Enter credit interest rate:"))
    credit_installment = int(input("Enter credit installment rate: "))
    calculate_credit_interest_and_month(provide_credit_amount(credit_amount), provide_interest_rate_of_credit(credit_rates), provide_credit_installment_rate(credit_installment))

main()

