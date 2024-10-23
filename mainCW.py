import os
import pprint

# 1st class will represent the main social media program
class socialMediaNetwork :
    def __init__(self):
        self.social_nw = {}

#The following function opens the file the user chose
    def showFiles(self):
        while True:
            #Program asks the user to input file name in terminal
            file_name = input("Please enter the file name you with to open: ")
            try:
                with open(file_name, 'r') as file:
                    for line in file:
                        names = line.strip().split()
                        # The line.strip() will remove any white spaces in between the values inside the file and then split the values into more.
                        if names:
                            self.social_nw[names[0]] = names[1:]
                    return self.display_social_nw()
            except FileNotFoundError:
                #If name of file isn't found, a FileNotFoundError is shown
                print("The file specified can't be found.")
                choice = input("Would you like to search again? Y/N")
                #The user will be prompted to try again
                #If they press N, the program closes
                if choice == 'n':
                    exit()

    # Displays the social network
    def display_social_nw(self):
        for name, friends in self.social_nw.items():
            print(name + " -> " + ", ".join(friends))

    def recommend_friend(self, individualName):
        # Create an instance of the CommonFriends class and pass the social network dictionary
        common_friends = CommonFriends(self.social_nw)
        # Get a dictionary of common friends count for each member and check if the member is in the common friends count dictionary using an if statement
        common_friends_count = common_friends.get_common_friends()
        if individualName not in common_friends_count:
            # Return message if member not found
            return "Recommended friend for {} is none".format(individualName)
        # Get a list of friend counts for the member
        friend_counts = common_friends_count[individualName]
        # Get a list of friend names
        friend_names = list(common_friends_count.keys())
        # Find the maximum count of common friends
        max_count = max(friend_counts)
        # Return message if no common friends found
        if max_count == 0:
            return "The recommended friend for {} is none".format(individualName)
        # Get the index of the member with the maximum count of common friends
        max_index = friend_counts.index(max_count)
        # Check if the member with the maximum count of common friends is the input member
        if max_index == friend_names.index(individualName):
            # Set the count of common friends to 0
            friend_counts[max_index] = 0
            # Find the next maximum count of common friends
            max_count = max(friend_counts)
            max_index = friend_counts.index(max_count)
        # Get the name of the friend with the maximum count of common friends
        friend_name = friend_names[max_index]
        # Check if the recommended friend is already a friend of the input member
        if friend_name in self.social_nw[individualName]:
            # Return message if the recommended friend is already a friend of the input member
            return "The recommended friend for {} is none".format(individualName)
        return "The recommended friend for {} is {}".format(individualName, friend_name)

class SocialNetworkAnalytics:
    def __init__(self, social_nw):
        #Initialize the class with the social network data
        self.social_nw = social_nw
    def showFriends(self, userName):
        if individualName in self.social_nw:
            print("Friends of {}: {}".format(individualName, ", ".join(self.social_nw[individualName])))
        else:
            print("Error: Member not found.")

    def find_indirect_connections(self):    #This function is to find the indirect connections for all sn members
        indirect_friends = {}
        for member in self.social_nw:
            indirect_friends[member] = set()
            for friend in self.social_nw[member]:
                # Add friends of friend to the indirect friends set
                indirect_friends[member].update(self.social_nw.get(friend, []))
            indirect_friends[member].discard(member)
        return indirect_friends


class CommonFriends:
    def __init__(self, social_nw):
        self.social_nw = social_nw

    def get_common_friends(self):
        #The function is supposed to return a dictionary with keys and values representing the number of common friends with other members.
        common_friends = {}
        for key1, value1 in self.social_nw.items():
            common_friends[key1] = []
            for key2, value2 in self.social_nw.items():
                common = set(value1) & set(value2)  # Finds common friends between the 2 named members
                common_friends[key1].append(
                    len(common))  # Appends the length of mutual friends to the list of common friends of the first member
        return common_friends


# Creating an object of the socialMediaNEtwork class and calling it
sn = socialMediaNetwork()
sn.showFiles()

common_friends = CommonFriends(sn.social_nw)  # Showing the common friend count for all individuals in the network file
print("This is the common friend counter for each friend in the social network")
pprint.pprint(common_friends.get_common_friends())

individualName = input("Please enter an individual's name")
print(sn.recommend_friend(individualName))                  #This prints the recommended friend's name

sna = SocialNetworkAnalytics(sn.social_nw)
# Asking for a member name from the user
individualName = input("Please enter an individual's name")
sna.showFriends(individualName)

indirect_friends = sna.find_indirect_connections()
print("Indirect friends:")
pprint.pprint(indirect_friends)


