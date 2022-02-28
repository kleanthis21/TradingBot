import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("5d95ba313ab9acdd29ef68cf9ae779dc0b35f17f75443d90ee17335d7e2bf457", "cc9f11837d30fa5cfbbabbcee7888ca8c9f4d277af61c66b81b54d71382ccd58", True)
    bitmex = BitmexClient("sbP7oq6vq8tGI1BPFzF3pAYi", "ESmZQFo-2iHJRpc-gIy87WuxqB69FsWnjSULpIAQNtMUu2o3", True)

    root = Root(binance, bitmex)
    root.mainloop()







