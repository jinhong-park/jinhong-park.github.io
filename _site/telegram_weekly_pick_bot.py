
#####    https://towardsdatascience.com/how-to-write-a-telegram-bot-with-python-8c08099057a8


#####    사진 업로딩
#####    https://code.luasoftware.com/tutorials/telegram/telegram-send-photo-to-channel


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 


from time import sleep


bot = Bot(token='6628416926:AAF1VoGyPOjozpREI0QRi73GW3e-8WXmF-U')

dp = Dispatcher(bot)

answers = []  # store the answers they have given


### add stuff here



# sends welcome message after start
@dp.message_handler(commands=['btc'])
async def welcome(message: types.Message):
    #await message.answer('hi', reply_markup = lang_kb)
    #await message.answer("From Telegram Bot")
    await message.answer_photo(photo = open("./btc30m.png",'rb'))
    await message.answer_photo(photo = open("./btc1h.png",'rb'))



# sends welcome message after start
@dp.message_handler(commands=['btcHigh'])
async def welcome(message: types.Message):
    #await message.answer('hi', reply_markup = lang_kb)
    #await message.answer("From Telegram Bot")
    await message.answer_photo(photo = open("./btc4h.png",'rb'))
    await message.answer_photo(photo = open("./btc6h.png",'rb'))
    await message.answer_photo(photo = open("./btc12h.png",'rb'))
    
    


@dp.message_handler(commands=['gm'])
async def welcome(message: types.Message):
    await message.answer('1. 장세 파악 : 일봉캔들로 전날캔들 중앙 위로 움직이면 롱 전날 일봉 중앙 아래로 움직이면 숏 관점으로 봄.')
    await message.answer("2. 숏 관점이면 볼린져밴드 중앙선에서 저항 맞는 다고 생각하고 숏에 들어가고 롱관점이면 볼린져밴드 중앙선에서 지지받는다는 생각을 한다.")
    await message.answer("3. 분봉은 보지 않고 보더라도 30분봉 1시간봉 4시간봉을 본다.")
    await message.answer("4. 볼린져밴드 내 생각 : 그러니까 볼린져밴드 하단에서는 숏치지 않고 볼린져밴드 상단에서는 롱치지 않아야 하네. 볼린져밴드 아래에 있는데(롱타점) 전날일봉캔들보다 아래로 빠지면 숏관점이니까 이날은 매매를 쉬어야함. 반대로 볼린져밴드 위에 있는데(숏타점) 전날일봉캔들보다 위로 가면 롱관점이므로 이날도 쉬어야함.")
    await message.answer("(X)5. 장세 파악 내 생각 : 전날일봉중앙을 기준으로 오전9시부터 오후5시까지 흐름을 관찰하자. 1시간봉을 기준으로 9개 봉과 30분봉 18개가 생기는데 중앙선을 몇번 넘었냐를 카운팅해서 포지션 정하자.")
    await message.answer("5. 장세 파악 내 생각 : 전날일봉중앙을 기준은 바로 첫날 틀렸음. 장세 파악은 전날일봉중앙도 맞지만 Hull trend buy sell 신호를 참고하자.")
    

    
# sends help message
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('We are a team of LGBT organizations from across Europe. We help you get into safety, provide support and answer any questions you may have. Press /start to get started. \nМи — команда ЛГБТ-організацій з усієї Європи. Ми допомагаємо вам увійти в безпеку, надаємо підтримку та відповідаємо на будь-які ваші запитання. Натисніть /start, щоб почати.')

# this is the last line

executor.start_polling(dp)

