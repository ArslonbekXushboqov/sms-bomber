SERVICES = [
    {
        "service": {
            "name": "Beeline UZ",
            "link": "https://beeline.uz/restservices/api/a2/auth/998{}/otp/send",
            'method': "GET",
            "with_data": {
                "ok": False,
                "data": {},
            },
            "with_param":{
                "ok": False,
                "params": {}
            },
            "HEADER": {},
            }
    },
    {
        "service": {
            "name": "Tashkent UZ",
            "link": "https://www.tashkent.uz/uz/virtual-send-code?phone={}&isSend=true",
            "method": "POST",
            "with_data": {
                "ok": False,
                "data": {},
            },
            "with_param":{
                "ok": False,
                "params": {}
            },
            "HEADER": {},
            }
    },
    {
        "service": {
            "name": "OLX Uzbekistan",
            "link": "https://www.olx.uz/api/v1/user/smsverification/request/",
            "method": "POST",
            "with_data": {
                "ok": True,
                "data": {
                    "countryCode": "+998",
                    "phone": ""
                }
            },
            "with_param":{
                "ok": False,
                "params": {}
            },
            "HEADER": {
                'Authorization': 'Bearer 853c7b5745db4e18604519ac508370d2bc78d4b8'
            }
        }
    },
    {
        "service": {
            "name": "OLCHA Uzbekistan",
            "link": "https://mobile.olcha.uz/api/v2/sendsms",
            "method": "POST",
            "with_data": {
                "ok": True,
                "data": {"phone": 1}
            },
            "with_param":{
                "ok": False,
                "params": {}
            },
            "HEADER": {}
        }
    },
    {
        "service": {
            "name": "ABAD Uzbekistan",
            "link": "https://py.abad.uz/v1.0/api/account/resendcode/",
            "method": "POST",
            "with_data": {
                "ok": True,
                "data": {'username': ''}
            },
            "with_param":{
                "ok": False,
                "params": {}
            },
            "HEADER": {}
        }
    },
    {
        "service": {
            "name": "Texnomart Uz",
            "link": "https://texnomart.uz/user/sugnup",
            "method": 'POST',
            "with_data": {
                'ok': True,
                "data": {
                    "phone":"",
                    "first_name": "Musaffo",
                    "email":"axaxaxascasc@gmail.com",
                    "last_name": "Osmon",
                    "_csrf-frontend":"1CPFlZYjVV9Ijwok2VQH0FuzhpW8YflF2YL5N1w0hticV6b_rmJiDSL4OVOjBzW3FOa-4fYJjwG118xVKgS_6Q=="
                }
            },
            "with_param": {
                "ok": False,
                "params": {}
            },
            "HEADER": {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cookie": "advanced-frontend=1jcn9v0faatjr70314vm4jasmt; _csrf-frontend=dae5b640a5e8317afb712c47d067f415eb3059136a90ca24abb3d9b6ac45b317a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22Htcj8A7Rjw3wzS2gOU8tJhvDlU5bv091%22%3B%7D; _ym_uid=163618075011281723; _ym_d=1636180750; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.1100728646.1636180754; _gid=GA1.2.1424804406.1636180754; _fbp=fb.1.1636180756165.418139122",
                'origin': "https://texnomart.uz",
                "referer": "https://texnomart.uz/ru",
                "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "x-csrf-token": "1CPFlZYjVV9Ijwok2VQH0FuzhpW8YflF2YL5N1w0hticV6b_rmJiDSL4OVOjBzW3FOa-4fYJjwG118xVKgS_6Q=="
            } # Cookie, CSRF Tokenlar VPN orqali olingan :)
        }
    }
]