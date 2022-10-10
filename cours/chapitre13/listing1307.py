english_dutch = { "last":"laatst", "week":"week", "the":"de", "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":"zaag", "first":"eerst", "performance":"optreden", "of":"van", "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij", "one":"een", "world":"wereld", "leading":"leidend", "modern":"modern", "composer":"componist", "composers":"componisten", "two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world ' s leading \
modern composers, Arthur \" Two-Sheds \" Jackson."

slicedtext = sentence.split( " " )

translated = ""
for word in slicedtext:
    for entry in english_dutch:
        if word.lower() == entry or word == entry:
            translated += english_dutch[entry] + " "
        else:
            translated += word + " "
            break

print( translated )
