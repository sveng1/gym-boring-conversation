import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


class Boring_conversationEnv(gym.Env):

    def __init__(self):

        self.state = 0
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(2)
        self.reward_range = (-5,-2,0)
        self.done = False
        self.info = "No info right now"


    def _transition_prob(self,a):

        s = self.state
        p = {}
        #p[s,a]={(r,s'):P(r,s'|s,a)}
        p[(0,0)] = {(0,0):0.7, (-2,1):0.3}
        p[(0,1)] = {(-5,0):1}
        p[(1,0)] = {(-2,1): 0.95, (0,0):0.05}
        p[(1,1)] = {(-5,0):1}

        return p[(s,a)]


    def step(self, action):

        prob = _transition_prob(action)
        probs = [v for v,k in prob.items()]
        trans = [k for v,k in prob.items()]

        outcome = np.random.choice(range(len(trans)),1,p=probs)
        step = trans[outcome[0]]
        reward, s_next = step
    
        self.state = s_next
        return s_next, reward, self.done, info


    def reset(self):
        self.state = 0

    
    def render(self, mode='human', close=False):
        if self.is_person_angry == 0:
            print("Boring person is happy")
        else:
            print("Boring person is angry with you for not listening")
        
