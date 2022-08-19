from drf_yasg import openapi

tags_speciality = ['Speciality']
tags_category = ['Category']
tags_information = ['Information']
tags_document = ['Document']

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

category_create = {
    'operation_description': '## Создание категории',
    'operation_summary': 'Создание категории',
    'tags': tags_category,
}

category_update = {
    'operation_description': '## Обновление категории',
    'operation_summary': 'Обновление категории',
    'tags': tags_category,
}

category_partial_update = {
    'operation_description': '## Обновление отдельного поля категории',
    'operation_summary': 'Частичное обновление категории',
    'tags': tags_category,
}

category_list = {
    'operation_description': '## Получение списка категориий',
    'operation_summary': 'Получение списка категориий',
    'tags': tags_category,
}

category_retrieve = {
    'operation_description': '## Получение категории',
    'operation_summary': 'Получение категории',
    'tags': tags_category,
}

category_destroy = {
    'operation_description': '## Удаление категории',
    'operation_summary': 'Удаление категории',
    'tags': tags_category,
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

information_create = {
    'operation_description': '## Создание информационных листов или претензий',
    'operation_summary': 'Создание информационных листов или претензий',
    'tags': tags_information,
}

information_update = {
    'operation_description': '## Обновление информационных листов или претензий',
    'operation_summary': 'Обновление информационных листов или претензий',
    'tags': tags_information,
}

information_partial_update = {
    'operation_description': '## Обновление отдельного поля информационного листа или претензии',
    'operation_summary': 'Частичное обновление  информационного листа или претензии',
    'tags': tags_information,
}

information_list = {
    'operation_description': '## Получение списка информационных листов или претензий',
    'operation_summary': 'Получение списка информационных листов или претензий',
    'tags': tags_information,
}

information_retrieve = {
    'operation_description': '## Получение информационных листов или претензий',
    'operation_summary': 'Получение информационных листов или претензий',
    'tags': tags_information,
}

information_destroy = {
    'operation_description': '## Удаление информационного листа или претензии',
    'operation_summary': 'Удаление информационного листа или претензии',
    'tags': tags_information,
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


document_create = {
    'operation_description': '## Создание документа',
    'operation_summary': 'Создание документа',
    'tags': tags_document,
}

document_update = {
    'operation_description': '## Обновление документа',
    'operation_summary': 'Обновление документа',
    'tags': tags_document,
}

document_partial_update = {
    'operation_description': '## Обновление отдельного поля документа',
    'operation_summary': 'Частичное обновление  документа',
    'tags': tags_document,
}

document_list = {
    'operation_description': '## Получение списка документов',
    'operation_summary': 'Получение списка документов',
    'tags': tags_document,
}

document_retrieve = {
    'operation_description': '## Получение документа',
    'operation_summary': 'Получение документа',
    'tags': tags_document,
}

document_destroy = {
    'operation_description': '## Удаление документа',
    'operation_summary': 'Удаление документа',
    'tags': tags_document,
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
