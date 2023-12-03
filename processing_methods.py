def ZalohovaneFlaseProcessing(df):
    df['voucher_amount'] = df['quantity'] * 0.15
    df['voucher_redemption_date'] = df['created'].apply(lambda x: x[:x.index(' ')])
    df['dummy_date'] = df['voucher_redemption_date']
    df['month'] = df['dummy_date'].apply(lambda x: x.split('.')[1])
    df['year'] = df['dummy_date'].apply(lambda x: x.split('.')[2])
    df['charity'] = 'FALSE'
    df.drop(labels = ['cp_description', 'created', 'quantity'], axis = 1, inplace = True)
