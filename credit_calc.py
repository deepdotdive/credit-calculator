import sys
import argparse
import math

parser = argparse.ArgumentParser(description='credit calculator')

parser.add_argument('--type', help='')
parser.add_argument('--principal', type=int, help='')
parser.add_argument('--periods', type=int, help='')
parser.add_argument('--interest', type=float, help='')
parser.add_argument('--payment', type=int, help='')

args = parser.parse_args()


def i():
    return (args.interest / 100) / 12


def define_sentence():
    if n_[0] == 0:
        if n_[1] == 1:  # month
            print(f'You need {n_[1]} month to repay this credit!')
        else:  # months
            print(f'You need {n_[1]} months to repay this credit!')
    elif n_[0] == 1:
        if n_[1] == 1:  # year, month
            print(f'You need {n_[0]} year and {n_[1]} month to repay this credit!')
        else:  # year, months
            print(f'You need {n_[0]} year and {n_[1]} months to repay this credit!')
    elif n_[1] == 0:
        if n_[0] == 1:  # year
            print(f'You need {n_[0]} year to repay this credit!')
        else:  # years
            print(f'You need {n_[0]} years to repay this credit!')
    elif n_[1] == 1:
        if n_[0] == 1:  # year, month
            print(f'You need {n_[0]} year and {n_[1]} month to repay this credit!')
        else:  # years, month
            print(f'You need {n_[0]} years and {n_[1]} month to repay this credit!')
    else:  # years, months
        print(f'You need {n_[0]} years and {n_[1]} months to repay this credit!')


if len(sys.argv) != 5:
    print('Incorrect parameters')
else:
    if args.type == 'diff':

        if args.payment is None and args.principal > 0 and args.periods > 0 and args.interest >= 0:
            diff_overpayment = 0 - args.principal
            counter = 0
            for m in range(1, args.periods + 1):
                diff_overpayment += math.ceil((args.principal / args.periods) + i() *
                                              (args.principal - (args.principal * (m - 1) / args.periods)))
                counter += 1
                print(f'Month {counter}: paid out',
                      math.ceil((args.principal / args.periods) + i() *
                                (args.principal - (args.principal * (m - 1) / args.periods))))
            print('\nOverpayment = ', diff_overpayment, sep='')
        
        else:
            print('Incorrect parameters')

    elif args.type == 'annuity':
        
        if args.principal is None and args.payment > 0 and args.periods > 0 and args.interest >= 0:
            credit_principal = \
                args.payment / ((i() * (math.pow(1 + i(), args.periods))) / (math.pow(1 + i(), args.periods) - 1))
            credit_principal_overpayment = math.ceil(args.payment * args.periods - credit_principal)
            print('Your credit principal = ', int(credit_principal), '!', sep='')
            print('Overpayment =', credit_principal_overpayment)

        elif args.payment is None and args.principal > 0 and args.periods > 0 and args.interest >= 0:
            annuity_payment = math.ceil(
                args.principal * ((i() * math.pow(1 + i(), args.periods)) / (math.pow(1 + i(), args.periods) - 1)))
            annuity_overpayment = annuity_payment * args.periods - args.principal
            print('Your annuity payment = ', annuity_payment, '!', sep='')
            print('Overpayment =', annuity_overpayment)

        elif args.periods is None and args.principal > 0 and args.payment > 0 and args.interest >= 0:
            periods_count = math.ceil(math.log(args.payment / (args.payment - i() * args.principal), 1 + i()))
            n_ = [periods_count // 12, periods_count % 12]
            periods_overpayment = periods_count * args.payment - args.principal
            define_sentence()
            print('Overpayment =', periods_overpayment)

        else:
            print('Incorrect parameters')
