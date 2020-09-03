import argparse
import math
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()


def differentiated(p, n, i):
    i /= (12 * 100)
    sum_p = 0
    for month in range(1, n + 1):
        d = math.ceil(p / n + i * (p - (p * (month - 1) / n)))
        print(f'Month {month}: payment is {d}')
        sum_p += d
    over = sum_p - p
    print()
    print(f'Overpayment = {over}')


def annuity_payment(p, n, i):
    i /= (12 * 100)
    a = math.ceil(p * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    over = (a * n) - p
    print(f'Your annuity payment = {a}!')
    print(f'Overpayment = {over}')


def annuity_principal(p, n, i):
    i /= (12 * 100)
    principal = math.floor(p / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)))
    over = (p * n) - principal
    print(f'Your credit principal = {principal}!')
    print(f'Overpayment = {over}')


def annuity_periods(p, a, i):
    i /= (12 * 100)
    n = math.ceil(math.log((a / (a - i * p)), 1 + i))
    years = n // 12
    month = n % 12
    over = (a * n) - p

    if years == 0:
        print(f'It will take {month} months to repay this credit!')
    elif month == 0:
        print(f'It will take {years} years to repay this credit!')
    else:
        print(f'It will take {years} years and {month} months to repay this credit!')
    print(f'Overpayment = {over}')


if args.type == 'diff':
    if len(sys.argv[1:]) < 4 or not args.interest:
        print('Incorrect parameters.')
    else:
        differentiated(args.principal, args.periods, args.interest)
elif args.type == 'annuity':
    if len(sys.argv[1:]) < 4:
        print('Incorrect parameters.')
    else:
        if args.principal and args.periods and args.interest:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.payment and args.periods and args.interest:
            annuity_principal(args.payment, args.periods, args.interest)
        elif args.principal and args.payment and args.interest:
            annuity_periods(args.principal, args.payment, args.interest)
else:
    print('Incorrect parameters.')
