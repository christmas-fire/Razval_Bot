from aiogram import Router, types

router_inline_mode = Router()


# todo Сделать нормальный текст к этой хуйне блять
# region Инлайн-режим
@router_inline_mode.inline_query()
async def inline_mode_order(inline_query: types.InlineQuery):
    text = "Сделайте заказ прямо сейчас, перейдя по ссылке в моего бота: @Razvaaal_bot"

    results = [
        types.InlineQueryResultArticle(
            id='1',
            title="RazvalBot👾",
            description=f"🎨 Ваш бот-художник | Эскизы на заказ\n"
                        f"🖌 Тату-эскизы, портреты, иллюстрации\n"
                        f"📩 Нажмите /start, чтобы начать\n",
            input_message_content=types.InputTextMessageContent(
                message_text=text,
                parse_mode="HTML"
            ),
            thumb_url="https://i.pinimg.com/564x/4c/88/b9/4c88b90d34f317b1d17e93e12d1e809e.jpg",
            thumb_width=48,
            thumb_height=48
        )
    ]
    button = types.InlineQueryResultsButton(text="Сделать заказ",
                                            start_parameter="start")
    await inline_query.answer(results=results,
                              button=button,
                              is_personal=True)

# endregion Инлайн-режим
