from parameters.sf_login_creds import SFLoginCreds
import random
import string
import os.path, json


def random_string_for_login(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_login_creds = [
                       SFLoginCreds(username="ed@ed.ed", password="zazazazazaz"),
                       SFLoginCreds(username="ed@ed.ed", password="cheglad3e|")] + [
                       SFLoginCreds(username=random_string_for_login('un', 10),
                                    password=random_string_for_login('pw', 15)) for i in range(2)
                   ]

# define the directory of the current file
current_file_dir = os.path.dirname(os.path.abspath(__file__))
file_with_creds = os.path.join(current_file_dir, "creds.json")
with open(file_with_creds, "w") as output:
    output.write(json.dumps(test_login_creds, default=lambda x: x.__dict__, indent=2))
