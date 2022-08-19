from drf_yasg import openapi

tags_speciality = ['Speciality']


speciality_create = {
    'operation_description': '## Создание специальности',
    'operation_summary': 'Создание специальности',
    'tags': tags_speciality,
}

speciality_update = {
    'operation_description': '## Обновление специальности',
    'operation_summary': 'Обновление специальности',
    'tags': tags_speciality,
}

speciality_partial_update = {
    'operation_description': '## Обновление отдельного поля специальности',
    'operation_summary': 'Частичное обновление специальности',
    'tags': tags_speciality,
}

speciality_list = {
    'operation_description': '## Получение списка специальностей',
    'operation_summary': 'Получение списка специальностей',
    'tags': tags_speciality,
}

speciality_retrieve = {
    'operation_description': '## Получение специальности',
    'operation_summary': 'Получение специальности',
    'tags': tags_speciality,
}

speciality_destroy = {
    'operation_description': '## Удаление специальности',
    'operation_summary': 'Удаление специальности',
    'tags': tags_speciality,
    'responses': {
        '204': openapi.Response(
            description='Response, when obj deleted.',
            examples={
                'application/json': {
                    'detail': '204 no content',
                }
            }
        )
    }
}