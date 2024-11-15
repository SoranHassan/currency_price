from telethon import TelegramClient as Client
from khayyam import JalaliDate
from telethon import events
from handlers import *
import config


bot = Client("self",
             api_id=config.API_ID,
             api_hash=config.HASH_ID)

@bot.on(events.NewMessage(outgoing=True, pattern=r".cmds"))
async def show_command(event):

    print("Req To start")
    print(time_request())

    text = commands()
    
    await bot.edit_message(event.message, message=f"**{text}**\n")

@bot.on(events.NewMessage(outgoing=True, pattern=r".dos"))
async def dollar_soleymani(event):

    name = 'dollar_soleymani'
    print(f"Req To Dollar/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"💵USD/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".dof"))
async def dollar_free_market(event):

    name = 'dollar_rl'
    print(f"Req To Dollar Free's Market/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"💵USD/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".doc"))
async def dollar_canada(event):

    name = 'cad'
    print(f"Req To Canada's Dollar/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"🇨🇦USD/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".eur"))
async def euro(event):

    name = 'eur'
    print(f"Req To EUR/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"🇪🇺EUR/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".chf"))
async def frank_ch(event):

    name = 'chf'
    print(f"Req To CHF/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"🇨🇭CHF/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".gbp"))
async def pound_uk(event):

    name = 'gbp'
    print(f"Req To GBP/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"💷GBP/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".iqd"))
async def dinar_iraq(event):

    name = 'iqd'
    print(f"Req To IQD/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"🇮🇶IQD/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".try"))
async def lir_turkey(event):

    name = 'try'
    print(f"Req To TRY/IR\n{time_request()}")
    price, time = get_data(name)[0], get_data(name)[1]
    text = f"🇹🇷TRY/IR {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".btc"))
async def bitcoin(event):

    name = 'bitcoin'
    print(f"Req To BTC/USD\n{time_request()}")
    price, time = get_data_crypto(name)[0], get_data_crypto(name)[1]
    text = f"🪙BTC/USD {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".mgl"))
async def mesghal(event):

    name = 'mesghal'
    print(f"Req To GOLD/IR\n{time_request()}")
    price, time = get_data_gold(name)[0], get_data_gold(name)[1]
    text = f"**MESGHAL {price}**"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".bhr"))
async def sekeh_bahar(event):

    name = 'sekeb'
    print(f"Req To BAHAR/IR\n{time_request()}")
    price, time = get_data_gold(name)[0], get_data_gold(name)[1]
    text = f"**BAHAR AZADI {price}**"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".imm"))
async def sekeh_emami(event):

    name = 'sekee'
    print(f"Req To IMM/IR\n{time_request()}")
    price, time = get_data_gold(name)[0], get_data_gold(name)[1]
    text = f"**EMAMI {price}**"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".eth"))
async def etherium(event):

    name = 'ethereum'
    print(f"Req To ETH/USD\n{time_request()}")
    price, time = get_data_crypto(name)[0], get_data_crypto(name)[1]
    text = f"🪙ETH/USD {price}"
    await bot.edit_message(event.message, message=f'**Price: {text}\nLast Time: {time}**')

@bot.on(events.NewMessage(outgoing=True, pattern=r".exp"))
async def server_timeout(event):

    dt_start = JalaliDate(1403, 6, 23)
    dt_now = JalaliDate.today()
    dt_end = JalaliDate(1403, 7, 22)

    time_expire = f"**Time Left: {dt_end - dt_now}**"

    await bot.edit_message(event.message, message=f"{time_expire}")







print("Bot is running...")
bot.start()
bot.run_until_disconnected()

