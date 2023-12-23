import os
import asyncio
from telegram import Bot

TOKEN = ''
bot = Bot(token=TOKEN)
CHAT_ID = ''

async def get_cpu_temperature():
    try:
        # Leer la temperatura de la CPU desde el archivo de temperatura
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temperature = float(file.read()) / 1000.0
        return temperature
    except Exception as e:
        print(f"Error al obtener la temperatura: {e}")
        return None

async def send_temperature_to_telegram(temperature):
    try:
        bot = Bot(token=TOKEN)
        message = f"Temperatura de la CPU: {temperature:.2f} °C"
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print(f"Error al enviar el mensaje a Telegram: {e}")

async def main():
    while True:
        temperature = await get_cpu_temperature()
        if temperature is not None:
            await send_temperature_to_telegram(temperature)
        await asyncio.sleep(300)  # Espera 5 minutos antes de volver a obtener la temperatura

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
