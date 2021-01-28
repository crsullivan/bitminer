from hashlib import sha256
import time
import threading

max_nonce = 1000000000000
stop_threads = False

def SHA256(text):

    return sha256(text.encode("ascii")).hexdigest()


def mine1(block_number, transactions, previous_hash, prefix_zeros):

    prefix_str = '0' * prefix_zeros
    start = time.time()
    for nonce in range(1, int(max_nonce / 2)):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        
        if new_hash.startswith(prefix_str):
            print(f"Congratulations!! You mined bitcoin with nonce value: {nonce}.")
            print(new_hash)
            total_time = str(time.time() - start)
            print(f"End mining. Mining took: {total_time} seconds.") 
            global stop_threads

        elif stop_threads: 
                exit()

    raise BaseException(f"Could not find correct nonce value after trying {max_nonce} times...")

def mine2(block_number, transactions, previous_hash, prefix_zeros):

    prefix_str = '0' * prefix_zeros
    start = time.time()
    for nonce in range(int(max_nonce / 2), max_nonce):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            print(f"Congratulations!! You mined bitcoin with nonce value: {nonce}.")
            print(new_hash) 
            total_time = str(time.time() - start)
            print(f"End mining. Mining took: {total_time} seconds.")
            global stop_threads

        elif stop_threads: 
                exit()

    raise BaseException(f"Could not find correct nonce value after trying {max_nonce} times...")

if __name__=='__main__':
    transactions = '''
    sully->joe->13,
    bobby->cassie->29,
    sarah-ella->22
    '''

    difficulty = 6

    t1 = threading.Thread(target=mine1, args=(5, transactions, '2ccf0bd188983e030323c269a5ba49ca77e1a160e60cb5b6ddfc8ff2b9be2148', difficulty))
    t2 = threading.Thread(target=mine2, args=(5, transactions, '2ccf0bd188983e030323c269a5ba49ca77e1a160e60cb5b6ddfc8ff2b9be2148', difficulty))
    t1.start()
    t2.start()

    