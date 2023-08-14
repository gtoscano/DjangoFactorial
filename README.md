# DjangoFactorial

DjangoAPIFactorial is a web application built using Django and the Django REST Framework. It exposes an API endpoint to calculate the factorial of a given integer. The factorial computation is implemented in C++, which is called by Django.


## Why Call C++ Code from other Programming languages 
C++ is known for its high performance and efficiency, making it a preferred choice for computational tasks. However, integrating C++ code with other platforms and languages can be challenging. This is where tools like SWIG, Pistache, and third-party API frameworks come into play.

#### Using Pistache for RESTful API
- **Web Accessibility**: By wrapping C++ code in a RESTful API, Pistache allows the functionality to be accessed over the web, expanding its reach to web and mobile applications.
- **Language Independence**: Any platform that understands HTTP can interact with the C++ code, making it more versatile and widely usable.
- **Integration with Existing Systems**: Easily fits into web-based ecosystems, enabling C++ code to be part of modern web architectures.
- For RESTful client codes, please check: https://github.com/gtoscano/RestFactorialClients (it has examples in c++, c#, golang, java, julia, octave, python, R, and rust)


#### Using SWIG
- **Cross-Language Compatibility**: SWIG allows you to call C++ code from various programming languages, providing a seamless bridge between C++ and languages like Python, Java, and more.
- **Consistent Interfaces**: By generating uniform interfaces, SWIG ensures that the C++ functionality behaves consistently across different languages.
- **Development Efficiency**: Reduces the need to write redundant code for each language, saving time and effort.
- For a SWIG example, please check: https://github.com/gtoscano/SwigFactorial 


#### Using a third-party RESTful framework (i.e. FastAPI, Django)
- **Modern Web Framework**: FastAPI or Django provide a Pythonic way to call C++ code, offering modern features like type checking and automatic documentation.
- **Performance with Ease**: Combines the performance advantages of C++ with the ease and flexibility of Python, providing an efficient yet developer-friendly approach.
- **Rapid Development**: Enables quick prototyping and development, leveraging C++ for computational tasks while using Python for web handling.
- **DjangoFactorial**: A Django implementation using the Django REST Framework to provide a similar factorial calculation endpoint. The project can be found [here](https://github.com/gtoscano/DjangoFactorial).
- **FastAPIFactorial**: A FastAPI implementation that provides an endpoint to calculate the factorial of a given number. The project can be found [here](https://github.com/gtoscano/FastAPIFactorial).


- For **RESTful client codes**: Implementation of RESTful clients in several programming languages can be din [here](https://github.com/gtoscano/RestFactorialClients). Such a project has examples in c++, c#, golang, java, julia, octave, python, R, and rust.


## Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. **Clone the Repository**: Clone the DjangoAPIFactorial project to your local machine.
```bash
git clone git@github.com:gtoscano/DjangoFactorial.git
```

2. **Navigate to the Project Directory**: Use your terminal to navigate to the directory containing the project.
```bash
cd DjangoFactorial
```

3. **Install Dependencies**: Install Django and the Django REST Framework:

   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations (Optional)**: If there are database migrations to apply, run:

   ```bash
   python manage.py migrate
   ```

## Running the Application

1. **Start the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

## Usage

### Calculate Factorial

To calculate the factorial of a number, navigate to the following URL in your browser:

```
http://127.0.0.1:8000/factorial/{number}/
```

Replace `{number}` with the integer for which you want to calculate the factorial.

## Contributing

If you would like to contribute to this project, please fork the repository, create a feature branch, and send a pull request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out with any questions or feedback.

