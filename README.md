# bevm_miner
bevm 铭文 $BMW python 脚本

## 申明（写在最前面）
1. 此脚本按照根据上一次项目方规则，进行编写的，主要还是在json中加入了随机uuid的格式
2. 项目方暂未公布索引，因此此脚本不敢保证100%成功，请大家谨慎思考使用
3. 此脚本免费分享，如有运行问题，可以私信问我。但是否被项目方索引，是否打成功了，请自行负责，本人不为mint结果负责
4. 此项目，不会收集任何私钥等相关信息，请放心使用，项目开源，可直接看代码
5. 已自测过了，能成功运行

## 项目方twitter
https://twitter.com/BM20_BTClayer2

## json格式
```
data:application/json,{"p":"bm-20","op":"mint","tick":"BMW","id":"5fdec33d-dd2e-4241-abce-958c36339b5a","amt":"10"}
```


## 使用方法：

1. 请打开mint_bevm.py文件，用文本打开都行
2. 在to_address，填上你的evm钱包地址（也就是小狐狸钱包）
3. 在private_key，填上你的钱包私钥
4. 在终端（mac是termial，windows是powershell、cmd、gitbash都行），执行下列指令

### Mac电脑

* 输入以下指令:   
python3 mint_bevm.py

### windows电脑

* 输入以下指令:  
python mint_bevm.py


## 最后
再贴一个我找到的打BWM铭文的js的代码仓库，我看了下脚本，都差不多，作为备用，请自行选择分辨

https://github.com/sfter/evm-inscription-mint