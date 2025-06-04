from datetime import datetime, timedelta
import random


class HelpFunctions:

    @staticmethod
    def date():
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%d.%m.%Y")

    @staticmethod
    def phone_number():
        operator_code = random.choice(['910', '911', '912', '913', '914', '915', '916', '917', '918', '919'])
        number = ''.join(str(random.randint(0, 9)) for _ in range(7))
        phone = f'+7{operator_code}{number}'
        return phone