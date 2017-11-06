import gym
import time


env = gym.make('CartPole-v0')
env.reset()

start = time.time()

for _ in range(400):
	env.render()
	a=env.step(env.action_space.sample()) # take a random action

print(time.time()-start)