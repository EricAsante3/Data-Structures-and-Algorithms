class Bank:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8  # We never want to rehash down below this many buckets.
        self._n_buckets = 8  # initial size. Good to use a power of 2 here.
        self._len = 0  # Number of items in custom set
        self._user = [[] for i in range(self._n_buckets)]  # List of Users
        self._Bankaccount = [[] for k in range(self._n_buckets)]  # List of Account balances

    # Given in lab
    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        # hash(item) returns a nice "random" integer using item.__hash__()
        # Use % to scale that hash to a number between 0 and n_buckets
        return (hash(item) % self._n_buckets)

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        # Find index of bucket `item` should be in, if it is here (self._find_bucket())
        # return True if item is in bucket, false otherwise
        if item in self._user[self._find_bucket(item)]:
            return True
        else:
            return False


    # Modified by me
    def getaccountbalence(self, user):
        index = self._user[self._find_bucket(user)].index(user) # User and acount hashmap are linked. The index of a user is the same as there balance.
                                                                # So i just find user index and place it in acount list to find there balance
        return self._Bankaccount[self._find_bucket(user)][index]

    def addmoney(self, recuser, amount):
        index = self._user[self._find_bucket(recuser)].index(recuser) # User and account balance Same index.
        self._Bankaccount[self._find_bucket(recuser)][index] = (self.getaccountbalence(recuser) + amount) # found user index. entered acount balence and add amount

    def removemoney(self, recuser, ammount):
        index = self._user[self._find_bucket(recuser)].index(recuser) # User and account balance Same index.
        self._Bankaccount[self._find_bucket(recuser)][index] = self.getaccountbalence(recuser) - ammount # found user index. entered acount balence and removed amount


    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored - they do not increase the length, but they do not raise an error."""
        # Check if item already here (`item in self`, since we already implemented self.__contains__()).

        # Return early if it's already here - we don't need to do anything
        if item in self:
            pass
        else:
            self._user[self._find_bucket(item)].append(item) # when new user is added. add 0 in acount hashmap where user index is.
            self._len += 1
            self._Bankaccount[self._find_bucket(item)].append(0)

            if (self._len >= (2 * self._n_buckets)):
                self._rehash(2)

        # Find index of bucket `item` should go in (self._find_bucket())

        # Add item to end of bucket

        # update length

        # rehash if necessary (items >= 2*buckets)

    def remove(self, item):
        """Removes item from CustomSet. Removing an item not in CustomSet should raise a KeyError."""
        # Check if item is in the CustomSet (`item in self`, since we already implemented self.__contains__()).
        # Raise a KeyError if it is not (and include a helpful message)

        # Find index of bucket `item` is in (self._find_bucket())

        # Remove item from bucket

        if self.__contains__(item) == True:
            self._user[self._find_bucket(item)].remove(item)
            self._len -= 1
            if self._n_buckets > 8:
                if (self._len <= ((.50) * self._n_buckets)):
                    self._rehash(.50)
        else:
            raise KeyError

        # update length

        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)

    def _rehash(self, new_buckets):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        self._n_buckets = int(new_buckets * self._n_buckets)

        num = len(self._user)
        templist = []
        tempmoney = []
        # everytime user hashmap is rehased has balnces with new user hashes.
        for i in range(num):
            for k in self._user[i]:
                templist.append(k)

        for i in range(num):
            for k in self._Bankaccount[i]:
                tempmoney.append(k)

        self._Bankaccount.clear()
        self._user.clear()

        self._user = [[] for i in range(self._n_buckets)]
        self._Bankaccount = [[] for i in range(self._n_buckets)]


        # Make a new list of `new_buckets` empty lists
        # Using a for loop, iterate over every bucket in self._L
        for k in range(len(templist)):
            self._user[(hash(templist[k]) % self._n_buckets)].append(templist[k])
            self._Bankaccount[(hash(templist[k]) % self._n_buckets)].append(tempmoney[k])









        # using a for loop, iterate over every item in this bucket
        # Find the index of the new bucket for that item
        # add that item to the correct bucket

        # Update self._L to point to the new list

