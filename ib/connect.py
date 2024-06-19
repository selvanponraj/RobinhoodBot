from ib_insync import CFD
from ib_insync import IB, Future, Forex
from ib_insync import util
from .utils import list_to_str
import time
import datetime
from datetime import timedelta, datetime, timezone

def reconnect(ib_instance):
    if not ib_instance.isConnected():
        print("Connection to IB API lost, trying to connect again...")
        try:
            ib_instance.connect('127.0.0.1', 7497, clientId=1)
            print("The connection to the IB API has been restored.")
        except Exception as e:
           print(f"Error trying to reconnect: {e}")

def connect_to_ib():
    ib = IB()
    max_attempts = 100
    attempt = 0

    while attempt < max_attempts:
        try:
            ib.connect('127.0.0.1', 7497, clientId=101)
            print("\n\n>> Connection to Interactive Brokers was successful.")
            return ib
        except ConnectionRefusedError:
            print("Connection to Interactive Brokers refused. Waiting and retrying...")
            attempt += 1
            time.sleep(30)
        except Exception as e:
            print(f"Connection error: {e}")
            return None

    print("Maximum number of attempts to connect to Interactive Brokers exceeded.")
    return None

def ib_account(ib):
    # Returns Dataframe of Account Information
    # Find Account Name
    account = ib.managedAccounts()[0]
    acc_str = list_to_str(account)

    # Get Account Summary Dataframe
    acc_val_list = ib.accountSummary(acc_str)
    df = util.df(acc_val_list)
    df = df.set_index('tag')
    # Return Dataframe as output
    return df

ib = connect_to_ib()
if ib is None:
    exit()


positions = ib.positions()

for position in positions:
    print(f'You have {position.position} shares of {position.contract.symbol}')

# df = ib_account()

# print(df)
# print(gbp_usd_rate(ib))

ib.disconnect()

def is_trading_time():
    now = datetime.now(timezone.utc)
    print(now)
    day = now.weekday()
    hour = now.hour
    # Checking if the time is in business hours (Monday 8:00 UTC to Friday 20:00 UTC)
    if 0 <= day <= 4 and 1 <= hour < 21:
        print("Markets are open for trading")
        return True
    else:
        print("Markets are closed.")
        return False

def get_current_date_string():
    current_date = datetime.now()
    return current_date.strftime('%Y%m%d-23:00:00')

