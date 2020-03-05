'''ScoreSnake Authoritative Scorekeeping Classes and Network Infrastructure'''

import socket
import json
import time
import threading

class BaseballScorekeeper:
    '''Scorekeeper for Baseball'''

    def __init__(self, serverIP='127.0.0.1'):
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

        # Networking
        self.server = NetworkHandler(serverIP, 42016)
        self.server.send(self.package())

    def package(self):
        '''Package scorekeeper variables into a JSON string.'''
        package = {
            'visitor': self.visitor,
            'home': self.home,
            'inning': self.inning,
            'top': self.top,
            'bottom': self.bottom,
            'balls': self.balls,
            'strikes': self.strikes,
            'outs': self.outs,
            'base1': self.base1,
            'base2': self.base2,
            'base3': self.base3
        }

        return json.dumps(package)

    def update(self):
        '''Update connected server with new score data.'''
        self.server.send(self.package())

    def strike(self):
        self.strikes += 1
        if self.strikes == 3: # Strikeout
            self.reset_count()
            self.out()

        self.update()
        return self.strikes

    def ball(self):
        self.balls += 1
        if self.balls == 4: # Walk
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

        self.update()
        return self.balls

    def out(self):
        self.outs += 1
        if self.outs == 3: # End of At-Bat
            self.advance_game()
            self.outs = 0

        self.update()
        return self.outs

    def minus_strike(self):
        self.strikes -= 1
        if self.strikes < 0:
            self.strikes = 0

        self.update()
        return self.strikes

    def minus_ball(self):
        self.balls -= 1
        if self.balls < 0:
            self.balls = 0

        self.update()
        return self.balls

    def minus_out(self):
        self.outs -= 1
        if self.outs < 0:
            self.outs = 0

        self.update()
        return self.outs

    def reset_strikes(self):
        self.strikes = 0
        self.update()
        return self.strikes

    def reset_balls(self):
        self.balls = 0
        self.update()
        return self.balls

    def reset_count(self):
        return (self.reset_balls(), self.reset_strikes())

    def reset_outs(self):
        self.outs = 0
        self.update()
        return self.outs

    def base1_toggle(self):
        if self.base1:
            self.base1 = False
        else:
            self.base1 = True

        self.update()
        return self.base1

    def base2_toggle(self):
        if self.base2:
            self.base2 = False
        else:
            self.base2 = True

        self.update()
        return self.base2

    def base3_toggle(self):
        if self.base3:
            self.base3 = False
        else:
            self.base3 = True

        self.update()
        return self.base3

    def reset_bases(self):
        self.base1 = False
        self.base2 = False
        self.base3 = False

        self.update()

    def score(self):
        if self.top:
            self.visitor += 1
            self.update()
            return self.visitor
        elif self.bottom:
            self.home += 1
            self.update()
            return self.home

    def minus_score(self):
        if self.top:
            self.visitor -= 1
            if self.visitor < 0:
                self.visitor = 0
            self.update()
            return self.visitor
        elif self.bottom:
            self.home -= 1
            if self.home < 0:
                self.home = 0
            self.update()
            return self.home

    def bottom_inning(self):
        self.bottom = True
        self.top = False

        self.update()
        return (self.inning, self.top, self.bottom)

    def top_inning(self):
        self.top = True
        self.bottom = False

        self.update()
        return (self.inning, self.top, self.bottom)

    def new_inning(self):
        self.inning += 1
        if self.bottom:
            self.update()
            return self.top_inning()

        self.update()
        return (self.inning, self.top, self.bottom)

    def old_inning(self):
        self.inning -= 1
        if self.inning < 1:
            self.inning = 1

        self.update()
        return (self.inning, self.top, self.bottom)

    def advance_game(self):
        if self.top:
            self.bottom_inning()
        elif self.bottom:
            self.new_inning()
        self.reset_count()
        self.reset_bases()

class NetworkHandler:
    '''UDP Server and Network Handler'''

    def __init__(self, server: str, port: int, ping=2.0):
        self.target_ip = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.last_package = None

        self.ping = ping
        self.heartbeat = threading.Thread(target=self.keep_alive)
        self.heartbeat.start()
        self.kill = False

    def send(self, package: str):
        '''Send score data over socket.'''
        self.last_package = bytes(package, 'utf-8')
        self.socket.sendto(self.last_package, (self.target_ip, self.port))

    def keep_alive(self):
        '''Periodically updates server with last package to account for packet loss.'''
        while True:
            time.sleep(self.ping)
            self.socket.sendto(self.last_package, (self.target_ip, self.port))
            if self.kill:
                break

    def stop_heartbeat(self):
        self.kill = True