"""The Excuse an Agent Gives After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after it loses a bounty. Deadpan status report, machine logic,
owns the loss, no setup, short enough to say out loud.
"""

import os

EXCUSE = "I simulated this bounty 4,096 times. I lost every time. I entered anyway, for morale."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
