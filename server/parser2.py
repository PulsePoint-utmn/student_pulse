import requests
import json
import chardet
import pandas as pd


def get_name():
    cookies = {
        'tc01': '0246815d8c8daf68c0ab1e208718f6db',
    }

    headers = {
        'authority': 'utmn.modeus.org',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU',
        'authorization': 'Bearer eyJ4NXQiOiJNalpoTjJVNVkyWTNNVGxpWWpVd01qbGtaR1U0TVdNek1ESXlaamM1Tm1RME0yUTJZVGxpTVEiLCJraWQiOiJkMGVjNTE0YTMyYjZmODhjMGFiZDEyYTI4NDA2OTliZGQzZGViYTlkIiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiRngxenVxSTF5S1ZiQ0xFWGFxNDJpZyIsInN1YiI6IjRhMTMyNjE4LTBkY2QtNDA4Ni05MmNmLWIxZDc0ODBhYjkzNSIsImF1ZCI6WyJzS2lyN1lRbk9VdTRHMGVDZm4zdFR4bkJmemNhIl0sImF6cCI6InNLaXI3WVFuT1V1NEcwZUNmbjN0VHhuQmZ6Y2EiLCJFeHRlcm5hbFBlcnNvbklkIjoiMjg1ODYxYjctNjlhZC00MDE5LTg0YWYtZTliODMyNmNmYzUyIiwiaXNzIjoiaHR0cHM6XC9cL2F1dGgubW9kZXVzLm9yZzo0NDNcL29hdXRoMlwvdG9rZW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiLQpdCw0YHQsNC9INCYLiDQkNCx0YPRiNC10LIiLCJleHAiOjE2OTk2ODcwMzksIm5vbmNlIjoiZFRaZlVrWlRWVll1YzFkcFgwaGtjMW96V2t0cGRVcDBNM1ZpZEhSalVYbzBWRlZmWkdwWFkyNDNNelF0IiwiaWF0IjoxNjk5NjAwNjM5LCJwZXJzb25faWQiOiIxMTE4ZjA0OC0yNDE0LTQyOTAtYWRiZi1kZjI3MTY0YjIyZTYifQ.YG5EGAQ_4r0jC9_-r1_WfCVviUWpbx52YamAFvCPcxhiAi6iII1X3O6qpUzF4e9LaeOg5UGSS2GZEx5GtCxozGaoDRwo1Jfu1L1VxxFSgIhR3rf4x9_Ko0-UYMt-r8gXf-G_kzoAkVsg_lgwb-ai3s726LKuw01TgafMu0yNz3ssisFMHMxnhH2KlIl6u5oLQdE7f0R50BXf7Vpwet1uo3qnKWLeHrculedJcYqLC5i8qft2_QhqBMk5rHiaoSOIk6k9kUnlk_45QUzzqE_KWaEpHoIbw6prWehMPG7pmeNoZnLrD8PiNVP7oylsgfKRdSK64YZUsX_8agtRypo8nA',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'tc01=0246815d8c8daf68c0ab1e208718f6db',
        'origin': 'https://utmn.modeus.org',
        'pragma': 'no-cache',
        'referer': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-08T14:26:24%22%7D&selectedEvent=%22%22&eventsFilter=%7B%22courseUnit%22:%5B%5D,%22cycleRealization%22:%5B%5D,%22room%22:%5B%5D,%22attendee%22:%5B%7B%22key%22:%221118f048-2414-4290-adbf-df27164b22e6%22%7D%5D,%22eventHoldingStatus%22:%5B%5D,%22specialtyCode%22:%5B%5D,%22learningStartYear%22:%5B%5D,%22profileName%22:%5B%5D,%22curriculum%22:%5B%5D,%22typeId%22:%5B%5D%7D',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        #В поле fullname будет поступать имя пользователя, ранее введенное пользователем на нешем сервисе
        'fullName': '',
        'sort': '+fullName',
        'size': 10,
        'page': 0,
    }

    response = requests.post(
        'https://utmn.modeus.org/schedule-calendar-v2/api/people/persons/search',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if response.status_code == 401:
        print("Ошибка 401: Неавторизованный запрос. Проверьте правильность авторизационных данных.")
        # Дополнительные действия, например, перевыполнение аутентификации


    return response


def get_schedule():
    cookies = {
        'tc01': '4134cd3b3d348535ded207f77c64b09f',
    }

    headers = {
        'authority': 'utmn.modeus.org',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU',
        'authorization': 'Bearer eyJ4NXQiOiJNalpoTjJVNVkyWTNNVGxpWWpVd01qbGtaR1U0TVdNek1ESXlaamM1Tm1RME0yUTJZVGxpTVEiLCJraWQiOiJkMGVjNTE0YTMyYjZmODhjMGFiZDEyYTI4NDA2OTliZGQzZGViYTlkIiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiVmMzaGdCWmlqZFpJTC1jaldlRDhJdyIsInN1YiI6IjRhMTMyNjE4LTBkY2QtNDA4Ni05MmNmLWIxZDc0ODBhYjkzNSIsImF1ZCI6WyJzS2lyN1lRbk9VdTRHMGVDZm4zdFR4bkJmemNhIl0sImF6cCI6InNLaXI3WVFuT1V1NEcwZUNmbjN0VHhuQmZ6Y2EiLCJFeHRlcm5hbFBlcnNvbklkIjoiMjg1ODYxYjctNjlhZC00MDE5LTg0YWYtZTliODMyNmNmYzUyIiwiaXNzIjoiaHR0cHM6XC9cL2F1dGgubW9kZXVzLm9yZzo0NDNcL29hdXRoMlwvdG9rZW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiLQpdCw0YHQsNC9INCYLiDQkNCx0YPRiNC10LIiLCJleHAiOjE2OTk3ODc4MTUsIm5vbmNlIjoiVjFab1VVSnRSRkJZYUROcFUxQXlaWFI2YVdoaExWQXpTbmh6VW01UFpHaDRMV3hrTm5KUVgxTnlTM2hFIiwiaWF0IjoxNjk5NzAxNDE1LCJwZXJzb25faWQiOiIxMTE4ZjA0OC0yNDE0LTQyOTAtYWRiZi1kZjI3MTY0YjIyZTYifQ.SndfueJLGaEqTf2lz5oqC0uQ41nm7yFBLLprw22Bsrq-JdhMydpURJMoidTymmtrmAU4ARcTL09Wh83OfUW_9gdVXsdP-40BNrzyMRLgrvsrM_48B-JPSF_dvtYP5Njj9iavxX4Y8R8wOJIk0wTpzPsHfRYNCNZbRFmyaQiUYS6V_izPR0Qp5UmepaSezOz75bx6tsuhMSYzYJ114Y5JxYhVj-z2BmdITJotSQor33GWrXnB6BW8aDzIEeG4dUALpRpwEkc0eTsbd_9Y2ZbgFM-fAVCW-X14CdaJkwyLhD420Y_gHN_Odml0DQnRNCbsxaQ2dX5UJBxizGB9fJaPwA',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'tc01=4134cd3b3d348535ded207f77c64b09f',
        'origin': 'https://utmn.modeus.org',
        'pragma': 'no-cache',
        'referer': 'https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-01T00:00:00%22%7D&selectedEvent=%22%22&eventsFilter=%7B%22courseUnit%22:%5B%5D,%22cycleRealization%22:%5B%5D,%22room%22:%5B%5D,%22attendee%22:%5B%5D,%22eventHoldingStatus%22:%5B%5D,%22specialtyCode%22:%5B%5D,%22learningStartYear%22:%5B%5D,%22profileName%22:%5B%5D,%22curriculum%22:%5B%5D,%22typeId%22:%5B%5D%7D&grid=%22Grid.05%22',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'size': 500,
        'timeMin': '2023-10-29T19:00:00Z',
        'timeMax': '2023-11-05T19:00:00Z',
        'attendeePersonId': [
            #Id, полученный первым запросом
            '0d0aede8-19d2-11e0-8351-101111111111',
        ],  
    }

    response = requests.post(
        'https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/search?tz=Asia/Tyumen&authAction=',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 401:
        print("2. Ошибка 401: Неавторизованный запрос. Проверьте правильность авторизационных данных.")
        # Дополнительные действия, например, перевыполнение аутентификации


    return response




def convert_windows1251_to_windows1252(data):
    if isinstance(data, dict):
        return {key: convert_windows1251_to_windows1252(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_windows1251_to_windows1252(item) for item in data]
    elif isinstance(data, str):
        return data.encode('windows-1251').decode('windows-1252', errors='replace')
    else:
        return data

# ...

def write_json(response, name):
    data = response.json()
    with open(f'./{name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)



def merge_tables_from_json(json_data):
    # Загрузка JSON данных
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Извлечение данных из таблиц events и course-unit-realizations
    events_data = data.get("events", [])
    course_unit_data = data.get("course-unit-realizations", [])

    # Преобразование данных в pandas DataFrame
    events_df = pd.json_normalize(events_data)
    course_unit_df = pd.json_normalize(course_unit_data)

    # Объединение таблиц по индексам с учетом связи один ко многим
    merged_df = pd.merge(events_df, course_unit_df, left_on='course-unit-realization.href', right_on='id', how='left', suffixes=('_event', '_course'))

    # Отбор нужных полей
    result_df = merged_df[['name_event', 'start', 'end', 'nameShort_course']]

    # Переименование столбцов
    result_df.columns = ['event_name', 'start_time', 'end_time', 'course_name']

    # Преобразование DataFrame в словарь
    result_dict = result_df.to_dict(orient='records')

    return result_dict

# Применяем функцию к вашему запросу
response = get_schedule()
result = merge_tables_from_json(response.json())
print(result)





# write_json(response=response, name="abc1")
# convert_windows1251_to_windows1252(response.text)
# write_json(response=response, name="abc2")


response = get_schedule()
result = merge_tables_from_json(response.json())
print(result)

