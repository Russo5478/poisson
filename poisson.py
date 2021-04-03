import sys
import math
import os

def main():
    try:
        def factorial(x):
            if x<=0:
                return 1

            else:
                return math.factorial(x)

        def poisson(mean,value):
            return (pow(2.71828,-mean)* (pow(mean,value))) / factorial(value)

        home_scored = input("Enter average goals scored by Home team: ")
        home_conceded = input("Enter average goals conceded by Home team: ")
        away_scored = input("Enter average goals scored by Away team: ")
        away_conceded = input("Enter average goals conceded by Away team: ")
        league_home_scored = input("Enter average league goals scored by Home teams: ")
        league_away_scored = input("Enter average league goals scored by Away teams: ")


        home_attack_strength = float(home_scored)/float(league_home_scored)
        away_attack_strength = float(away_scored)/float(league_away_scored)

        home_defence_strength = float(home_conceded)/float(league_away_scored)
        away_defence_strength = float(away_conceded)/float(league_home_scored)

        home_mean = float(home_attack_strength)*float(away_defence_strength)*float(league_home_scored)
        away_mean = float(away_attack_strength)*float(home_defence_strength)*float(league_away_scored)

        hg_l = []
        hg_l.clear()

        ag_l = []
        ag_l.clear()

        for i in range(0,16):
            home_goals = poisson(home_mean,i)
            hg_l.append(home_goals)

        for x in range(0,16):
            away_goals = poisson(away_mean,x)
            ag_l.append(away_goals)

        home_win0 = (hg_l[1]*ag_l[0]) + (hg_l[2]*ag_l[0]) + (hg_l[3]*ag_l[0]) + (hg_l[4]*ag_l[0]) + (hg_l[5]*ag_l[0])
        home_win1 = (hg_l[6]*ag_l[0]) + (hg_l[7]*ag_l[0]) + (hg_l[8]*ag_l[0]) + (hg_l[9]*ag_l[0]) + (hg_l[10]*ag_l[0])
        home_win2 = (hg_l[11]*ag_l[0]) + (hg_l[12]*ag_l[0]) + (hg_l[13]*ag_l[0]) + (hg_l[14]*ag_l[0]) + (hg_l[15]*ag_l[0])
        home_win4 = (hg_l[2]*ag_l[1]) + (hg_l[3]*ag_l[1]) + (hg_l[3]*ag_l[2]) + (hg_l[4]*ag_l[1]) + (hg_l[4]*ag_l[2])
        home_win5 = (hg_l[4]*ag_l[3]) + (hg_l[5]*ag_l[1]) + (hg_l[5]*ag_l[2]) + (hg_l[5]*ag_l[3]) + (hg_l[5]*ag_l[4])
        home_win6 = (hg_l[6]*ag_l[1]) + (hg_l[6]*ag_l[2]) + (hg_l[6]*ag_l[3]) + (hg_l[6]*ag_l[4]) + (hg_l[6]*ag_l[5])
        home_win7 = (hg_l[7]*ag_l[1]) + (hg_l[7]*ag_l[2]) + (hg_l[7]*ag_l[3]) + (hg_l[7]*ag_l[4]) + (hg_l[7]*ag_l[5])
        home_win8 = (hg_l[7]*ag_l[6]) + (hg_l[8]*ag_l[1]) + (hg_l[8]*ag_l[2]) + (hg_l[8]*ag_l[3]) + (hg_l[8]*ag_l[4])
        home_win9 = (hg_l[8]*ag_l[5]) + (hg_l[8]*ag_l[6]) + (hg_l[8]*ag_l[7]) + (hg_l[9]*ag_l[1]) + (hg_l[9]*ag_l[2])
        home_win10 = (hg_l[9]*ag_l[3]) + (hg_l[9]*ag_l[4]) + (hg_l[9]*ag_l[5]) + (hg_l[9]*ag_l[6]) + (hg_l[9]*ag_l[7])
        home_win11 = (hg_l[9]*ag_l[8]) + (hg_l[10]*ag_l[1]) + (hg_l[10]*ag_l[2]) + (hg_l[10]*ag_l[3]) + (hg_l[10]*ag_l[4])
        home_win12 = (hg_l[10]*ag_l[5]) + (hg_l[10]*ag_l[6]) + (hg_l[10]*ag_l[7]) + (hg_l[10]*ag_l[8]) + (hg_l[10]*ag_l[9])
        home_win13 = (hg_l[11]*ag_l[1]) + (hg_l[11]*ag_l[2]) + (hg_l[11]*ag_l[3]) + (hg_l[11]*ag_l[4]) + (hg_l[11]*ag_l[5])
        home_win14 = (hg_l[11]*ag_l[6]) + (hg_l[11]*ag_l[7]) + (hg_l[11]*ag_l[8]) + (hg_l[11]*ag_l[9]) + (hg_l[11]*ag_l[10])
        home_win15 = (hg_l[12]*ag_l[1]) + (hg_l[12]*ag_l[2]) + (hg_l[12]*ag_l[3]) + (hg_l[12]*ag_l[4]) + (hg_l[12]*ag_l[5])
        home_win16 = (hg_l[12]*ag_l[6]) + (hg_l[12]*ag_l[7]) + (hg_l[12]*ag_l[8]) + (hg_l[12]*ag_l[9]) + (hg_l[12]*ag_l[10])
        home_win17 = (hg_l[12]*ag_l[11]) + (hg_l[13]*ag_l[1]) + (hg_l[13]*ag_l[2]) + (hg_l[13]*ag_l[3]) + (hg_l[13]*ag_l[4])
        home_win18 = (hg_l[13]*ag_l[5]) + (hg_l[13]*ag_l[6]) + (hg_l[13]*ag_l[7]) + (hg_l[13]*ag_l[8]) + (hg_l[13]*ag_l[9])
        home_win19 = (hg_l[13]*ag_l[10]) + (hg_l[13]*ag_l[11]) + (hg_l[13]*ag_l[12]) + (hg_l[14]*ag_l[1]) + (hg_l[14]*ag_l[2])
        home_win20 = (hg_l[14]*ag_l[3]) + (hg_l[14]*ag_l[4]) + (hg_l[14]*ag_l[5]) + (hg_l[14]*ag_l[6]) + (hg_l[14]*ag_l[7])
        home_win21 = (hg_l[14]*ag_l[8]) + (hg_l[14]*ag_l[9]) + (hg_l[14]*ag_l[10]) + (hg_l[14]*ag_l[11]) + (hg_l[14]*ag_l[12])
        home_win22 = (hg_l[14]*ag_l[13]) + (hg_l[15]*ag_l[1]) + (hg_l[15]*ag_l[2]) + (hg_l[15]*ag_l[3]) + (hg_l[15]*ag_l[4])
        home_win23 = (hg_l[15]*ag_l[5]) + (hg_l[15]*ag_l[6]) + (hg_l[15]*ag_l[7]) + (hg_l[15]*ag_l[8]) + (hg_l[15]*ag_l[9])
        home_win24 = (hg_l[15]*ag_l[10]) + (hg_l[15]*ag_l[11]) + (hg_l[15]*ag_l[12]) + (hg_l[15]*ag_l[13]) + (hg_l[15]*ag_l[14])
        home_win25 = home_win0+home_win1+home_win2+home_win4+home_win5+home_win6+home_win7+home_win8
        home_win26 = home_win9+home_win10+home_win11+home_win12+home_win13+home_win14+home_win15+home_win16+home_win17
        home_win = home_win18+home_win19+home_win20+home_win21+home_win22+home_win23+home_win24+home_win25+home_win26

        draw1 =(hg_l[0]*ag_l[0]) + (hg_l[1]*ag_l[1]) + (hg_l[2]*ag_l[2]) + (hg_l[3]*ag_l[3]) + (hg_l[4]*ag_l[4]) + (hg_l[5]*ag_l[5])
        draw2 =(hg_l[6]*ag_l[6]) + (hg_l[7]*ag_l[7]) + (hg_l[8]*ag_l[8]) + (hg_l[9]*ag_l[9]) + (hg_l[10]*ag_l[10]) + (hg_l[11]*ag_l[11])
        draw3 =(hg_l[12]*ag_l[12]) + (hg_l[13]*ag_l[13]) + (hg_l[14]*ag_l[14]) + (hg_l[15]*ag_l[15])
        draw = draw1 + draw2 + draw3

        away_win0 = (hg_l[0]*ag_l[1]) + (hg_l[0]*ag_l[2]) + (hg_l[0]*ag_l[3]) + (hg_l[0]*ag_l[4]) + (hg_l[0]*ag_l[5])
        away_win1 = (hg_l[0]*ag_l[6]) + (hg_l[0]*ag_l[7]) + (hg_l[0]*ag_l[8]) + (hg_l[0]*ag_l[9]) + (hg_l[0]*ag_l[10])
        away_win2 = (hg_l[0]*ag_l[11]) + (hg_l[0]*ag_l[12]) + (hg_l[0]*ag_l[13]) + (hg_l[0]*ag_l[14]) + (hg_l[0]*ag_l[15])
        away_win4 = (hg_l[1]*ag_l[2]) + (hg_l[1]*ag_l[3]) + (hg_l[2]*ag_l[3]) + (hg_l[1]*ag_l[4]) + (hg_l[2]*ag_l[4])
        away_win5 = (hg_l[3]*ag_l[4]) + (hg_l[1]*ag_l[5]) + (hg_l[2]*ag_l[5]) + (hg_l[3]*ag_l[5]) + (hg_l[4]*ag_l[5])
        away_win6 = (hg_l[1]*ag_l[6]) + (hg_l[2]*ag_l[6]) + (hg_l[3]*ag_l[6]) + (hg_l[4]*ag_l[6]) + (hg_l[5]*ag_l[6])
        away_win7 = (hg_l[1]*ag_l[7]) + (hg_l[2]*ag_l[7]) + (hg_l[3]*ag_l[7]) + (hg_l[4]*ag_l[7]) + (hg_l[5]*ag_l[7])
        away_win8 = (hg_l[6]*ag_l[7]) + (hg_l[1]*ag_l[8]) + (hg_l[2]*ag_l[8]) + (hg_l[3]*ag_l[8]) + (hg_l[4]*ag_l[8])
        away_win9 = (hg_l[5]*ag_l[8]) + (hg_l[6]*ag_l[8]) + (hg_l[7]*ag_l[8]) + (hg_l[1]*ag_l[9]) + (hg_l[2]*ag_l[9])
        away_win10 = (hg_l[3]*ag_l[9]) + (hg_l[4]*ag_l[9]) + (hg_l[5]*ag_l[9]) + (hg_l[6]*ag_l[9]) + (hg_l[7]*ag_l[9])
        away_win11 = (hg_l[8]*ag_l[9]) + (hg_l[1]*ag_l[10]) + (hg_l[2]*ag_l[10]) + (hg_l[3]*ag_l[10]) + (hg_l[4]*ag_l[10])
        away_win12 = (hg_l[5]*ag_l[10]) + (hg_l[6]*ag_l[10]) + (hg_l[7]*ag_l[10]) + (hg_l[8]*ag_l[10]) + (hg_l[9]*ag_l[10])
        away_win13 = (hg_l[1]*ag_l[11]) + (hg_l[2]*ag_l[11]) + (hg_l[3]*ag_l[11]) + (hg_l[4]*ag_l[11]) + (hg_l[5]*ag_l[11])
        away_win14 = (hg_l[6]*ag_l[11]) + (hg_l[7]*ag_l[11]) + (hg_l[8]*ag_l[11]) + (hg_l[9]*ag_l[11]) + (hg_l[10]*ag_l[11])
        away_win15 = (hg_l[1]*ag_l[12]) + (hg_l[2]*ag_l[12]) + (hg_l[3]*ag_l[12]) + (hg_l[4]*ag_l[12]) + (hg_l[5]*ag_l[12])
        away_win16 = (hg_l[6]*ag_l[12]) + (hg_l[7]*ag_l[12]) + (hg_l[8]*ag_l[12]) + (hg_l[9]*ag_l[12]) + (hg_l[10]*ag_l[12])
        away_win17 = (hg_l[11]*ag_l[12]) + (hg_l[1]*ag_l[13]) + (hg_l[2]*ag_l[13]) + (hg_l[3]*ag_l[13]) + (hg_l[4]*ag_l[13])
        away_win18 = (hg_l[5]*ag_l[13]) + (hg_l[6]*ag_l[13]) + (hg_l[7]*ag_l[13]) + (hg_l[8]*ag_l[13]) + (hg_l[9]*ag_l[13])
        away_win19 = (hg_l[10]*ag_l[13])+(hg_l[11]*ag_l[13]) + (hg_l[12]*ag_l[13]) + (hg_l[1]*ag_l[14]) + (hg_l[2]*ag_l[14])
        away_win20 = (hg_l[3]*ag_l[14])+(hg_l[4]*ag_l[14]) + (hg_l[5]*ag_l[14]) + (hg_l[6]*ag_l[14]) + (hg_l[7]*ag_l[14])
        away_win21 = (hg_l[8]*ag_l[14])+(hg_l[9]*ag_l[14]) + (hg_l[10]*ag_l[14]) + (hg_l[11]*ag_l[14]) + (hg_l[12]*ag_l[14])
        away_win22 = (hg_l[13]*ag_l[14])+(hg_l[1]*ag_l[15]) + (hg_l[2]*ag_l[15]) + (hg_l[3]*ag_l[15]) + (hg_l[4]*ag_l[15])
        away_win23 = (hg_l[5]*ag_l[15])+(hg_l[6]*ag_l[15]) + (hg_l[7]*ag_l[15]) + (hg_l[8]*ag_l[15]) + (hg_l[9]*ag_l[15])
        away_win24 = (hg_l[10]*ag_l[15])+(hg_l[11]*ag_l[15]) + (hg_l[12]*ag_l[15]) + (hg_l[13]*ag_l[15]) + (hg_l[14]*ag_l[15])
        away_win25 = away_win0+away_win1+away_win2+away_win4+away_win5+away_win6+away_win7+away_win8+away_win9+away_win10
        away_win26 = away_win11+away_win12+away_win13+away_win14+away_win15+away_win16+away_win17+away_win18+away_win19+away_win20
        away_win = away_win21+away_win22+away_win23+away_win24+away_win25+away_win26


        double_home = (draw + home_win)/2
        double_away = (draw + away_win)/2
        home_away = (home_win + away_win)/2

        over_551 = (hg_l[3]*ag_l[3])+(hg_l[5]*ag_l[1])+(hg_l[1]*ag_l[5])+(hg_l[0]*ag_l[6])+(hg_l[6]*ag_l[0])+(hg_l[2]*ag_l[4])
        over_552 = (hg_l[5]*ag_l[2])+(hg_l[2]*ag_l[5])+(hg_l[4]*ag_l[3])+(hg_l[3]*ag_l[4])+(hg_l[0]*ag_l[7])+(hg_l[7]*ag_l[0])
        over_553 = (hg_l[6]*ag_l[2])+(hg_l[3]*ag_l[5])+(hg_l[5]*ag_l[3])+(hg_l[4]*ag_l[4])+(hg_l[0]*ag_l[8])+(hg_l[8]*ag_l[0])
        over_554 = (hg_l[2]*ag_l[7])+(hg_l[7]*ag_l[2])+(hg_l[3]*ag_l[6])+(hg_l[6]*ag_l[3])+(hg_l[4]*ag_l[5])+(hg_l[5]*ag_l[4])
        over_555 = (hg_l[2]*ag_l[8])+(hg_l[7]*ag_l[3])+(hg_l[3]*ag_l[7])+(hg_l[4]*ag_l[6])+(hg_l[6]*ag_l[4])+(hg_l[5]*ag_l[5])
        over_556 = (hg_l[11]*ag_l[0])+(hg_l[0]*ag_l[11])+(hg_l[10]*ag_l[1])+(hg_l[1]*ag_l[10])+(hg_l[2]*ag_l[9])+(hg_l[8]*ag_l[2])
        over_557 = (hg_l[4]*ag_l[2])+(hg_l[1]*ag_l[6])+(hg_l[6]*ag_l[1])+(hg_l[1]*ag_l[7])+(hg_l[7]*ag_l[1])+(hg_l[2]*ag_l[6])
        over_558 = (hg_l[0]*ag_l[9])+(hg_l[9]*ag_l[0])+(hg_l[1]*ag_l[8])+(hg_l[8]*ag_l[1])+(hg_l[0]*ag_l[10])+(hg_l[10]*ag_l[0])
        over_559 = (hg_l[1]*ag_l[9])+(hg_l[9]*ag_l[1])+(hg_l[9]*ag_l[2])+(hg_l[2]*ag_l[9])+(hg_l[8]*ag_l[3])+(hg_l[3]*ag_l[8])
        over_5510 = (hg_l[4]*ag_l[7])+(hg_l[7]*ag_l[4])+(hg_l[5]*ag_l[6])+(hg_l[6]*ag_l[5])
        over_55 = over_551+over_552+over_553+over_554+over_555+over_556+over_557+over_558+over_559+over_5510

        over_451 = (hg_l[1]*ag_l[4])+(hg_l[4]*ag_l[1])+(hg_l[3]*ag_l[2])+(hg_l[2]*ag_l[3])+(hg_l[0]*ag_l[5])+(hg_l[5]*ag_l[0])
        over_45 = over_451 + over_55

        over_351 = (hg_l[3]*ag_l[1])+(hg_l[1]*ag_l[3])+(hg_l[2]*ag_l[2])+(hg_l[0]*ag_l[4])+(hg_l[4]*ag_l[0])
        over_35 = over_45 + over_351

        over_251 = (hg_l[2]*ag_l[1])+(hg_l[1]*ag_l[2])+(hg_l[0]*ag_l[3])+(hg_l[3]*ag_l[0])
        over_25 = over_251 + over_35

        over_151 = (hg_l[0]*ag_l[2])+(hg_l[2]*ag_l[0])+(hg_l[1]*ag_l[1])
        over_15 = over_151 + over_25

        over_051 = (hg_l[0]*ag_l[1])+(hg_l[1]*ag_l[0])
        over_05 = over_051 + over_15

        under_05 = (hg_l[0]*ag_l[0])

        under_15 = (hg_l[0]*ag_l[1])+(hg_l[1]*ag_l[0])+under_05

        under_25 = (hg_l[1]*ag_l[1])+(hg_l[0]*ag_l[2])+(hg_l[2]*ag_l[0])+under_15

        under_35 = (hg_l[1]*ag_l[2])+(hg_l[2]*ag_l[1])+(hg_l[0]*ag_l[3])+(hg_l[3]*ag_l[0])+under_25

        under_45 = (hg_l[2]*ag_l[2])+(hg_l[3]*ag_l[1])+(hg_l[1]*ag_l[3])+(hg_l[4]*ag_l[0])+(hg_l[0]*ag_l[4])+under_35

        under_55 = (hg_l[3]*ag_l[2])+(hg_l[2]*ag_l[3])+(hg_l[1]*ag_l[4])+(hg_l[4]*ag_l[1])+(hg_l[5]*ag_l[0])+(hg_l[0]*ag_l[5])+under_45

        gg_no1 = (hg_l[0]*ag_l[1])+(hg_l[0]*ag_l[2])+(hg_l[0]*ag_l[3])+(hg_l[0]*ag_l[4])+(hg_l[0]*ag_l[5])+(hg_l[0]*ag_l[0])
        gg_no2 = (hg_l[0]*ag_l[6])+(hg_l[0]*ag_l[7])+(hg_l[0]*ag_l[8])+(hg_l[0]*ag_l[9])+(hg_l[0]*ag_l[10])
        gg_no3 = (hg_l[0]*ag_l[11])+(hg_l[0]*ag_l[12])+(hg_l[0]*ag_l[13])+(hg_l[0]*ag_l[14])+(hg_l[0]*ag_l[15])
        gg_no4 = (hg_l[1]*ag_l[0])+(hg_l[2]*ag_l[0])+(hg_l[3]*ag_l[0])+(hg_l[4]*ag_l[0])+(hg_l[5]*ag_l[0])
        gg_no5 = (hg_l[6]*ag_l[0])+(hg_l[7]*ag_l[0])+(hg_l[8]*ag_l[0])+(hg_l[9]*ag_l[0])+(hg_l[10]*ag_l[0])
        gg_no6 = (hg_l[11]*ag_l[0])+(hg_l[12]*ag_l[0])+(hg_l[13]*ag_l[0])+(hg_l[14]*ag_l[0])+(hg_l[15]*ag_l[0])
        gg_no = gg_no1 + gg_no2 + gg_no3 + gg_no4 + gg_no5 + gg_no6

        gg_yes1 = home_win4+home_win5+home_win6+home_win7+home_win8+home_win9+home_win10+home_win11+home_win12+home_win14+home_win15
        gg_yes2 = home_win16+home_win17+home_win18+home_win19+home_win20+home_win21+home_win22+home_win23+home_win24+home_win13
        gg_yes3 = away_win4+away_win5+away_win6+away_win7+away_win8+away_win9+away_win10+away_win11+away_win12+away_win13+away_win14
        gg_yes4 = away_win15+away_win16+away_win17+away_win18+away_win19+away_win20+away_win21+away_win22+away_win23+away_win24
        gg_yes = gg_yes1 + gg_yes2 + gg_yes3 + gg_yes4

        home_winby1_1 = (hg_l[1]*ag_l[0])+(hg_l[2]*ag_l[1])+(hg_l[3]*ag_l[2])+(hg_l[4]*ag_l[3])+(hg_l[5]*ag_l[4])+(hg_l[6]*ag_l[5])
        home_winby1_2 = (hg_l[7]*ag_l[6])+(hg_l[8]*ag_l[7])+(hg_l[9]*ag_l[8])+(hg_l[10]*ag_l[9])+(hg_l[11]*ag_l[10])+(hg_l[12]*ag_l[11])
        home_winby1 = (hg_l[13]*ag_l[12])+(hg_l[14]*ag_l[13])+(hg_l[15]*ag_l[14])+home_winby1_1+home_winby1_2

        home_winby2_1 = (hg_l[2]*ag_l[0])+(hg_l[3]*ag_l[1])+(hg_l[4]*ag_l[2])+(hg_l[5]*ag_l[3])+(hg_l[6]*ag_l[4])+(hg_l[7]*ag_l[5])
        home_winby2_2 = (hg_l[8]*ag_l[6])+(hg_l[9]*ag_l[7])+(hg_l[10]*ag_l[8])+(hg_l[11]*ag_l[9])+(hg_l[12]*ag_l[10])+(hg_l[13]*ag_l[11])
        home_winby2 = (hg_l[14]*ag_l[12])+(hg_l[15]*ag_l[13])+home_winby2_1+home_winby2_2

        home_winby3_plus1 = (hg_l[3]*ag_l[0])+(hg_l[4]*ag_l[0])+(hg_l[5]*ag_l[0])+(hg_l[4]*ag_l[1])+(hg_l[5]*ag_l[1])+(hg_l[5]*ag_l[2])+(hg_l[10]*ag_l[4])
        home_winby3_plus2 = (hg_l[6]*ag_l[1])+(hg_l[6]*ag_l[2])+(hg_l[6]*ag_l[3])+(hg_l[8]*ag_l[1])+(hg_l[8]*ag_l[2])+(hg_l[8]*ag_l[3])+(hg_l[8]*ag_l[4])
        home_winby3_plus3 = (hg_l[1]*ag_l[7])+(hg_l[2]*ag_l[7])+(hg_l[3]*ag_l[7])+(hg_l[4]*ag_l[7])+(hg_l[8]*ag_l[5])+(hg_l[9]*ag_l[1])+(hg_l[9]*ag_l[2])
        home_winby3_plus4 = (hg_l[9]*ag_l[3])+(hg_l[9]*ag_l[4])+(hg_l[9]*ag_l[5])+(hg_l[9]*ag_l[6])+(hg_l[10]*ag_l[1])+(hg_l[10]*ag_l[2])+(hg_l[10]*ag_l[3])
        home_winby3_plus5 = (hg_l[10]*ag_l[5])+(hg_l[10]*ag_l[6])+(hg_l[10]*ag_l[7])+(hg_l[11]*ag_l[6])+(hg_l[11]*ag_l[7])+(hg_l[11]*ag_l[8])+(hg_l[13]*ag_l[4])
        home_winby3_plus6 = (hg_l[12]*ag_l[6])+(hg_l[12]*ag_l[7])+(hg_l[12]*ag_l[8])+(hg_l[12]*ag_l[9])+(hg_l[13]*ag_l[1])+(hg_l[13]*ag_l[2])+(hg_l[13]*ag_l[3])
        home_winby3_plus7 = (hg_l[13]*ag_l[10])+(hg_l[14]*ag_l[1])+(hg_l[14]*ag_l[2])+(hg_l[14]*ag_l[8])+(hg_l[14]*ag_l[9])+(hg_l[14]*ag_l[10])+(hg_l[14]*ag_l[11])
        home_winby3_plus8 = (hg_l[14]*ag_l[8])+(hg_l[14]*ag_l[9])+(hg_l[14]*ag_l[10])+(hg_l[14]*ag_l[11])+(hg_l[15]*ag_l[1])+(hg_l[15]*ag_l[2])+(hg_l[15]*ag_l[3])+(hg_l[15]*ag_l[4])
        home_winby3_plus9 = (hg_l[15]*ag_l[10])+(hg_l[15]*ag_l[11])+(hg_l[15]*ag_l[12])
        home_winby3_plus10 = home_win1+home_win2+home_win13+home_win15+home_win18+home_win20+home_win23
        home_winby3_plus = home_winby3_plus1+home_winby3_plus2+home_winby3_plus3+home_winby3_plus4+home_winby3_plus5+home_winby3_plus6+home_winby3_plus7+home_winby3_plus8+home_winby3_plus9+home_winby3_plus10

        away_winby1_1 = (hg_l[0]*ag_l[1])+(hg_l[1]*ag_l[2])+(hg_l[2]*ag_l[3])+(hg_l[3]*ag_l[4])+(hg_l[4]*ag_l[5])+(hg_l[5]*ag_l[6])
        away_winby1_2 = (hg_l[6]*ag_l[7])+(hg_l[7]*ag_l[8])+(hg_l[8]*ag_l[9])+(hg_l[9]*ag_l[10])+(hg_l[10]*ag_l[11])+(hg_l[11]*ag_l[12])
        away_winby1 = (hg_l[12]*ag_l[13])+(hg_l[13]*ag_l[14])+(hg_l[14]*ag_l[15])+away_winby1_1+away_winby1_2

        away_winby2_1 = (hg_l[0]*ag_l[2])+(hg_l[1]*ag_l[3])+(hg_l[2]*ag_l[4])+(hg_l[3]*ag_l[5])+(hg_l[4]*ag_l[6])+(hg_l[5]*ag_l[7])
        away_winby2_2 = (hg_l[6]*ag_l[8])+(hg_l[7]*ag_l[9])+(hg_l[8]*ag_l[10])+(hg_l[9]*ag_l[11])+(hg_l[10]*ag_l[12])+(hg_l[11]*ag_l[13])
        away_winby2 = (hg_l[12]*ag_l[14])+(hg_l[13]*ag_l[15])+away_winby2_1+away_winby2_2

        away_winby3_plus1 = (hg_l[0]*ag_l[3])+(hg_l[0]*ag_l[4])+(hg_l[0]*ag_l[5])+(hg_l[1]*ag_l[4])+(hg_l[5]*ag_l[1])+(hg_l[5]*ag_l[2])+(hg_l[4]*ag_l[10])
        away_winby3_plus2 = (hg_l[1]*ag_l[6])+(hg_l[2]*ag_l[6])+(hg_l[3]*ag_l[6])+(hg_l[1]*ag_l[7])+(hg_l[2]*ag_l[7])+(hg_l[3]*ag_l[7])+(hg_l[4]*ag_l[7])
        away_winby3_plus3 = (hg_l[1]*ag_l[8])+(hg_l[2]*ag_l[8])+(hg_l[3]*ag_l[8])+(hg_l[4]*ag_l[8])+(hg_l[5]*ag_l[8])+(hg_l[1]*ag_l[9])+(hg_l[2]*ag_l[9])
        away_winby3_plus4 = (hg_l[3]*ag_l[9])+(hg_l[4]*ag_l[9])+(hg_l[5]*ag_l[9])+(hg_l[6]*ag_l[9])+(hg_l[1]*ag_l[10])+(hg_l[2]*ag_l[10])+(hg_l[3]*ag_l[10])
        away_winby3_plus5 = (hg_l[5]*ag_l[10])+(hg_l[6]*ag_l[10])+(hg_l[7]*ag_l[10])+(hg_l[6]*ag_l[11])+(hg_l[7]*ag_l[11])+(hg_l[8]*ag_l[11])+(hg_l[4]*ag_l[13])
        away_winby3_plus6 = (hg_l[6]*ag_l[12])+(hg_l[7]*ag_l[12])+(hg_l[8]*ag_l[12])+(hg_l[9]*ag_l[12])+(hg_l[1]*ag_l[13])+(hg_l[2]*ag_l[13])+(hg_l[3]*ag_l[13])
        away_winby3_plus7 = (hg_l[10]*ag_l[13])+(hg_l[1]*ag_l[14])+(hg_l[2]*ag_l[14])+(hg_l[8]*ag_l[14])+(hg_l[9]*ag_l[14])+(hg_l[10]*ag_l[14])+(hg_l[11]*ag_l[14])
        away_winby3_plus8 = (hg_l[1]*ag_l[15])+(hg_l[2]*ag_l[15])+(hg_l[3]*ag_l[15])+(hg_l[4]*ag_l[15])
        away_winby3_plus9 = (hg_l[10]*ag_l[15])+(hg_l[11]*ag_l[15])+ (hg_l[12]*ag_l[15])
        away_winby3_plus10 = away_win1+away_win2+away_win13+away_win15+away_win18+away_win20+away_win23
        away_winby3_plus = away_winby3_plus1+away_winby3_plus2+away_winby3_plus3+away_winby3_plus4+away_winby3_plus5+away_winby3_plus6+away_winby3_plus7+away_winby3_plus8+away_winby3_plus9+away_winby3_plus10

        os.system('cls')

        draw_round = round((draw*100),2)
        draw_percent = str(draw_round) + '%'

        homewin_round = round((home_win*100),2)
        homewin_percent = str(homewin_round) + '%'

        awaywin_round = round((away_win*100),2)
        awaywin_percent = str(awaywin_round) + '%'
        
        print('\n')
        print("Home Win possibility: " + homewin_percent)
        print("Away Win possibility: " + awaywin_percent)
        print("Draw possibility: " + draw_percent)

        doublehome_round = round((double_home*100),2)
        doublehome_percent = str(doublehome_round) + '%'

        doubleaway_round = round((double_away*100),2)
        doubleaway_percent = str(doubleaway_round) + '%'

        doublehome_away = round((home_away*100),2)
        doublehome_away_percent = str(doublehome_away) + '%'

        print("\n")
        print("Home or Draw Possibility is: " + doublehome_percent)
        print("Away or Draw Possibility is: " + doubleaway_percent)
        print("Home or Away Possibility is: " + doublehome_away_percent)

        over05_round = round((over_05*100),2)
        over05_percent = str(over05_round) + '%'

        under05_round = round((under_05*100),2)
        under05_percent = str(under05_round) + '%'

        over15_round = round((over_15*100),2)
        over15_percent = str(over15_round) + '%'

        under15_round = round((under_15*100),2)
        under15_percent = str(under15_round) + '%'

        over25_round = round((over_25*100),2)
        over25_percent = str(over25_round) + '%'

        under25_round = round((under_25*100),2)
        under25_percent = str(under25_round) + '%'

        over35_round = round((over_35*100),2)
        over35_percent = str(over35_round) + '%'

        under35_round = round((under_35*100),2)
        under35_percent = str(under35_round) + '%'

        over45_round = round((over_45*100),2)
        over45_percent = str(over45_round) + '%'

        under45_round = round((under_45*100),2)
        under45_percent = str(under45_round) + '%'

        over55_round = round((over_55*100),2)
        over55_percent = str(over55_round) + '%'

        under55_round = round((under_55*100),2)
        under55_percent = str(under55_round) + '%'
               
        print("\n")
        print("Over 0.5 ---> " + over05_percent + "\t Under 0.5 ---> " + under05_percent)
        print("Over 1.5 ---> " + over15_percent + "\t Under 1.5 ---> " + under15_percent)
        print("Over 2.5 ---> " + over25_percent + "\t Under 2.5 ---> " + under25_percent)
        print("Over 3.5 ---> " + over35_percent + "\t Under 3.5 ---> " + under35_percent)
        print("Over 4.5 ---> " + over45_percent + "\t Under 4.5 ---> " + under45_percent)
        print("Over 5.5 ---> " + over55_percent + "\t Under 5.5 ---> " + under55_percent)

        ggno_round = round((gg_no*100),2)
        ggno_percent = str(ggno_round) + '%'

        ggyes_round = round((gg_yes*100),2)
        ggyes_percent = str(ggyes_round) + '%'
     
        print("\n")
        print("BTTS No ---> " + ggno_percent)
        print("BTTS Yes ---> " + ggyes_percent)

        homewinby1_round = round((home_winby1*100),2)
        homewinby1_percent = str(homewinby1_round) + '%'

        homewinby2_round = round((home_winby2*100),2)
        homewinby2_percent = str(homewinby2_round) + '%'

        homewinby3_round = round((home_winby3_plus*100),2)
        homewinby3_percent = str(homewinby3_round) + '%'

        print("\n")
        print("Home to Win by 1 goal Margin: " + homewinby1_percent)
        print("Home to win by 2 goal Margin: " + homewinby2_percent)
        print("Home to Win by 3+ goal Margin: " + homewinby3_percent)

        awaywinby1_round = round((away_winby1*100),2)
        awaywinby1_percent = str(awaywinby1_round) + '%'

        awaywinby2_round = round((away_winby2*100),2)
        awaywinby2_percent = str(awaywinby2_round) + '%'

        awaywinby3_round = round((away_winby3_plus*100),2)
        awaywinby3_percent = str(awaywinby3_round) + '%'

        print("\n")
        print("Away to Win by 1 goal Margin: " + awaywinby1_percent)
        print("Away to win by 2 goal Margin: " + awaywinby2_percent)
        print("Away to Win by 3+ goal Margin: " + awaywinby3_percent)
        
    except (KeyboardInterrupt):
        sys.exit()

main()