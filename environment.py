import gym


class FarkleEnv(gym.Env):
    __possible_actions = 3
    __state_space_size = 3

    def __init__(self):
        super(FarvleEnv, self).__init__()

        self.action_space = gym.spaces.Discrete(FarkleEnv.__possible_actions)
        self.observation_space = gym.spaces.Discrete(FarkleEnv.__state_space_size)


    def step(self, action):
        # Execute one time step within environment
        # Return observation, reward, done, info
        raise NotImplementedError


    def reset(self):
        # Reset state of environment to initial state
        # Return initial observation
        raise NotImplementedError


    def render(self, mode="human"):
        # Render environment to screen
        raise NotImplementedError

