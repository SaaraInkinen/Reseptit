def one():
    end = int(input("Haluatko uuden reseptin? (0 = kyllä, 1 = ei)")
    return end

def two():
    end = int(input("Haluatko uuden reseptin? (0 = kyllä, 1 = ei)")
    return end

def three():
    end = int(input("Haluatko uuden reseptin? (0 = kyllä, 1 = ei)")
    return end

def main():
    print("Hei! Täältä saat ideoita, mitä leivot tai teet ruuaksi.")
    end = int(0)
    while(end != 1):
        print("Sinulla on seuraavat vaihtoehdot:")
        print("1. Kaikki")
        print("2. Suolaiset")
        print("3. Makeat")
        choice = int(input("Valitse syöttämällä numero: "))
        if (choice == 1):
            end = one(end)
        elif (choice == 2):
        elif (choice == 3):
        else:
            print("Valitse kokonaisluku välillä 1-3")
        
main()
    
