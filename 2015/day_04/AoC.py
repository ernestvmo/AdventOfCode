from hashlib import md5

def lowest_hash(secret_key: str, part: str):
    for i in range(10**10):
        hex = md5(str(secret_key + str(i)).encode()).hexdigest()
        if part == '1' and hex[:5] == '00000':
            return i
        if part == '2' and hex[:6] == '000000':
            return i

if __name__ == "__main__":
    secret_key = "bgvyzdsv"
    hash = lowest_hash(secret_key, part='1')
    print(hash)

    hash = lowest_hash(secret_key, part='2')
    print(hash)