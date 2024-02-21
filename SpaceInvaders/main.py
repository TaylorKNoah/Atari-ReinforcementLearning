import gym
import random

# Setup Environment
env = gym.make('SpaceInvaders-v4', render_mode='human')
env.action_space.seed(42)

height, width, channels = env.observation_space.shape
actions = env.action_space.n
print(height, width, channels)
print(actions)

# Little Test w/ no Model
def envTest(episodes: int):
	for episode in range(episodes):
		state = env.reset(seed=42)
		done = False
		score = 0

		while not done:
			env.render()
			action = random.choice([0, 1, 2, 3, 4, 5])
			observation, reward, done, truncated, info = env.step(action)
			score += reward
		print('Episode: {}, Score: {}'.format(episode, score))
	env.close()

envTest(1)