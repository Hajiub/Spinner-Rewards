import time
import random

class Spinner:
    """
    Generating random rewards based on a predefined list of rewards.
    """

    REWARDS = {
        "NOTHING BOY! GET BACK TO WORK": 0.5,
        "10 mins social media": 0.1,
        "10 mins of anything": 0.05,
        "20 mins of dolingo": 0.1,
        "20 mins of chess": 0.1,
        "read an article": 0.05,
        "two spins": 0.034
    }

    def __init__(self, rewards_text_path: str = "rewards.txt"):

        self.path = rewards_text_path

    def spin(self) -> str:

        return random.choices(list(self.REWARDS.keys()), list(self.REWARDS.values()))[0]

    def reward(self, reward_str: str) -> None:
        with open(self.path, "w") as f:
            f.write(f"Reward: {reward_str} Spun at: {time.ctime(time.time())}" + '\n')

    def main(self) -> None:
        result = self.spin()
        print(result)
        if result != "NOTHING BOY! GET BACK TO WORK":
            self.reward(result)

if __name__ == "__main__":
    spinner = Spinner()
    spinner.main()
