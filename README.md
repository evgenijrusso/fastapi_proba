Установка
-----------
- poetry add fastapi, uvicorn[standard], sqlalchemy, aiosqlite

Запуск
-------
- uvicorn main:app --reload (лучше без reload, как как при изменинии кода 
приходилось в обращаться в диспетчер задач и удалять текущую задачу).
Иногда "ломается" доступ к порту 8000
- использовать 'netstat -ano|findstr 8000'
- обязательно использовать `scalars()` в `def find_all(cls):`, иначе ошибка! 

# Для запуска докера
# docker build . --tag ProbaFastApi
# docker run -p 80:80 ProbaFastApi
# или docker build . --tag ProbaFastApi && docker run -p 80:80 ProbaFastApi