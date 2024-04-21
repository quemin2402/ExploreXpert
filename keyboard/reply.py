from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start_kb= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Build your route"),
            KeyboardButton(text="Chat about the attractions"),
        ]
    ],
    resize_keyboard=True
)

back_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu")]
    ],
    resize_keyboard=True
)

categories_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Parks'),KeyboardButton(text='Religious')],
        [KeyboardButton(text='Museums'),KeyboardButton(text='Malls')],
        [KeyboardButton(text='Entertainment'), KeyboardButton(text='Monuments')],
        [KeyboardButton(text='Excursion')],
        [KeyboardButton(text='list of your choices'), KeyboardButton(text='Clear my choices'),KeyboardButton(text='make a route')],
        [KeyboardButton(text='Menu')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

museums_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Atameken'),KeyboardButton(text='EXPO')],
        [KeyboardButton(text='Pyramid'),KeyboardButton(text='National Museum')],
        [KeyboardButton(text='Saken Seifulin'), KeyboardButton(text='Hall of Gold')],
        [KeyboardButton(text='Palace of Independence'), KeyboardButton(text='Has Sanat Art Gallery')],
        [KeyboardButton(text='First President Museum'), KeyboardButton(text='Nazarbayev Center')],
        [KeyboardButton(text='Military-Historical Mus.')],
        [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)

parks_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Burabay'),KeyboardButton(text='Nurzhol')],
        [KeyboardButton(text='Kazakh Eli'),KeyboardButton(text='Atyrau Bridge')],
        [KeyboardButton(text='Arbat'),KeyboardButton(text='Metropolitan Park')],
        [KeyboardButton(text='President Park'),KeyboardButton(text='Zheruyik')],
        [KeyboardButton(text='Triathlon Park'),KeyboardButton(text='EXPO Park')],
        [KeyboardButton(text='Jetysu Park'),KeyboardButton(text='Old Square ')],
        [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)

entertainment_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Jungle'),KeyboardButton(text='Oceanarium Ailand')],
        [KeyboardButton(text='Ferris Wheel Ailand'),KeyboardButton(text='Exotarium Ailand')],
        [KeyboardButton(text='Arbat'),KeyboardButton(text='Metropolitan Park')],
        [KeyboardButton(text='President Park'),KeyboardButton(text='Zheruyik')],
        [KeyboardButton(text='Triathlon Park'),KeyboardButton(text='EXPO Park')],
        [KeyboardButton(text='Jetysu Park'),KeyboardButton(text='Old Square ')],
        [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)
monuments_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Baiterek'),KeyboardButton(text='Alzhir')],
        [KeyboardButton(text='Arc de Triumph')],
        [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)

malls_kb= ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Khan Shatyr')],
    [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]
    ],
    resize_keyboard=True
)

excursion_kb= ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Astana Opera Excursion'),KeyboardButton(text='River Ishim Excursion')],
    [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]],
    resize_keyboard=True
)

religious_kb= ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Hazrat Sultan'),KeyboardButton(text='Nur-Astana Mosque')],
              [KeyboardButton(text='Svyat Uspenskyi')],
              [KeyboardButton(text='Menu'),KeyboardButton(text='Back')]],
              resize_keyboard=True
)

confirmation_kb= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Share with your location',request_location=True),KeyboardButton(text='Menu')]
    ],
    resize_keyboard=True
)