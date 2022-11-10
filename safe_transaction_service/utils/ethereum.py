from functools import cache

from gnosis.eth import EthereumClientProvider
from safe_transaction_service.utils.ethereum_network import EthereumNetwork



@cache
def get_ethereum_network() -> EthereumNetwork:
    return EthereumClientProvider().get_network()
