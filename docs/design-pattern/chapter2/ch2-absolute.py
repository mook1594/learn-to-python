class SecretString:

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__pass_phrase
        else:
            return ''

secret_string = SecretString("ACME: Top Secret", "antwerp")
print(secret_string.decrypt("antwerp"))
