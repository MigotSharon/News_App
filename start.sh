export NEWS_API_KEY='5d4ccde6a3854c5c85843f848b341fea'
export SECRET_KEY="MigotSharon"
gunicorn manage:app
python3.6 manage.py server