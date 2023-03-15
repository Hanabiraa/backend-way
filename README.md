# 🤖🤖🤖 My backend-way 🤖🤖🤖

## Repository where I learn django, python and follow these roadmaps: 
### 1) [Backend roadmap](https://roadmap.sh/backend)
### 2) [Python roadmap](https://roadmap.sh/python)

***

```python
from typing import Tuple

import json
from dataclasses import asdict, dataclass

@dataclass
class Hanabiraa:
    languages: Tuple[str, ...] = ("Python" , "SQL", "HTML5", "CSS", "JS")
    databases: Tuple[str, ...] = ("SQLite", "PostgreSQL", "Redis", "RabbitMQ")
    web_frameworks: Tuple[str, ...] = ("FastAPI", "Django", "React")
    misc: Tuple[str, ...] = ("Docker", "Docker Compose", "Celery")
    ongoing  : Tuple[str, ...] = ("Django", "DRF", "DS and algorithms", "Goolang")

    def jsonify(self) -> str:
        return json.dumps(asdict(self), indent=4)

hanabiraa_stack = Hanabiraa()
print(hanabiraa_stack.jsonify())
```

***

## Repo structure :
> notes-way - to summarize theoretical material, such as what is threads and concurrency or n + 1 problem problem

> python-way - to study algorithms and data structures, as well as tasks and interesting features of syntax

> django-way - to study Django, DRF
 
> fastAPI-way - to study FastAPI, Celery with fastAPI and etc

> frontend-way - to study on beginning level html/css, js and other frontend  frameworks

> sql-way - to study SQL syntax/dialects and various DBMS (Database Management System)

> Certificates - for certificates from various courses / hackathons and others

***
## What I have already learned and what I am studying:
> ### Python
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepik](https://stepik.org/course/67/promo) |Программирование на Python| **Completed** |
| [Stepik](https://stepik.org/course/512/promo) | Python: основы и применение | **Completed** |
| [Coursera](https://www.coursera.org/learn/mathematics-and-python)|Математика и Python для анализа данных| **Completed** |
| [Kaggle](https://www.kaggle.com/learn/python) | Python | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/pandas) | Pandas | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-visualization) | Data Visualization | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-cleaning) | Data Cleaning | **Completed** |
| [testdriven.io](https://testdriven.io/blog/fastapi-react/) | Developing a Single Page App with FastAPI and React | **Completed** |
| [testdriven.io](https://testdriven.io/courses/fastapi-celery/intro/) | The Definitive Guide to Celery and FastAPI | **Completed** |
#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| Изучаем Python. Том 1 | Лутц Марк | **Completed** |
| Изучаем Python. Том 2 | Лутц Марк | **Completed** |
| Django for beginners | William Vincent | **Completed** |
| [The Ultimate FastAPI Tutorial](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/) | Christopher Samiullah | **Completed** |
| [How to use server-sent events (SSE) with FastAPI?](https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi) | Bobby Iliev | **Completed** |
| Lightweight Django using REST, websockets & backbone | Julia Elman & Mark Lavin | To Do |

> ### Algorithms & Data Structures
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepik](https://stepik.org/course/217/promo) |Алгоритмы: теория и практика. Методы| To Do |
| [Stepik](https://stepik.org/course/1547/promo) | Алгоритмы: теория и практика. Структуры данных | To Do |

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| [DS & Algorithms (Online book)](https://www.programiz.com/dsa) | Programiz | **Completed** |
| Грокаем алгоритмы | Бхаргава Адитья | **Completed** |
| Алгоритмы. Руководство по разработке | Стивен Скиена | To Do |

> ### SQL

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| PostgreSQL. Основы языка SQL | Е.П. Моргунов | **Completed**  |

> ### Other

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| [html & css is hard](https://www.internetingishard.com/html-and-css/)| Oliver James | **Completed** |
| [Tutorial: Intro to React](https://reactjs.org/tutorial/tutorial.html#before-we-start-the-tutorial) | React official docs | **Completed** |
| [Docker for beginners](https://testdriven.io/blog/docker-for-beginners/) | [testdriven.io user](https://testdriven.io/authors/girllovestocode/) | **Completed** |
| [Try docker-compose](https://docs.docker.com/compose/gettingstarted/) | Official docker docs | **Completed** |
| [Docker best practices](https://testdriven.io/blog/docker-best-practices/) | [testdriven.io user](https://testdriven.io/authors/shaji/) | **Completed** |
