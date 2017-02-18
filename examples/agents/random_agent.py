#!/usr/bin/env bash

import argparse

import gym

class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space
    def act(self, observation, reward, done):
        return self.action_space.sample()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('env_id', nargs='?', default='CartPole-v0', help='Select the environment to run')
    args = parser.parse_args()
    env = gym.make(args.env_id)
    outdir = 'tmp'
    env = gym.wrappers.Monitor(env, directory=outdir, force=True)
    env.seed(0)
    # Remove video.
    # env.close()
    agent = RandomAgent(env.action_space)
    episode_count = 100
    reward = 0
    for i in range(episode_count):
        ob = env.reset()
        done = False
        while not done:
            print(ob)
            action = agent.act(ob, reward, done)
            ob, reward, done, info = env.step(action)
            print(action)
            print(reward)
            print()
        print('done')
        print()
    env.close()
