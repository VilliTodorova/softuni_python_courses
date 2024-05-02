def main():
    message = input('Say Hi or Bye here: ')
    result = convert(message)
    print(result)


def convert(message):
    happy_emoji = message.replace(':)', '\U0001F642')
    sad_emoji = happy_emoji.replace(':(', '\U0001F641')
    return sad_emoji


main()
