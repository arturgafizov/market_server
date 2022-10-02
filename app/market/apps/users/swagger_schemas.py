tags_login_mobile = ['Authorization mobile']

tags_pre_login_create = {
    'operation_description': '## Апи для отправки смс с кодом на телефон пользователя',
    'operation_summary': 'Отправка смс с кодом',
    'tags': tags_login_mobile,
}

tags_login_create = {
    'operation_description': '## Апи для получения смс с кодом пришедшем на телефон и последующим получением токена',
    'operation_summary': 'Апи принимает код с телефона и авторизуешься',
    'tags': tags_login_mobile,
}