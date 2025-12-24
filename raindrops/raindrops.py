def convert(number):  
    drops = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }
    ans = ""

    for factor, sound in drops.items():
        if number % factor == 0:
            ans += sound
    return ans or str(number)
    
    # ans = ""
    # if number % 3 == 0:
    #     ans += "Pling"
    # if number % 5 == 0: 
    #     ans += "Plang"
    # if number % 7 == 0:
    #     ans += "Plong"
    # return ans or str(number)