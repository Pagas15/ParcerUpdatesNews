from aiogram import types, Router

other_router = Router()


@other_router.message()
async def echo(message: types.Message) -> None:
    await message.send_copy(chat_id=message.chat.id)
