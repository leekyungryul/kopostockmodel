# FinanceDataReader 라이브러리 들어가면 크롤링하는
import FinanceDataReader as web
from datetime import date, timedelta
# 시각화 할때 쓴다.
import matplotlib.pyplot as plt
import datetime

# %matplotlib inline
# 해상도에 따라 다르다?
plt.figure(figsize=(15,9))
from matplotlib import font_manager, rc
# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family='AppleGothic')

today = date.today()
startday = date.today() - timedelta(720)
yesterday = date.today() - timedelta(1)
#startday = '3/14/2014'
#yesterday = '4/14/2016'
print(yesterday)
# 207940 : 종목코드
SEC = web.DataReader("AAPL", startday, yesterday)
# print(type(SEC))
print(SEC.tail(10))
# SEC['Close'].plot(figsize=(16,4))
# 2행 1열의 1행
plt.subplot(211)
# 아래 기간을 끊어서 close정보만을 b색상(파랑)으로 찍겠다.
SEC["2020-05-11":"2021-05-11"]['Close'].plot(figsize=(16,4), style='b')
# 2행 1열의 2행
plt.subplot(212)
# 아래 기간을 끊어서 volume정보만을 g색상(초록)으로 찍겠다.
SEC["2020-05-11":"2021-05-11"]["Volume"].plot(figsize=(16,4), style='g')

plt.show()