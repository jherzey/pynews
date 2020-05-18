import emoji
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


class AppInteractions:
    startNewsOptions = [
        {"option": "Subscribe for news", "callbackId": "subscribeOption"},
        {"option": "Request news brief", "callbackId": "getFeedOption"},
    ]
    newsCountryOptions = [
        {"option": "English", "callbackId": "en"},
        {"option": "Russian", "callbackId": "ru"},
        {"option": "French ", "callbackId": "fr"},
        {"option": "Italian", "callbackId": "it"},
    ]
    categoryOptions = [
        {"option": "General", "callbackId": "General"},
        {"option": "Business", "callbackId": "Business"},
        {"option": "Health", "callbackId": "Health"},
        {"option": "Technology", "callbackId": "Technology"},
        {"option": "Sports", "callbackId": "Sports"},
        {"option": "Entertainment", "callbackId": "Entertainment"},
    ]

    instantCategoryOptions = [
        {"option": "General", "callbackId": "instantGeneral"},
        {"option": "Business", "callbackId": "instantBusiness"},
        {"option": "Health", "callbackId": "instantHealth"},
        {"option": "Technology", "callbackId": "instantTechnology"},
        {"option": "Sports", "callbackId": "instantSports"},
        {"option": "Entertainment", "callbackId": "instantEntertainment"},
    ]

    deleteCategoryOptions = [
        {"option": "General", "callbackId": "deleteGeneral"},
        {"option": "Business", "callbackId": "deleteBusiness"},
        {"option": "Health", "callbackId": "deleteHealth"},
        {"option": "Technology", "callbackId": "deleteTechnology"},
        {"option": "Sports", "callbackId": "deleteSports"},
        {"option": "Entertainment", "callbackId": "deleteEntertainment"},
    ]

    startReply = emoji.emojize(
        "Hello there, :smile: :woman: \n \n I'm Jessie :information_desk_person: ,  your newscaster.",
        use_aliases=True,
    )
    languageOptionReply = emoji.emojize(
        ":information_desk_person: Great!\nPlease select your  \n country/prefered language :crossed_flags: \n \n:exclamation: Only one language can\n be selected :smile:",
        use_aliases=True,
    )
    newsCategoryReply = emoji.emojize(
        ":information_desk_person: Excellent!\nPlease select your prefered \ncategory. \n\n:100: You may select more than one. ",
        use_aliases=True,
    )
    newCategoryReply = emoji.emojize(
        "Well done ! :smile:\nYou will now recieve regular\nnews updates  :information_desk_person:",
        use_aliases=True,
    )
    addCategoryReply = emoji.emojize(
        "Well done ! :smile:\nYou've successfully added\na new category  :information_desk_person:",
        use_aliases=True,
    )
    pendingNewsReply = emoji.emojize(
        ":information_desk_person: Nice\nYou'll be recieving your news bulletin soon",
        use_aliases=True,
    )
    chosenCategoryReply = emoji.emojize(
        ":information_desk_person: Sorry\nYou've chosen this \n this category already",
        use_aliases=True,
    )
    droppedCategoryReply = emoji.emojize(
        ":information_desk_person: Successful!\nYou won't be recieving \nnews from this category anymore",
        use_aliases=True,
    )
    notSubscriberReply = emoji.emojize(
        ":information_desk_person: Sorry\nYou've not chosen this \n this category yet",
        use_aliases=True,
    )

    def announceNews(category):
        pendingNewsReply = emoji.emojize(
            ":information_desk_person: Nice\nYou'll be your "
            + category
            + " news bulletin soon",
            use_aliases=True,
        )

    startNewsBtns = []
    newsCountryBtns = []
    instantCategoryBtns = []
    deleteCategoryBtns = []
    categoryBtns = []

    for startOption in startNewsOptions:
        startButton = [
            InlineKeyboardButton(
                startOption["option"], callback_data=startOption["callbackId"]
            )
        ]
        startNewsBtns.append(startButton)

    for countryOption in newsCountryOptions:
        countryBtn = [
            InlineKeyboardButton(
                countryOption["option"], callback_data=countryOption["callbackId"]
            )
        ]
        newsCountryBtns.append(countryBtn)

    for categoryOption in categoryOptions:
        categoryBtn = [
            InlineKeyboardButton(
                categoryOption["option"], callback_data=categoryOption["callbackId"]
            )
        ]
        categoryBtns.append(categoryBtn)

    for instantCategoryOption in instantCategoryOptions:
        instantCategoryBtn = [
            InlineKeyboardButton(
                instantCategoryOption["option"],
                callback_data=instantCategoryOption["callbackId"],
            )
        ]
        instantCategoryBtns.append(instantCategoryBtn)

    for deleteCategoryOption in deleteCategoryOptions:
        deleteCategoryBtn = [
            InlineKeyboardButton(
                deleteCategoryOption["option"],
                callback_data=deleteCategoryOption["callbackId"],
            )
        ]
        deleteCategoryBtns.append(deleteCategoryBtn)

    startNewsKeyboard = InlineKeyboardMarkup(startNewsBtns)
    newsCountryKeyboard = InlineKeyboardMarkup(newsCountryBtns)
    categoryKeyboard = InlineKeyboardMarkup(categoryBtns)
    instantCategoryKeyboard = InlineKeyboardMarkup(instantCategoryBtns)
    deleteCategoryKeyboard = InlineKeyboardMarkup(deleteCategoryBtns)
