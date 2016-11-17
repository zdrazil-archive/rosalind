string = 'GXmAbvZU6PCxruaOhVnIEKQs61EIvx25xitDR3HnkDYmdwifKZUF43qbDva2aieWVSSaxicolaex2FUFiIGrMY4U1bBOSpoFJLIgDkzzB3Gc1FeLbdhBC0crispusfaJ5U4BpUExQ9qTaMQr2svvyughEx2rjsJ5ziPzGQH4ydG.'
array = [[66, 73], [118, 124]]
result = ""

for number in array:
    if result == "":
        result = string[number[0]:number[1] + 1]
    else:
        result = result + ' ' + string[number[0]:number[1] + 1]
print(result)