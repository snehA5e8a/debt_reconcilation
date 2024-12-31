owe = {
    'Somiya': 8535,
    'Dalia': 6690,
    'Sophy': 8440,
    'Appachan': 8740,
    'Steffin': 1913,
    'Sneha': 3487,
    'George': 2459,
    'Suni': 8680
}

spend = {
'Oswin': 21220,
'Susan': 26373,
'Divya': 1350
}

for debtor, debt in owe.items():
    if debt>0:     
        for creditor, lent in spend.items():
            if lent>0:
                if debt<=lent:
                    print(debtor, 'owes', creditor, debt)
                    spend[creditor] -= debt
                    owe[debtor] = 0
                    break
                else:
                    print(debtor, 'owes', creditor, lent)
                    owe[debtor] -= lent
                    debt = owe[debtor]
                    spend[creditor] = 0          