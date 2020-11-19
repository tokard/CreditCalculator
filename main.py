import math
import argparse


class CreditCalculator:
    def annuity_month(self, principal, annuity_payment, credit_interest):
        nominal_interest_rate = credit_interest / 12 / 100
        count_of_periods = math.log(annuity_payment / (annuity_payment - nominal_interest_rate * principal),
                                    1 + nominal_interest_rate)
        count_of_periods = math.ceil(count_of_periods)
        print(f'You need {count_of_periods // 12} years and {count_of_periods % 12} months to repay this credit!')
        overpayment = annuity_payment * count_of_periods - principal
        print(f'Overpayment = {overpayment}')

    def annuity_payment(self, principal, count_of_periods, credit_interest):
        nominal_interest_rate = credit_interest / (12 * 100)
        annuity_payment = principal * (nominal_interest_rate * pow(1 + nominal_interest_rate, count_of_periods)) / \
                          (pow(1 + nominal_interest_rate, count_of_periods) - 1)
        annuity_payment = math.ceil(annuity_payment)
        print(f'Your annuity payment = {annuity_payment}!')
        overpayment = annuity_payment * count_of_periods - principal
        print(f'Overpayment = {overpayment}')

    def annuity_principal(self, annuity_payment, count_of_periods, credit_interest):
        nominal_interest_rate = credit_interest / (12 * 100)
        principal = annuity_payment / ((nominal_interest_rate * pow(1 + nominal_interest_rate, count_of_periods)) /
                                       (pow(1 + nominal_interest_rate, count_of_periods) - 1))
        principal = math.ceil(principal)
        print(f'Your credit principal = {principal}!')
        overpayment = annuity_payment * count_of_periods - principal
        print(f'Overpayment = {overpayment}')

    def diff_payment(self, principal, periods, interest):
        i = interest / (12 * 100)
        all_d = 0
        for j in range(periods):
            d = math.ceil(principal / periods + i * (principal - principal * j / periods))
            all_d += d
            print(f'Month {j + 1}: paid out {d}')
        print(f'\nOverpayment = {all_d - principal}')

    def action(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--type', help='the type of payments: "annuity" or "diff" (differentiated)')
        parser.add_argument('--payment', help='monthly payment', type=int)
        parser.add_argument('--principal', help='to calculate payment', type=int)
        parser.add_argument('--periods', help='the number of months and/or years needed to repay the credit', type=int)
        parser.add_argument('--interest', help='is specified without a percent sign', type=float)
        args = parser.parse_args()
        if args.type == 'annuity':
            if args.payment is None and args.principal and args.periods and args.interest:
                self.annuity_payment(args.principal, args.periods, args.interest)
            elif args.principal is None and args.payment and args.periods and args.interest:
                self.annuity_principal(args.payment, args.periods, args.interest)
            elif args.periods is None and args.principal and args.payment and args.interest:
                self.annuity_month(args.principal, args.payment, args.interest)
            else:
                print('Incorrect parameters')
        elif args.type == "diff" and args.principal and args.periods and args.interest:
            self.diff_payment(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameters')


credit = CreditCalculator()
credit.action()
