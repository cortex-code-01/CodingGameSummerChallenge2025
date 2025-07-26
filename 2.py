import sys
import math


class RemainingAgentInfo:
    agent_id: int
    x: int
    y: int
    cooldown: int
    splash_bombs: int
    wetness: int


class AgentInfo:
    agent_id: int
    player: int
    shoot_cooldown: int
    optimal_range: int
    soaking_power: int
    splash_bombs: int


# Win the water fight by controlling the most territory, or out-soak your opponent!

my_id = int(input())  # Your player id (0 or 1)
agent_data_count = int(input())  # Total number of agents in the game
my_agents_data: list[AgentInfo] = []
enemy_agents_data: list[AgentInfo] = []
for i in range(agent_data_count):
    # agent_id: Unique identifier for this agent
    # player: Player id of this agent
    # shoot_cooldown: Number of turns between each of this agent's shots
    # optimal_range: Maximum manhattan distance for greatest damage output
    # soaking_power: Damage output within optimal conditions
    # splash_bombs: Number of splash bombs this can throw this game
    agent_data = AgentInfo()
    agent_data.agent_id, agent_data.player, agent_data.shoot_cooldown, agent_data.optimal_range, agent_data.soaking_power, agent_data.splash_bombs = [
        int(j) for j in input().split()]
    if agent_data.player == my_id:
        my_agents_data.append(agent_data)
    else:
        enemy_agents_data.append(agent_data)

# width: Width of the game map
# height: Height of the game map
width, height = [int(i) for i in input().split()]
for i in range(height):
    inputs = input().split()
    for j in range(width):
        # x: X coordinate, 0 is left edge
        # y: Y coordinate, 0 is top edge
        x = int(inputs[3 * j])
        y = int(inputs[3 * j + 1])
        tile_type = int(inputs[3 * j + 2])


def remaining_agent_is_enemy(agent_id) -> bool:
    for enemy_agent_data in enemy_agents_data:
        if enemy_agent_data.agent_id == agent_id:
            return True
    return False


# game loop
while True:
    agent_count = int(input())  # Total number of agents still in the game
    remaining_enemy_agents_data: list[RemainingAgentInfo] = []
    remaining_my_agents_data: list[RemainingAgentInfo] = []
    highest_wetness_enemy_id = 0
    highest_wetness_enemy_value = 0
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        remaining_agent_data = RemainingAgentInfo()
        remaining_agent_data.agent_id, remaining_agent_data.x, remaining_agent_data.y, remaining_agent_data.cooldown, remaining_agent_data.splash_bombs, remaining_agent_data.wetness = [
            int(j) for j in input().split()]
        if remaining_agent_is_enemy(remaining_agent_data.agent_id):
            remaining_enemy_agents_data.append(remaining_agent_data)
            if remaining_agent_data.wetness > highest_wetness_enemy_value:
                highest_wetness_enemy_id, highest_wetness_enemy_value = remaining_agent_data.agent_id, remaining_agent_data.wetness
        else:
            remaining_my_agents_data.append(remaining_agent_data)

    my_agent_count = int(input())  # Number of alive agents controlled by you

    for i in range(my_agent_count):
        print(str(my_agents_data[i].agent_id) + '; SHOOT ' + str(highest_wetness_enemy_id))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"
