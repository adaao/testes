def main():
    one_bilion = 1000000000
    counting = 0

    for index in range(0, one_bilion):
        counting += 1
    
    print('{}'.format(counting))

main()