from typing import List


class Mutation:
    """
    Pls Add a description
    """
    def __init__(self):
        self.name = None

    def Mutate(self, fields: List[tuple], subfields: List):
        mod_fields = [f"{i[0]}:\"{i[1]}\"" for i in fields]
        _args = tuple(i.strip("\'") for i in mod_fields)
        newline = "\n"
        result = f"""
        mutation {{
            {self.name}{_args}{{
                {newline.join(i for i in subfields)}
            }}
        }}
        """
        return result.replace("\'", "")


class createDepositAccount(Mutation):
    def __init__(self):
        """
        Create deposit account
        """
        super().__init__()
        self.name = "createDepositAccount"


class Buy(Mutation):
    def __init__(self):
        """
        Buy crypto
        """
        super().__init__()
        self.name = "buy"


# create_account = createDepositAccount()

# print(create_account.Mutate(
#             fields=[('accountName', "tony stark")],
#             subfields=["accountNumber", "accountName", "accountType", "bankName"]
#         ))
