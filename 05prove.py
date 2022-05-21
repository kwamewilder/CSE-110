


def main():

    
    global name
    global play_decision
    global move
    global move_answer
    main.health = 10

    name = input ('Hello there stranger, What name may I call you by? ')

    print ('\n' + name + '!' + ' That\'s a beautiful name.')

    play_decision = input ('\nYou are about embark on a great adventure.\n'
        + 'Once you start, there is no turning back\n'
        + 'So, what do you say?\n'
        + '1. This is not for me\n'
        + '2. I love adventures ')
    play_answer = ['1', '2']

    while play_decision not in play_answer:
        play_decision = input ('You are about embark on a great adventure.\n'
        + 'Once you start, there is no turning back\n'
        +'\n'
        + 'So, what do you say?\n'
        + '1. This is not for me'
        + '2. I love adventures ')

    if play_decision == '1':
        print ('\nOnly cowards hide behind silence - Paulo Coelho')
        main()
              

    move_answer = ['WALK', 'Walk', 'walk', 'RUN', 'Run', 'run']

    move = input ('\nThe road infront of you is straight, narrow and far\n'
        + 'Would you like to WALK or RUN? ')

    while move not in move_answer:
        print ('\nYou can either RUN or WALK here')
        move = input ('The road infront of you is straight, narrow and far\n'
        + 'Would you like to WALK or RUN? ')

    print ('You are at a crossroad now')

    if move == move_answer[0] or move == move_answer[1] or move == move_answer[2]:
        main.health = main.health - 1
        print ('That was a long walk.\n'
            + 'Health -1. Your total health is now ' + str(main.health))

        

    else:
        main.health = main.health - 2
        print ('You run so fast.\n'
            + 'Health -2. Your total health is now ' + str(main.health))

    
        
main()

def direct():

    direction_gen = ['EAST', 'East', 'east', 'NORTH', 'North', 'north', 'WEST', 'West', 'west']

    direction = input ('\nWhich direction would you take?\n'
        + 'EAST\n'
        + 'NORTH\n'
        + 'WEST\n')

    while direction not in direction_gen:
        direction = input ('Which direction would you take?\n'
        + 'EAST\n'
        + 'NORTH\n'
        + 'WEST\n')
    
    if direction == direction_gen[0] or direction == direction_gen[1] or direction == direction_gen[2]:
        if main.health < 15:
            print ('There is a river infront of you. Whiles you are thinking of a way to cross, a fairy appears to you.\n'
                + 'Hello ' + name + '.' + 'In order to cross this river, you will need more health than ' + str(main.health) + '\n'
                + '\nYou are back to the crossroad\n')
            direct()

        else:
            print ('\nThere is a river infront of you. Whiles you are thinking of a way to cross, a fairy appears to you.\n'
                + 'Hello' + name + '.' + 'You are worthy to cross. \n'
                + 'The fairy sprinkles her powder on you and you suddenly find yourself infront of a huge metal gate\n'
                + 'As the gate opens, it get very shiny. So shiny, you can barely watvh.\n'
                + 'Infront of you lies so much gold. More than you would ever need')

            reward_answer = ['LEAVE', 'Leave', 'leave', 'TAKE', 'Take', 'take']

            reward = input ('Would you TAKE all the gold home and live a rich life or LEAVE it behind since it\'s not yours? ')

            while reward not in reward_answer:
                reward = input ('Would you TAKE all the gold home and live a rich life or LEAVE it behind since it\'s not yours? ')

            if reward == reward_answer[0] or reward == reward_answer[1] or reward == reward_answer[2]:
                print ('\nThe fairy appears to you once again\n'
                    + 'Fairy: Oh you Honest and Noble warrior\n'
                    + 'You passed the test so many have failed\n'
                    + 'You are now ordained the king of this land and beyond and all this gold belongs to you\n'
                    'YOU WIN\'! GAME OVER!')
                

            else: 
                main.health = main.health * 0
                print ('\nYou take as much gold as you can and head back with so much joy\n'
                    + 'On your way home, you meet thieves who rob you of the gold and beat you up\n'
                    + 'You are so weak that you can barely crawl back home\n'
                    + 'Your health drops to ' + str(main.health) + '\n'
                    + 'YOU DIED. GAMER OVER\'!')
        


    if direction == direction_gen[3] or direction == direction_gen[4] or direction == direction_gen[5]:
       if move == move_answer[0] or move == move_answer[1] or move == move_answer[2]:
            main.health = main.health - 2
            print ('\nYou keep walking and walking and walking and don\'t come accross anything.\n'
            + 'Health - 2. Your total health is now ' + str(main.health))



       if move == move_answer[3] or move == move_answer[4] or move == move_answer[5]:
            main.health = main.health - 3
            print ('\nYou keep running and running and running and don\'t come accross anything.\n'
            + 'Health -3. Your total health is now ' + str(main.health))

            

       print ('\nYou see a very big golden gate.\n'
            + 'Finally\'!' + ' You say to yourself.\n'
            + 'As you open the gate and enter, you are immediately captured by three Ogres.\n'
            + 'The golden gate mislead you into your doom.\n'
            + 'You are our prisoner they say, unless you tell us the right answer to this riddle\n')

       riddle_answer = ['DARKNESS', 'Darkness', 'darkness']
       
       riddle = input ('The more of this there is, the less you can see: ')

       if riddle == riddle_answer[0] or riddle == riddle_answer[1] or riddle == riddle_answer[2]:
            main.health = main.health + 10
            print ('\nOgre: How did you know the answer to that?\n'
                + 'A clever one you are. Take this to replenish your health\n'
                + 'Health + 10. Your health is now ' + str(main.health)
                + '\nWe are setting you free. Off you go now')
            direct()

            

       else:
            print ('Ogre: Wrong answer\'! '
                + 'You are our prisoner now\n'
                + 'GAME OVER\'!')
        
   


    if direction == direction_gen[6] or direction == direction_gen[7] or direction == direction_gen[8]:
        feed_answer = ['GIVE', 'Give', 'give', 'EAT', 'Eat', 'eat']

        print('\nWhiles walking, you took out a piece of bread from your bag to eat.\n'
            + 'From nowhere appeared this little boy who looked very poor and dirty\n'
            + 'He looked up to you and begged you for a piece of the bread\n'
            + 'The bread is so little and won\'t be enough for the both of you\n')

        feed = input( '\nWhat do you do?\n' + 'GIVE the bread to the poor boy or EAT the bread:')  

        while feed not in feed_answer:
            feed = input( '\nWhat do you do?\n' + 'GIVE the bread to the poor boy or EAT the bread:')  
        
        if feed == feed_answer[0] or feed == feed_answer[1] or feed == feed_answer[2]:
            print ('\nBoy: Thank you noble warrior. Whenever you have to answer a question to save your life,' 
            + 'Health -3. Your health is now ' + str(main.health)
            + '\nRemember it starts with a D and ends with an S')
            direct()

        else:
            main.health = main.health - 5
            print ('Boy: You are not worthy of what lies ahead of you\n'
            + 'Health -5. Your health is now ' + str(main.health))
            direct () 


direct()














