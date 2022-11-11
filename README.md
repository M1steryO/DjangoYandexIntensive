# DjangoYandexIntensive

## Installation

Clone project from github.

```bash
git clone https://github.com/M1steryO/DjangoYandexIntensive.git
```


Create a Virtual Environment and install dependencies.

```bash
cd DjangoYandexIntensive
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

Create file .env for secret data and put data there.

```shell
SECRET_KEY=django_secret_key
DEBUG=True
```

## Usage

To run the application write this command.

```bash
python manage.py runserver
```

After that, the application will be launched on http://127.0.0.1:8000/.

## Database Sctructure
![image](https://user-images.githubusercontent.com/64431505/201345054-e301552a-e01d-4d5f-a04d-13761d551542.png)



## License
[MIT](https://choosealicense.com/licenses/mit/)
