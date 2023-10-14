import matplotlib.pyplot as plt
import os
import shutil
from constants import ACTIONS

class PlotAgents:
    def __init__(self, agents_num):
        self.agents_rewards = [[0] for _ in range(agents_num)]
        self.enable_save = False
        self.counter = 0
        self.initalize_counter()


    def update_agent(self, agent_n, reward):
        if len(self.agents_rewards[agent_n-1]) > 100:
            del self.agents_rewards[agent_n-1][:1]
        self.agents_rewards[agent_n-1].append(reward)

    def plot(self):
        self.enable_save = True
        self.counter += 1
        plt.clf()
        plt.title("Training...")
        plt.xlabel("Number of Games")
        plt.ylabel("Reward")
        for agent_reward in self.agents_rewards:
            plt.plot(agent_reward)
        plt.legend([f"Agent{i}" for i in range(1, len(self.agents_rewards) + 1)], loc='upper left')
    
    def save_plot(self):
        w, h = plt.gcf().get_size_inches()
        plt.gcf().set_size_inches(10, 5)
        if self.enable_save:
            i = 100
            while True:
                if self.counter < i:
                    break
                else:
                    i += 100
            plt.savefig(f"./info_models/reward_plots/reward_plot({i - 100}-{i}).png")
        plt.gcf().set_size_inches(w, h)
        
    def initalize_counter(self):
        if os.path.exists("./info_models/info.txt"):
            with open("./info_models/info.txt", "r") as f:
                lines = f.readlines()
                self.counter = int(lines[1].replace('\n', '').split(' ')[-1])
        
     

def clear_existing_model():
    if os.path.exists("./info_models"):
        shutil.rmtree("./info_models")
    os.makedirs("./info_models")
    os.makedirs("./info_models/reward_plots")
    
def play_step(idx, socket):
    act = ACTIONS[idx]
    socket.sendall(str.encode(act))
