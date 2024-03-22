# from eth_account import (
#     Account,
# )
# from eth_keys import (
#     keys,
# )
# from mnemonic import (
#     Mnemonic
# )
#
#
# def create_account(password='', restore_sentence=None):
#     """
#     Creates new wallet that means private key with an attached address using os.urandom CSPRNG
#     :param password: Is used as extra randomness to whatever randomness your OS can provide
#     :param restore_sentence: Used in case of restoring wallet from mnemonic sentence.
#     :return: object with private key
#     """
#     extra_entropy = password
#
#     mnemonic = Mnemonic("english")
#     if restore_sentence is None:
#         mnemonic_sentence = mnemonic.generate()
#     else:
#         mnemonic_sentence = restore_sentence
#     seed = mnemonic.to_seed(mnemonic_sentence, extra_entropy)
#     master_private_key = seed[32:]
#     eth_acc = from_key(master_private_key)
#     priv_key = keys.PrivateKey(eth_acc.privateKey)
#     pub_key = priv_key.public_key
#     return pub_key, priv_key.to_hex()
#
#
# def from_key(private_key):
#     return Account.from_key(private_key)
