from web3 import Web3

# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('https://arbitrum-one.public.blastapi.io'))

# 设置交易参数
account = Web3.toChecksumAddress('0xYourAccountAddress')
private_key = '0xYourPrivateKey'

contract_address = Web3.toChecksumAddress('0x67a24ce4321ab3af51c2d0a4801c3e111d88c9d9')
input_data = '0x4e71d92d'



#估算GAS
payload = {
    'from': account,
    'to': contract_address,
    'data': input_data
}
estimation = int(w3.eth.estimateGas(payload)*2)


# 构造交易
nonce = w3.eth.getTransactionCount(account)
tx = {
    'nonce': nonce,
    'to': contract_address,
    'value': 0,
    'gas': estimation,
    'gasPrice': w3.eth.gasPrice,
    'data': input_data
}

# 签名交易
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

# 发送交易
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# 打印交易哈希
print('Transaction Hash:', tx_hash.hex())
