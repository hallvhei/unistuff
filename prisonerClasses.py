import random as rnd
class Player:

    playercount = 0

    def __init__(self, name):
        self.name = name.lower()
        Player.playercount += 1

    def Cooperator(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Cooperator chosen!")

        print("Current round: {}".format(current_round))
        decision = 0
        if decision != 1 and decision != 0:
            print("ERROR. No value decided!")
            return(3)

        return decision

    def Defector(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Defector chosen")

        decision = 1
        if decision != 1 and decision != 0:
            print("ERROR. No value detected")
            return

        return decision

    def Randomy(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Randomy chosen")

        decision = rnd.randint(0,1)
        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision

    def Opposite(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Opposite chosen!")

        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            decision = rnd.randint(0,1)
        elif previous_games[other_player][current_round-1] == 0:
            decision = 1
        elif previous_games[other_player][current_round-1] == 1:
            decision = 0

        return decision

    def MeFirst(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("MeFirst chosen!")

        if player_number == 0:
            decision = 0
        elif player_number == 1:
            decision = 1

        return decision

    def HappyFlop(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("HappyFlop chosen!")
            decision = 0
        else:
            decision = (current_round) % 2

        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision


    def AngryFlop(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("AngryFlop chosen!")
            decision = 1
        else:
            decision = (current_round+1) % 2

        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision

    def Grudgy(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Grudgy chosen!")

        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if 1 in previous_games[other_player]:
            decision = 1
        else:
            decision = 0

        return decision

    def Tit4Tat(self, previous_games, player_number, current_round):
        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            print("Tit4tat chosen!")
            decision = 0
        elif current_round != 0:
            #print("Other player: {} Current round: {}".format(other_player,current_round))
            decision = previous_games[other_player][current_round-1]

        return decision

    def Tit42Tat(self, previous_games, player_number, current_round):
        # Tit42Tat retaliates if any of the two previous plays by the opponent were defections
        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            print("Tit42tat chosen!")
            decision = 0
        elif current_round == 1:
            decision = previous_games[other_player][current_round-1]
        elif current_round >= 2:
            if 1 in previous_games[other_player][(current_round-2):]:
                decision = 1
            else:
                decision = 0
        else:
            decision = 0

        return decision

    def Trapper(self, previous_games, player_number, current_round):
        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            print("Trapper chosen!")
            decision = 0
        elif current_round >= 1 and (current_round % 3) == 0:
            decision = 1
        else:
            decision = previous_games[other_player][current_round-1]

        return decision

    def SmartTrapper(self, previous_games, player_number, current_round):
        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            print("SmartTrapper chosen!")
            decision = 0
        elif current_round >= 1 and (current_round % 3) == 0:
            decision = 1
        elif current_round > 1 and (current_round % 3) == 1:
            decision = 1

        else:
            decision = previous_games[other_player][current_round-1]

        return decision


    def Play(self, previous_games, player_number, current_round):
        for i in range(10):
            n = str(i)
            if self.name == "cooperator" or self.name == ("cooperator" + n):
                return self.Cooperator(previous_games, player_number, current_round)

            elif self.name == "defector" or self.name == ("defector" + n):
                return self.Defector(previous_games, player_number, current_round)

            elif self.name == "randomy" or self.name == ("randomy" + n):
                return self.Randomy(previous_games, player_number, current_round)

            elif self.name == "opposite" or self.name == ("opposite" + n):
                return self.Opposite(previous_games, player_number, current_round)

            elif self.name == "mefirst"  or self.name == ("mefirst" + n):
                return self.MeFirst(previous_games, player_number, current_round)

            elif self.name == "happyflop" or self.name == ("happyflop" + n):
                return self.HappyFlop(previous_games, player_number, current_round)

            elif self.name == "angryflop" or self.name == ("angryflop" + n):
                return self.AngryFlop(previous_games, player_number, current_round)

            elif self.name == "grudgy" or self.name == ("grudgy" + n):
                return self.Grudgy(previous_games, player_number, current_round)

            elif self.name == "tit4tat" or self.name == ("tit4tat" + n):
                return self.Tit4Tat(previous_games, player_number, current_round)

            elif self.name == "tit42tat" or self.name == ("tit42tat" + n):
                return self.Tit42Tat(previous_games, player_number, current_round)

            elif self.name == "trapper" or self.name == ("trapper" + n):
                return self.Trapper(previous_games, player_number, current_round)

            elif self.name == "smarttrapper" or self.name == ("smarttrapper" + n):
                return self.SmartTrapper(previous_games, player_number, current_round)


        print("No strategy chosen!")
        return 3
