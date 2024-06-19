
from ib_insync import *

def is_paper_account(ib_instance):
    managed_accounts = ib_instance.managedAccounts()
    for account in managed_accounts:
        if account.startswith('DU'):
            print(">> Account type: Paper account")
            return True  # DU znamená paper trading účet
        elif account.startswith('U'):
            print(">> Real account, not allowed!")
    return False

def list_to_str(list1):
    list_str = "".join(list1)
    return list_str

def usd_sgd_rate(ib_instance):
    # Gets the current USD_SGD Exchange Rate
    # Requires ib_account() connection to use.

    pair_name = Forex('USDSGD')
    bars = ib_instance.reqHistoricalData(
        pair_name, endDateTime='', durationStr='300 S',
        barSizeSetting='5 mins', whatToShow='MIDPOINT', useRTH=True)
    df = util.df(bars)
    df = df.tail(1)
    val = df['close'].values[0]
    return val

def gbp_usd_rate(ib_instance):
    # Gets the current USD_SGD Exchange Rate
    # Requires ib_account() connection to use.

    pair_name = Forex('GBPUSD')
    bars = ib_instance.reqHistoricalData(
        pair_name, endDateTime='', durationStr='300 S',
        barSizeSetting='5 mins', whatToShow='MIDPOINT', useRTH=True)
    df = util.df(bars)
    df = df.tail(1)
    val = df['close'].values[0]
    return val

def net_liquidation_value(dataframe):
    # Requires ib_account() dataframe to use.
    df = dataframe
    nlv_val = float(df.loc['NetLiquidation'].get('value'))
    return nlv_val

def buying_power(dataframe):
    # Requires ib_account() dataframe to use.
    df = dataframe
    bp_val = float(df.loc['BuyingPower'].get('value'))
    return bp_val

def available_funds(dataframe):
    # Requires ib_account() dataframe to use.
    df = dataframe
    af_val = float(df.loc['AvailableFunds'].get('value'))
    return af_val

def gross_position_value(dataframe):
    # Requires ib_account() dataframe to use.
    df = dataframe
    gpv_val = float(df.loc['GrossPositionValue'].get('value'))
    return gpv_val