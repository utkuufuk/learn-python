while True:
    try:
        favNum = int(input("What's your favourite number?\n"))
        print(1/favNum)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except:
        print("Unidentified Flying Problem")
    finally:
        print("Loop complete.\n")
        


