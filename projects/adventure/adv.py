from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Opposite directions that can be traversed.
opposite_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}
visited = set()
path = {}
cache_rooms = list()

while len(visited) < len(room_graph):
    room_id = player.current_room.id
    # If current id has not been logged, add it
    if room_id not in path:
        visited.add(room_id)
        # Fill values with data from get_exits
        path[room_id] = player.current_room.get_exits()

    # if there are no other routes, travel back
    if len(path[room_id]) < 1:
        prev = cache_rooms.pop()
        traversal_path.append(prev)
        player.travel(prev)
    else:
        next_dir = path[room_id].pop()
        traversal_path.append(next_dir)
        cache_rooms.append(opposite_directions[next_dir])
        player.travel(next_dir)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
