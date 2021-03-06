import sys
from xlrd import open_workbook
from decimal import Decimal, InvalidOperation

if sys.argv[1] == '--csv':
    output_format = 'csv'
    book = open_workbook(sys.argv[2])
    s = book.sheet_by_index(0)
else:
    output_format = 'qif'
    book = open_workbook(sys.argv[1])
    s = book.sheet_by_index(0)

col_search = True

amount_col = -1
transaction_date_col = -1
details_col = -1
credit_card = False

transactions = []

for row in range(s.nrows):
    # we are searching for column identifiers
    if col_search:
        for col in range(s.ncols):
            contents = s.cell(row, col).value
            if contents == "Amount" or contents == "KD. Equivalent ":
                amount_col = col
                col_search = False # done searching
                credit_card = contents == "KD. Equivalent "
            elif contents == "Post Date":
                transaction_date_col = col
            elif contents == "Transaction Date" and transaction_date_col == -1:
                transaction_date_col = col
            elif contents == "Details" or contents == "Transaction Details":
                details_col = col
    else:
        try:
            amount = str(s.cell(row, amount_col).value).split("\n")[0]
            transaction_date = s.cell(row, transaction_date_col).value.split("\n")[0]
            details = s.cell(row, details_col).value.split("\n")[0]
            
            if credit_card:
                amount = str(-1 * Decimal(amount))
            else:
                Decimal(amount)
            
            transactions.append((transaction_date, amount, details))
        except InvalidOperation:
            pass

if output_format == 'csv':
    print('date,amount,details')
    for t in transactions:
        print('{},{},{}'.format(*t))
elif output_format == 'qif':
    print("!Type:Bank")
    for t in transactions:
        print("D" + t[0])
        print("T" + t[1])
        print("P" + t[2])
        print("^")