import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


class Boring_conversationEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):

        self.is_person_angry = 0
        self.action_space = spaces.Discrete(2)

    def transition_prob(a):

        s = self.is_person_angry

        p = {}
        #p[s,a]={(r,s'):P(r,s'|s,a)}
        p[(0,0)] = {(0,0):0.7, (-2,1):0.3}
        p[(0,1)] = {(-5,0):1}
        p[(1,0)] = {(-2,1): 0.95, (0,0):0.05}
        p[(1,1)] = {(-5,0):1}

        return p[(s,a)]


    def step(self, action):

    
        return reward, s_next


    def get_reward(self):
    
    def render(self, mode='human', close=False):
