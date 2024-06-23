#all funk

import re
import phonenumbers
from phonenumbers import geocoder, carrier, timezone




























def phonepars():
    while True:
        phone_number = input("Введите номер телефона (например, +79991234567): ")
        try:
            parsed_number = phonenumbers.parse(phone_number)
            if not phonenumbers.is_valid_number(parsed_number):
                print("Некорректный номер телефона. Попробуйте еще раз.")
                continue
            
            country = geocoder.description_for_number(parsed_number, "ru")
            provider = carrier.name_for_number(parsed_number, "ru")
            timezone_info = timezone.time_zones_for_number(parsed_number)
            country_code = parsed_number.country_code
            national_number = parsed_number.national_number
            is_mobile = "мобильный" if phonenumbers.is_mobile_number(parsed_number) else "стационарный"
            
            phone_info = [
                f"Страна: {country}",
                f"Код страны: +{country_code}",
                f"Номер: {national_number}",
                f"Тип: {is_mobile}",
                f"Провайдер: {provider}",
                f"Часовой пояс: {', '.join(timezone_info)}"
            ]
            print("\n".join(phone_info))
            break
        except (phonenumbers.phonenumberutil.NumberParseException, IndexError):
            print("Некорректный формат номера телефона. Попробуйте еще раз.")