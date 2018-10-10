

# 入口文件  出现了循环导入的问题！？
# 在入口文件中調用在app/app.py實例化flask核心對象app


from app.app_ import create_app

# 調用實例化的app
app = create_app()


# 爲入口文件定製一個示例的視圖函數  (也就是說可以在入口文件中創建視圖函數)
# 把所有視圖函數寫在入口文件中是非常不可取的 拆分視圖函數，特定視圖函數屬於某個版本號是好的標記
# 如何在版本目錄下(如/v1)下的視圖函數中拿到入口文件的實例化的app?(一個問題接龍一個問題)？
#可以嘗試用藍圖註冊的辦法 （藍圖級別太高？後面再處理）
# 無法直接 視圖函數----->app 所以分兩步
#1. 視圖函數（在特定版本目錄下）---->blueprint(實例化藍圖)   sep_flask/api/v1/特定視圖函數文件(如user.py)
#2. 再將實例化的藍圖註冊到flask核心對象app上面   set_flask/app/app.py(對核心對象app的所有操作都在app/app.py中)






#啓動 上面調用的app

#判斷是否是入口文件
if __name__ == '__main__':
    app.run(debug=True)

