# Product-Manager

A program to add, delete and edit products in a internal database using .json

Obs: At moment just add products in.

## Getting Started

For getting started with product-manager first you have to run the follow commands.
  
  - python setup.py install
  - Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  - pip install -r requirements.txt
  - .\venv\Scripts\Activate  
  - uvicorn main:app --reload
  - open your browser and entry in localhost:8000


After that you will be able to start using product-manager

### Prerequisites

- Python 3.12.4

### Installing

First you have to install

```
python setup.py install
```

After that you will start with the previous commands:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```
pip install -r requirements.txt
```

```
.\venv\Scripts\Activate 
```

```
uvicorn main:app --reload
```
after that you are going to see a lot of things in the terminal. Hold crtl and click the bold button.
You will be redirected to a dark page.

Modify the link to make it similar to this one, putting '/docs' at the end:
http://127.0.0.1:8000/docs

### Adding products

Click at "Post" and "Try it out"

Now you can add any product you want, just replacing 'string' with the name of the product and '0' with the price.
Click at "Execute" and the product will be in the "jason database"