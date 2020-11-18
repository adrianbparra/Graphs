import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # {1: {2,3}}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # to get the total friendships you multiply avg friendship time number of users
        total_friendships = avg_friendships * num_users

        # create a list of possible friendship combinations
        friendship_combinations = []
        # (1,5) == (5,1)

        # add O(n) for combination creation

        for user_id in range(1,num_users + 1):

            for friend_id in range(user_id + 1, num_users + 1):

                friendship_combinations.append((user_id,friend_id))
                
        

        random.shuffle(friendship_combinations)
        # print(len(friendship_combinations))

        # only make the total / 2 of friendship combinations 
        # half of total friendships since 1:2 and 2:1 is two friendships
        friendship_to_make = friendship_combinations[:(total_friendships // 2)]

        # create friendships
        for friendship in friendship_to_make:
            # print(friendship)
            self.add_friendship(friendship[0],friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # get the depht traversal for each frienship path the user_id has
        # user_id = 1
        # {8:[1,8], 9:[1,8,9], 2:[1,8,9,2], 10:[1,8,9,2,10],...}

        # visited will be the paths already visited

        # print("friendships:",self.friendships[user_id])

        # as each new path is encountered add to visited
        path = [user_id]

        visited[user_id] = path

        # print(currentPath)
        

        q = []

        # add the first to a stack
        q.append(path)

        while q:

            current_path = q.pop(0)
            # remove the first path in queue

            current_friend = current_path[-1]
            # get the last friend it the current path

            # print(current_friend)

            # add a path for each friendship
            for friend in self.friendships[current_friend]:
                
                # if that friend has been visited dont do anything
                if friend in visited:
                    continue
                else:
                    # create a new path
                    new_path = list(current_path)
                    # add the new friend to the path
                    new_path.append(friend)
                    # add the path to visited and to the queue to see if ther is more
                    # paths to search for the new user
                    visited[friend] = new_path
                    q.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
