# simple version of 10-3
#name = input("what is your name? ")

#with open('guestbook.txt', 'w') as guestlog:
    #guestlog.write(name.title())
    #print(name.title() + " has been added to the guest log.")


# To keep this in one file give the user a choice.
choice = input("guestbook or programming? \n")
# Only check for guest in the choice. Obvious issues, but otehrwise we do program
if 'guest' in choice:
    # prompt for name and write it to the guest log.
    name = input("what is your name? ")
    print(name.title() + " has been added to the guest log.")
    with open('guestbook.txt', 'w') as guestlog:
        while name != '':
            name = input("what is your name? ")
            guestlog.write(name.title() + "\n")
            print(name.title() + " has been added to the guest log.")
else:
    with open('why.txt', 'w') as whys:
        reason = input("Why do you like programming? ")
        print("So it's because of the " + reason)
        while reason != '':
            reason = input("Why else do you like programming? ")
            whys.write(reason + "\n")
            print("So it's because of the " + reason)
            if reason == '':
                print("Ok all done")


