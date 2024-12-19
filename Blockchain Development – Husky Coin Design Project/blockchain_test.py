import unittest
from blockchain import *




class Transactionclass(unittest.TestCase):
    def testTransaction(self):
        """Tests functionality of Transaction method"""
        t1 = Transaction("ben","eric",100)
        self.assertEqual(t1.sending_user, "ben")
        self.assertEqual(t1.receiving_user, "eric")
        self.assertEqual(t1.amount, 100)
        self.assertEqual(t1.transactionorder, ["ben", "eric", 100])



class Blockclass(unittest.TestCase):
    def testBlock(self):
        """Tests functionality of Block method"""
        # Testing Transactionhistory
        b1 = Block()
        self.assertEqual(b1.transactions, []) # Transaction history is empty since block was just created
        t1 = Transaction("ROOT","sam",100)
        t2 = Transaction("ROOT", "pam", 20)
        t3 = Transaction("ROOT", "lam", 9)
        b1.addtransaction(t1) # adding transactions object inside a list inside block.
        b1.addtransaction(t2)
        b1.addtransaction(t3)
        self.assertEqual(b1.transactions, [t1, t2, t3]) # Transactions Have succesfully been added to Block.

        # Testing previous block hash.
        self.assertEqual(b1.previous_block_hash, None) # Previous block hash equals None since there is nothing connected to it
        blockchain = Blockchain()  # Creating a instance of blockchain which automatically generates a genesis block
        blockchain.add_block(b1)  # added new block into chain
        self.assertEqual(b1.previous_block_hash, hash(blockchain._blockchain[0])) # b1 previous hash is now genesis hash



class Ledgerclass(unittest.TestCase):
    def testLedger(self):
        """Tests functionality of Ledger method"""
        l1 = Ledger() # My Ledger hashmap implementation works by having 2 hase tables 1 for usernames and the other for user account balences
        self.assertEqual(l1.ledger_hashmap._user,[[], [], [], [], [], [], [], []]) # Since there are no user yet. Hashmap is empty.
        self.assertEqual(l1.ledger_hashmap._Bankaccount,[[], [], [], [], [], [], [], []]) # since there are no accounts yet. Hashmap is empty
        l1.addnewuser("Ben") # creating new users for my hashmap as examples
        l1.addnewuser("Sam")
        self.assertTrue("Ben" in l1.ledger_hashmap) # Ben has succesfully been added to user hashmap.
        self.assertTrue("Sam" in l1.ledger_hashmap) # Sam has succesfully been added to user hashmap.
        self.assertEqual(l1.curretbalence("Ben"),0) # Both of these users have 0 huskycoins in there account
        self.assertEqual(l1.curretbalence("Sam"),0) # Both of these users have 0 huskycoins in there account

        # Using has funds method to prove ben and sam have no funds right now
        self.assertFalse(l1.has_funds("Ben", 100), False)
        self.assertFalse(l1.has_funds("Sam", 100), False)

        # Using deposit method to give ben and sam some funds
        l1.deposit("Ben", 100) # ben recived 100 huskybucks
        l1.deposit("Sam", 100) # sam recived 100 huskybuck
        self.assertTrue(l1.has_funds("Ben", 100), True)  # Using has funds method to prove ben and sam have funds right now
        self.assertTrue(l1.has_funds("Sam", 100), True)
        self.assertEqual(l1.curretbalence("Ben"),100) # Both of these users have 100 huskycoins in there account
        self.assertEqual(l1.curretbalence("Sam"),100) # Both of these users have 100 huskycoins in there account

        # Using transfer method to transfer Ben's money to Sam.
        l1.transfer("Ben",100)
        l1.deposit("Sam",100)
        self.assertFalse(l1.has_funds("Ben", 100),False)  # Using has funds method to prove ben and sam have funds right now
        self.assertTrue(l1.has_funds("Sam", 100), True)
        self.assertEqual(l1.curretbalence("Ben"), 0)  # Ben now has 0 huskypoints
        self.assertEqual(l1.curretbalence("Sam"), 200)  # Sam now has 200 husckypoints.



class BlockChainclass(unittest.TestCase):
    def testblockchain(self):
        """Tests functionality of Blockchain method"""

        # Create variables used in tests
        chainblock = Blockchain() # Create instance of BlockChain
        t1 = Transaction("ROOT", "Sam", 100) # creating transactions to use in test
        t2 = Transaction("ROOT","lam", 200)
        t3 = Transaction("sam","lam",10000)
        Block1 = Block() # creating blocks to use in tests
        Block1.addtransaction(t1)
        Block2 = Block()
        Block2.addtransaction(t2)
        Block3 = Block()
        Block3.addtransaction(t3)


        # Testing add block
        self.assertEqual(chainblock.add_block(Block1), True) # This came out to be true because the genis block "ROOT" has more than enough funds to transfer to Sam
        self.assertIn(hash(Block1), chainblock._blockchain) # block 1 succesfully added to chain

        self.assertEqual(chainblock._bc_ledger.curretbalence("Sam"),100) # Transaction completed succesfully all currency transfered
        self.assertEqual(chainblock._bc_ledger.curretbalence("ROOT"),999899)

        self.assertEqual(chainblock.add_block(Block2), True) # This came out to be true because the genis block "ROOT" has more than enough funds to transfer to Lam
        self.assertIn(hash(Block2), chainblock._blockchain) # block 2 succesfully added to chain

        self.assertEqual(chainblock._bc_ledger.curretbalence("lam"),200) # Transaction completed succesfully all currency transfered
        self.assertEqual(chainblock._bc_ledger.curretbalence("ROOT"),999699)

        self.assertEqual(chainblock.add_block(Block3), False) # this came out False because needed funds were not satisfied by sender
        self.assertNotIn(Block3, chainblock._blockchain) # block 1 Not added to chain

        self.assertEqual(chainblock._bc_ledger.curretbalence("Sam"),100) # Both users account balences did not change
        self.assertEqual(chainblock._bc_ledger.curretbalence("lam"),200) # Both users account balences did not change


        #Testing validate_chain()
        self.assertEqual(chainblock.validate_chain(),[None]) # Validate_chain without modifying any transaction
        # returns None since no block transactions were modified

        Block1.transactions[0] = ("ROOT", "Sam", 100000000000000) # Modifiying a transaction in Block1 to give sam infinite money

        # Calling validate_chain again after modification
        self.assertEqual(chainblock.validate_chain(),["Block1"]) # Validate_chain successfully determined a transaction in Block 1 was modified




if __name__ == "__main__":
    unittest.main()

