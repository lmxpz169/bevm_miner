from web3 import Web3,Account
import time 
import uuid

#rpc信息
rpc="https://rpc-2.bevm.io/"
#接受地址
to_address =''
#你自己的私钥
private_key=''
lim=1500 #打多少张


def generate_random_uuid():
    return str(uuid.uuid4())

# 连接到rpc节点
w3 = Web3(Web3.HTTPProvider(rpc))
from_address = Account.from_key(private_key).address
print('网络链接：',w3.is_connected())
#判断网络链接
if w3.is_connected() ==True:
    #获取当前noce
    nonce=w3.eth.get_transaction_count(from_address)
    # 批量发送交易
    for i in range(lim):
        # 获取当前燃气价格
        gas_price = w3.eth.gas_price
        # 将燃气价格从Wei转换为Gwei
        gas_price_gwei = w3.from_wei(gas_price, 'Gwei')
        data = 'data:application/json,{"p":"bm-20","op":"mint","tick":"BMW","id":"5fdec33d-dd2e-4241-abce-958c36339b5a","amt":"10"}'
        # 生成随机UUID
        random_uuid = generate_random_uuid()
        # 替换ID值
        modified_data = data.replace('"id":"5fdec33d-dd2e-4241-abce-958c36339b5a"', f'"id":"{random_uuid}"')
        print("当前nonce:",nonce,"当前gas:",gas_price_gwei,'发送地址:',from_address,'data:',modified_data)
        transaction = {
            'from': from_address,  # from：发送地址
            'to': to_address,  # to：接收地址
            'value': w3.to_wei(0, 'ether'),  # value：发送的以太币数量（整数）。这是以太币的数量，以Wei为单位。1 Ether等于10^18 Wei。
            'nonce': nonce,  # nonce：发送地址的交易计数（整数）。它用于确保交易的唯一性。
            'gas': 210000,  # gas：指定用于交易的燃气数量（整数）。燃气用于执行交易的计算和存储操作。
            'gasPrice': int(1.2 * gas_price),  # gasPrice：燃气价格（整数）。以Wei为单位的燃气单价，用于计算交易的燃气费用。
            'data': w3.to_hex(text=modified_data),  # 要添加到 Input Data 的自定义数据
            'chainId': w3.eth.chain_id  # 区块链id
        }
        # 2.签名交易
        signed = w3.eth.account.sign_transaction(transaction, private_key)
        try:
            # 3.广播交易
            tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
            print("Hash:", tx_hash.hex(),'noce:',nonce)
        except Exception as e:
            print('交易发生错误',e,'交易data：',data)
        nonce+=1


