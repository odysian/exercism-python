def recite(start_verse, end_verse):
    DAYS_AND_GIFTS = (
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves"),
        ("third", "three French Hens"),
        ("fourth", "four Calling Birds"),
        ("fifth", "five Gold Rings"),
        ("sixth", "six Geese-a-Laying"),
        ("seventh", "seven Swans-a-Swimming"),
        ("eighth", "eight Maids-a-Milking"),
        ("ninth", "nine Ladies Dancing"),
        ("tenth", "ten Lords-a-Leaping"),
        ("eleventh", "eleven Pipers Piping"),
        ("twelfth", "twelve Drummers Drumming"),
    )
    lyrics = []

    for i in range(start_verse - 1, end_verse):
        day = DAYS_AND_GIFTS[i][0]
        line = f"On the {day} day of Christmas my true love gave to me: "
        gifts = []
        for j in range(i, -1, -1):
            gifts.append(DAYS_AND_GIFTS[j][1])
        if i > 0:
            gifts[-1] = "and " + gifts[-1]

        line += ", ".join(gifts)
        lyrics.append(line)
    return lyrics
