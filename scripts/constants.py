MAX_MEMORY = 100_000
BATCH_SIZE = 32
LR = 0.00025  # learning rate
GAMMA = 0.99
ACTIONS = ["left", "right", "up", "down", "shoot"]
NUM_ACTIONS = len(ACTIONS)
epsilon_random_frames = 500000