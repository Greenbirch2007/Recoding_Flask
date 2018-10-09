


# 7月老師的思路是先佔位，然後在其他地方使用這個類
#最後再回過頭來實現這個類
# 下面就是先應用的過程
#1.首先實例化兩個redprint（自定義對象）
class Redprint:
    # 編寫一個類的時候，首先要思考它的構造函數（如何實例化） 還要在紅圖中取實現裝飾器的功能
    # （裝飾器不是憑空來的）（還是要借鑑藍圖）1.實例化構造函數 2. 實現裝飾器功能 3.實現url_prefix參數
    # 另外在應用這個紅圖的時候，用到了url_prefix的參數設置
    def __init__(self,name):
        self.name = name
        self.mound =[] #這裏是視圖函數的信息，所以列表
    # route函數的作用就是接收一堆參數，然後調用藍圖的add_url_rule方法完成視圖函數向藍圖的書冊
    def route(self,rule, **options):  #參考藍圖進行改寫
        def decorator(f): # f是裝飾器作用的方法
            #要解決的是在紅圖中如何拿到藍圖的本身？
            self.mound.append((f,rule,options))
            return f
        return decorator

    def register(self,bp,url_prefix=None):  # 在這個函數中有了藍圖，可以在這裏完成視圖那函數向紅圖的註冊方法
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f,rule,options in self.mound: # 序列解包（存入的時候是一個元組的形式，遍歷時自動解包成3個變量）
            endpoint = options.pop("endpoint", f.__name__) #f.__name__ 取視圖函數的名字作爲默認值
            bp.add_url_rule(url_prefix + rule,endpoint,f,**options)
            # 注意路由的註冊額 路由設計從後往前
            #  藍圖的url_prefix/紅圖的url_prefix/視圖函數中的rule






    # url---->endpoint---->viewfunction

# 在這裏紅圖要做的事情和藍圖是一樣的。都是接收來自視圖函數的參數。並完成視圖函數對其的註冊
# 有url要訪問請求時
# url--->endpoint ----->viewfunciton(視圖函數)


#反之，有視圖函數，要訪問url
# viewfunciton(視圖函數)------>endpoint-------->url
