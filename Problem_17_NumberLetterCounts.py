#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
#words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
#forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
#letters. The use of "and" when writing out numbers is in compliance with
#British usage.
import time

number_words = {
1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred',
200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred',
600:'six hundred', 700:'seven hundred', 800:'eight hundred',
900:'nine hundred', 1000:'one thousand'
}

def get_words():
    words = ""
    for number in range(1, 1001):
        hundreds = 0
        tens = 0
        ones = 0
        letter_count = 0

        #working only with ones through teens
        if number >= 1 and number <= 19:
            words += number_words[number]

        #working with tens and ones
        elif number >= 20 and number <= 99:
            tens, ones = divmod(number, 10)
            if ones == 0:
                words += number_words[tens*10]
            else:
                words += number_words[tens*10] + number_words[ones]

        #working with hundreds, tens and ones
        elif number >= 100 and number <= 999:
            hundreds, tens = divmod(number, 100)

            if (tens > 10) and (tens < 20) or\
               ((tens % 10) == 0) and (tens > 0):
                words += number_words[hundreds*100] + " and " +\
                number_words[tens]
            elif number % 100 == 0:
                words += number_words[hundreds*100]

            tens, ones = divmod(tens, 10)

            if (tens == 0) and (ones >= 1):
                words += number_words[hundreds*100] + " and " +\
                number_words[ones]
            elif (tens > 20) and (tens <= 99) and (ones >= 1):
                tens = tens // 10
                ones = tens % 10
                words += number_words[hundreds*100] + " and " +\
                number_words[tens] + number_words[ones]
            elif (tens > 1) and (ones > 0):
                words += number_words[hundreds*100] + " and " +\
                number_words[tens*10] + number_words[ones]

            #working with one thousand
        elif number == 1000:
            words += number_words[number]

    letter_count += calc_number_letters(words)
    return letter_count

def calc_number_letters(words):
    count = 0
    if words == "":
        return 0
    for letter in words:
        if letter.isspace():
            continue
        elif letter == "-":
            continue
        else:
            count += 1
    return count

start = time.time()
num_letters = get_words()
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (num_letters,elapsed))
