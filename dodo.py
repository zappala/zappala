def task_install():
    """install """
    return {
        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* zappala@internet.byu.edu:/var/www/zappala.byu.edu'],
        }
