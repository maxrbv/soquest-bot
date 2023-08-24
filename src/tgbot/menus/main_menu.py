from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MENU_GET_DATA = '✅Получить данные'
MENU_EDIT_ADDRESS = 'Изменить адрес'
MENU_EDIT_SIGNATURE = 'Изменить подпись'
MENU_GET_SIGNATURE_GUIDE = 'Как получить подпись?'
MENU_CONTACT_DEVELOPER = 'Связаться с разработчиком'

btnGetData = InlineKeyboardButton(MENU_GET_DATA, callback_data='btn_get_data')
btnEditAddress = InlineKeyboardButton(MENU_EDIT_ADDRESS, callback_data='btn_edit_address')
btnEditSignature = InlineKeyboardButton(MENU_EDIT_SIGNATURE, callback_data='btn_edit_signature')
btnGetSignatureGuide = InlineKeyboardButton(MENU_GET_SIGNATURE_GUIDE, url='https://teletype.in/@maxrbv/soquest-bot-signature')
btnContactDeveloper = InlineKeyboardButton(MENU_CONTACT_DEVELOPER, url='https://t.me/UrwaLeason')

mainMenu = InlineKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnGetData)
mainMenu.add(btnEditAddress, btnEditSignature)
mainMenu.add(btnGetSignatureGuide)
mainMenu.add(btnContactDeveloper)
