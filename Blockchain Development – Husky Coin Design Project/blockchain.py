from hashmap import Bank # Import from hashmap


class Transaction(): # Transaction Class
    """Create transaction orders"""

    def __init__(self, from_user, to_user, amount):
        self.sending_user = from_user # User sending money
        self.receiving_user = to_user # User receiving money
        self.amount = amount # Amount of currency
        self.transactionorder = [self.sending_user, self.receiving_user, self.amount] # Transaction order

    def __repr__(self): # Repr of object
        return str(self.transactionorder)
    
class Block():
    """Creates Block which can contain transaction within it"""

    def __init__(self, transaction=None):
        self.previous_block_hash = None # Previous Hash
        self.transactions = [] # Transaction order list
        if transaction != None: # Adds genesis block to transaction order
            self.addtransaction(transaction)


    def addtransaction(self, transaction): # Add transactions orders to Transaction list
        self.transactions.append(transaction)


class Ledger():
    """Built in hashmap. That can create user and modify there account balances"""

    def __init__(self):
        self.ledger_hashmap = Bank() # Create instance of Hashmap

    def addnewuser(self,username): # Method to add username to Hashmap
        self.ledger_hashmap.add(username)

    def curretbalence(self, username): # Returns account balence of user from hashmap
        return self.ledger_hashmap.getaccountbalence(username)

    def has_funds(self,user,amount): # Has funds method determine if user has enough money in his acount
        if user not in self.ledger_hashmap:
            return False
        else:
            balance = self.ledger_hashmap.getaccountbalence(user)
            return balance >= amount


    def deposit(self, user, amount): # Adds money to account balance in hashmap
        self.ledger_hashmap.addmoney(user,amount)



    def transfer(self, user, amount): # Removes money from account in Hashmap
        self.ledger_hashmap.removemoney(user,amount)


class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self.unhashedtransactions = list() # unhased list of transactions objects
        self.unhashedblock = list() # unhased list of block objects
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()



    def add_block(self, blockinstace):

        for i in blockinstace.transactions: # Goes through every transactions in a block and verfies that sending_user has enough funds for the transaction.
            if self._bc_ledger.has_funds(i.sending_user, i.amount) == False: # if not return false
                return False

        for i in blockinstace.transactions: # if all Sending_user in a block transaction list have funds Procced transaction
            if i.receiving_user not in self._bc_ledger.ledger_hashmap: # If sending_user is sending money to a user not in hashmap. Add reciving user to hashmap.
                self._bc_ledger.addnewuser(i.receiving_user) #adds new user
                self._bc_ledger.deposit(i.receiving_user,i.amount) # Add currency amount to receiving users balence
                self._bc_ledger.transfer(i.sending_user, i.amount) # removes currency amount from Sending users balence
            else:
                self._bc_ledger.deposit(i.receiving_user, i.amount) # Add currency amount to receiving users balence
                self._bc_ledger.transfer(i.sending_user, i.amount) # removes currency amount from Sending users balence

        blockinstace.previous_block_hash = hash(self._blockchain[(len(self._blockchain)-1) ]) # updates blocks previous_block_hash with block ahead of them when added to blockchain
        self._blockchain.append(hash(blockinstace)) # appends block hash to block chain
        self.unhashedblock.append((blockinstace)) # appends block object to unhashed block list

        for i in blockinstace.transactions: # for every transaction in block
            self.unhashedtransactions.append(i) # append to unhased transactions

        return True



    def validate_chain(self):
        orginaltransactions = [] # 2 lists to compare
        currenttransactions = []
        for i in self.unhashedtransactions: # orginal transaction objects get hashed and get added to orginaltransaction list.
            orginaltransactions.append(hash(i))

        for i in self.unhashedblock: # Gets current transaction hashes them and adds them to a list
            for k in i.transactions:
                currenttransactions.append(hash(k))

        Compromisedblocks = [None] # list of compromised blocks. set at None at start

        for (l,k) in zip(orginaltransactions,currenttransactions): # if orginal hash not equal to current hash
            if l != k:
                if None in Compromisedblocks: # remove None from list
                    Compromisedblocks.remove(None)
                Compromisedblocks.append("Block"+str(currenttransactions.index(k)+1)) # append block of compromised transaction.

        return Compromisedblocks






    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.addnewuser(self._ROOT_BC_USER)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
