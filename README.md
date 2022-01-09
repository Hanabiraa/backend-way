# 🤖🤖🤖 My backend-way 🤖🤖🤖

## Repository where I learn django, python and and follow these roadmaps: 
### 1) [Backend roadmap](https://roadmap.sh/backend)
### 2) [Python roadmap](https://roadmap.sh/python)

***

<!-- Zero width character is used to put extra blank lines before and after code -->
<h3>

```python
​
from __future__ import annotations

import json
from dataclasses import asdict, dataclass


@dataclass
class FutureStack:
    languages: tuple[str, ...] = ("Python")
    databases: tuple[str, ...] = ("SQLite", "PostgreSQL", "Redis")
    misc     : tuple[str, ...] = ("Docker")
    ongoing  : tuple[str, ...] = ("Django", "DRF", "asyncio", "aiohttp")

    def jsonify(self) -> str:
        return json.dumps(asdict(self), indent=4)


stack = FutureStack()
print(stack.jsonify())
​
```
</h3>

***

## Repo structure :
> notes-way - to summarize theoretical material, such as what is threads and concurrency or n + 1 problem problem

> python-way - to study algorithms and data structures, as well as tasks and interesting features of syntax

> Certificates - for certificates from various courses / hackathons and others

***
## What I have already learned and what I am studying:
> ### Python
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepic](https://stepik.org/course/67/promo) |Программирование на Python| **Completed** |
| [Stepic](https://stepik.org/course/512/promo) | Python: основы и применение | To Do |
| [Coursera](https://www.coursera.org/learn/mathematics-and-python)|Математика и Python для анализа данных| **Completed** |
| [Kaggle](https://www.kaggle.com/learn/python) | Python | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/pandas) | Pandas | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-visualization) | Data Visualization | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-cleaning) | Data Cleaning | **Completed** |

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| Изучаем Python. Том 1 | Лутц Марк| **Completed** |
| Изучаем Python. Том 2 | Лутц Марк | To Do |


> ### Algorithms & Data Structures
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepic](https://stepik.org/course/217/promo) |Алгоритмы: теория и практика. Методы| To Do |
| [Stepic](https://stepik.org/course/1547/promo) | Алгоритмы: теория и практика. Структуры данных | To Do |

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| Грокаем алгоритмы | Бхаргава Адитья | To Do |
| Изучаем Python. Том 2 | Лутц Марко | To Do |

> ### SQL
#### Courses (Coming soon)
| URL | Title | Status |
| :---: | --- | :---: |
|||

#### Books (Coming soon)
| Title | Author | Status |
| --- | :---: | :---: |
| |

> ### Soft Skills
#### Courses (Coming soon)
| URL | Title | Status |
| :---: | --- | :---: |
|||

#### Books (Coming soon)
| Title | Author | Status |
| --- | :---: | :---: |
| |
