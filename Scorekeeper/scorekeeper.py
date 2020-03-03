class BaseballScorekeeper:
    def __init__(self):
        # Scores
        self.visitor = 0
        self.home = 0

        # Inning
        self.inning = 1
        self.top = True
        self.bottom = False

        # Count
        self.balls = 0
        self.strikes = 0
        self.outs = 0

        # Bases
        self.base1 = False
        self.base2 = False
        self.base3 = False

    def strike(self):
        self.strikes += 1
        if self.strikes == 3: # Strikeout
            self.reset_count()
            self.out()
        return self.strikes

    def ball(self):
        self.balls += 1
        if self.outs == 4: # Walk
            self.reset_count()
            if self.base1:
                if self.base2:
                    if self.base3:
                        self.score()
                    else:
                        self.base3 = True
                else:
                    self.base2 = True
            else:
                self.base1 = True
        return self.balls

    def out(self):
        self.outs += 1
        if self.outs == 3: # End of At-Bat
            self.advance_game()
            self.outs = 0
        return self.outs

    def minus_strike(self):
        self.strikes -= 1
        return self.strikes

    def minus_ball(self):
        self.balls -= 1
        return self.balls

    def minus_out(self):
        self.outs -= 1
        return self.outs

    def reset_strikes(self):
        self.strikes = 0
        return self.strikes

    def reset_balls(self):
        self.balls = 0
        return self.balls

    def reset_count(self):
        return (self.reset_balls(), self.reset_strikes())

    def reset_outs(self):
        self.outs = 0
        return self.outs

    def base1_toggle(self):
        if self.base1:
            self.base1 = False
        else:
            self.base1 = True
        return self.base1

    def base2_toggle(self):
        if self.base2:
            self.base2 = False
        else:
            self.base2 = True
        return self.base2

    def base3_toggle(self):
        if self.base3:
            self.base3 = False
        else:
            self.base3 = True
        return self.base3

    def reset_bases(self):
        self.base1 = False
        self.base2 = False
        self.base3 = False

    def score(self):
        if self.top:
            self.visitor += 1
            return self.visitor
        elif self.bottom:
            self.home += 1
            return self.home

    def minus_score(self):
        if self.top:
            self.visitor -= 1
            return self.visitor
        elif self.bottom:
            self.home -= 1
            return self.home

    def bottom_inning(self):
        self.bottom = True
        self.top = False
        return (self.inning, self.top, self.bottom)

    def top_inning(self):
        self.top = True
        self.bottom = False
        return (self.inning, self.top, self.bottom)

    def new_inning(self):
        self.inning += 1
        if self.bottom:
            return self.top_inning()
        return (self.inning, self.top, self.bottom)

    def old_inning(self):
        self.inning -= 1
        return (self.inning, self.top, self.bottom)

    def advance_game(self):
        if self.top:
            self.bottom_inning()
        elif self.bottom:
            self.new_inning()
        self.reset_count()
        self.reset_bases()
    