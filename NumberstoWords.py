'''
    Time Complexity - O(logN)
    Space Complexity - O(1)

    where N is the number that is to be converted into words.
'''

#Array to handle all the numbers less than 10.
onesPlace = [ "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ",
            "nine "]

#Array to handle all the numbers between 10 and 20.
lessThanTwenty = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ",
            "nineteen "]

#Array to handle all the numbers less than 100 which are divisible by 10.
tensPlace = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ",
            "ninety "]



#Function to print a given number in words.
def getWords(num) :
    if num == 0 :
        return "Zero"
    
    #stores the number in words.
    valueInWords = ""
    
    #Appending the value at thousands and ten crore's place (in case it is greater than zero).
    croreValue = num // 10000000
    
    if croreValue > 0 :
        valueInWords += handleValLessThanHundred(croreValue, "crore ")

    #Appending the value at thousands and ten lakh's place (in case it is greater than zero).
    lakhValue = (num // 100000) % 100

    if lakhValue > 0 :
        valueInWords += handleValLessThanHundred(lakhValue, "lakh ")
                         

    #Appending the value at thousands and ten thousand's place (in case it is greater than zero).
    thousandValue = (num // 1000) % 100
        
    if thousandValue > 0 :
        valueInWords += handleValLessThanHundred(thousandValue, "thousand ")


    #Appending the value at hundred's place (in case it is greater than zero).
    hundredValue = (num // 100) % 10
    
    if hundredValue > 0 :
        valueInWords += (handleValLessThanHundred(hundredValue, "hundred "))

    #Appending the value at last 2 digits (in case they are greater than 0).
    tensValue = num % 100
                         
    if tensValue > 0 :
        valueInWords += (handleValLessThanHundred(num % 100, ""))

    #Capitalize the first letter.
    ch = valueInWords[0].upper()
    
    return ch + "" + valueInWords[1 : ]



#The value of n this function receives is always <= 100.
def handleValLessThanHundred(number, suffix) :
    valueInWords = ""

    if number <= 9 :
        valueInWords += onesPlace[number]
    elif number <= 19 :
        valueInWords += lessThanTwenty[number % 10]
    else :
        valueInWords += (tensPlace[number // 10] + onesPlace[number % 10])

    #The suffix shall only be added when the value is greater than zero.
    valueInWords += suffix

    return valueInWords