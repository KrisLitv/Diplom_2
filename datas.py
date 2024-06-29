
#BASE_URL базовый URL, к которому будут добавляться различные конечные точки для отправки HTTP-запросов.

BASE_URL = 'https://stellarburgers.nomoreparties.site'


#Endpoints - словарь, содержащий пути к различным конечным точкам API.

Endpoints = {
    'USER_REGISTER': '/api/auth/register',
    'USER_LOGIN': '/api/auth/login',
    'USER_INFO': '/api/auth/user',
    'USER_ORDER': '/api/orders',
    'INGREDIENTS_GET': '/api/ingredients',
    'LOGOUT': '/api/auth/logout'
}

#Messages - это словарь, содержащий сообщения об ошибках, которые могут возникнуть при выполнении различных операций с API.

Messages = {
    'USER_ALREADY_EXISTS': 'User already exists',
    'REQUIRED_FIELDS_MISSING': 'Email, password and name are required fields',
    'UNAUTHORIZED': 'You should be authorised',
    'INTERNAL_SERVER_ERROR': 'Internal Server Error',
    'INCORRECT_CREDENTIALS': 'email or password are incorrect',
    'INGREDIENTS_NOT_PROVIDED': 'Ingredient ids must be provided'
}

#INCORRECT_EMAIL и INCORRECT_PASSWORD используются для тестов, чтобы проверить поведение системы при вводе неверных учетных данных.

INCORRECT_EMAIL = 'incorrect_email@ya.ru'
INCORRECT_PASSWORD = '1234'
