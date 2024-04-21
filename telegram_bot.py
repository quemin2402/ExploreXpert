import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import CommandStart,Command,or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from bot.private import private
from keyboard import reply
import gpt
from take_data import preparer
import share_coord
import requests

TOKEN='7138496335:AAFaPH7C6izcOx5hi8brPeqHeNda8seWadQ'
bot =Bot(token=TOKEN)

dp=Dispatcher()

hashi={}

user_choice={}

location=None



 
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Welcome to our chatbot, in partnership with City Pass Astana, your digital guide to all things Astana and Kazakhstan! 🇰🇿 \nWhether you're curious about the futuristic skyline of Astana, now known as Nur-Sultan, or the rich history and culture of this Central Asian gem, I'm here to help.\n From local cuisine to must-visit landmarks, let's explore the beauty and diversity of Kazakhstan together. Ask me anything!",reply_markup=reply.start_kb)

@dp.message(or_f(Command('understand_new_information'), F.text.lower()=="chat about the attractions"))
async def info(message: types.Message):
    global hashi
    hashi[message.from_user.id] = True
    await message.answer('You can ask your questions!', reply_markup=reply.back_kb)


@dp.message(or_f(Command('make_a_tour'),F.text.lower()=='build your route'))
async def tour(message: types.Message):
    await message.answer('Choose your locations:',reply_markup=reply.categories_kb)

@dp.message(F.text.lower()=='menu')
async def back(message:types.Message):
    global hashi
    hashi[message.from_user.id] = False
    await message.answer('Welcome back. Choose your option.',reply_markup=reply.start_kb)

@dp.message(F.text.lower()=='back')
async def museums(message:types.Message):
     await message.answer('Continue choosing your locations:', reply_markup=reply.categories_kb)

@dp.message(F.text.lower()=='museums')
async def museums(message:types.Message):
     await message.answer('Here a list of available museums', reply_markup=reply.museums_kb)

@dp.message(F.text.lower()=='parks')
async def museums(message:types.Message):
     await message.answer('Here a list of available parks', reply_markup=reply.parks_kb)

@dp.message(F.text.lower()=='entertainment')
async def museums(message:types.Message):
     await message.answer('Here a list of available entertainments', reply_markup=reply.entertainment_kb)

@dp.message(F.text.lower()=='monuments')
async def museums(message:types.Message):
     await message.answer('Here a list of available monuments', reply_markup=reply.monuments_kb)

@dp.message(F.text.lower()=='malls')
async def museums(message:types.Message):
     await message.answer('Here a list of available malls', reply_markup=reply.malls_kb)

@dp.message(F.text.lower()=='religious')
async def museums(message:types.Message):
     await message.answer('Here a list of available religious', reply_markup=reply.religious_kb)

@dp.message(F.text.lower()=='excursion')
async def museums(message:types.Message):
     await message.answer('Here a list of available religious', reply_markup=reply.excursion_kb)

@dp.message(F.text.in_(preparer.places))
async def upload_to_choice(message:types.Message):
    global user_choice
    user_choice[message.from_user.id]=user_choice.get(message.from_user.id,[])
    if message.text in user_choice[message.from_user.id]:
        user_choice[message.from_user.id].remove(message.text)
        await message.answer(f'You removed {message.text} from your choice!')
    else:
        user_choice[message.from_user.id].append(message.text)
        await message.answer(f'You added {message.text} in your choice!')

@dp.message(F.text == 'list of your choices')
async def choice(message:types.Message):
    global user_choice
    if message.from_user.id not in user_choice or user_choice[message.from_user.id] == []:
        await message.answer("List of your choices is empty!")
    else:
        await message.answer(f'You chose {user_choice[message.from_user.id]}.')

@dp.message(F.text == 'make a route')
async def confirmation(message:types.Message):
    global user_choice
    if message.from_user.id not in user_choice or user_choice[message.from_user.id] == []:
        await message.answer("List of your choices is empty!")
    else:
         await message.answer(f'Share with your geolocation if you confirm you path {user_choice[message.from_user.id]}',reply_markup=reply.confirmation_kb)

@dp.message(F.text == 'Clear my choices')
async def clear(message:types.Message):
    global user_choice
    user_choice[message.from_user.id]=[]
    await message.answer('You have succesfully clean your choice!')

@dp.message(F.location)
async def get_location(message:types.Message):
    global user_choice
    await message.answer('Location received, please wait for your route...')
    longtitude,latitude=message.location.longitude,message.location.latitude
    coords=preparer.transform(user_choice[message.from_user.id])
    share_coord.locationOutput(coords,[longtitude,latitude],message.from_user.id)
    await message.answer('Your route is ready!')
    path=f'maps/map_{message.from_user.id}.html'
    send_document = 'https://api.telegram.org/bot' + TOKEN +'/sendDocument?'
    data = {
  'chat_id': message.from_user.id,
  'parse_mode':'HTML',
  'caption':'This is your route!'
    }
    files={
         'document':open(path,'rb')
    }
    r=requests.post(send_document,data=data,files=files,stream=True)
    print(r.url)


    

@dp.message(F.text)
async def other(message: types.Message):
        global hashi
        if hashi.get(message.from_user.id,False):
            await message.answer(gpt.gpt(message.text))
        else:
             await message.answer('Unknown message. Please try again.')
       



async def  main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
asyncio.run(main())