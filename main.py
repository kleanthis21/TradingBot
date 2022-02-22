import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient

logger = logging.getLogger()


stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

#fdsfsd
if __name__ == '__main__':

    binance = BinanceFuturesClient("5d95ba313ab9acdd29ef68cf9ae779dc0b35f17f75443d90ee17335d7e2bf457",
                                   "cc9f11837d30fa5cfbbabbcee7888ca8c9f4d277af61c66b81b54d71382ccd58", True)
    print(binance.get_balances())
    #print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 40000, "GTC"))
    #print(binance.get_order_status("BTCUSDT", 2964498628))
    #print(binance.cancel_order("BTCUSDT", 2964498628))


    root = tk.Tk()
    root.mainloop()







