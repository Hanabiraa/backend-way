# ???????????? My backend-way ????????????

## Repository where I learn django, python and and follow these roadmaps: 
### 1) [Backend roadmap](https://roadmap.sh/backend)
### 2) [Python roadmap](https://roadmap.sh/python)

***

<!-- Zero width character is used to put extra blank lines before and after code -->
<h3>

```python
???
from __future__ import annotations

import json
from dataclasses import asdict, dataclass


@dataclass
class FutureStack:
    languages: tuple[str, ...] = ("Python", "HTML5", "CSS")
    databases: tuple[str, ...] = ("PostgreSQL")
    misc     : tuple[str, ...] = ("Docker")
    ongoing  : tuple[str, ...] = ("Django", "DRF")

    def jsonify(self) -> str:
        return json.dumps(asdict(self), indent=4)


stack = FutureStack()
print(stack.jsonify())
???
```
</h3>

***

## Repo structure :
> notes-way - to summarize theoretical material, such as what is threads and concurrency or n + 1 problem problem

> python-way - to study algorithms and data structures, as well as tasks and interesting features of syntax

> frontend-way - to study on beginning level html/css, js and other frontend  frameworks

> sql-way - to study SQL syntax/dialects and various DBMS (Database Management System)

> Certificates - for certificates from various courses / hackathons and others

***
## What I have already learned and what I am studying:
> ### Python
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepic](https://stepik.org/course/67/promo) |????郋迣??訄邾邾邽??郋赲訄郇邽迮 郇訄 Python| **Completed** |
| [Stepic](https://stepik.org/course/512/promo) | Python: 郋??郇郋赲?? 邽 郈??邽邾迮郇迮郇邽迮 | **Completed** |
| [Coursera](https://www.coursera.org/learn/mathematics-and-python)|??訄??迮邾訄??邽郕訄 邽 Python 迡郅?? 訄郇訄郅邽郱訄 迡訄郇郇????| **Completed** |
| [Kaggle](https://www.kaggle.com/learn/python) | Python | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/pandas) | Pandas | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-visualization) | Data Visualization | **Completed** |
| [Kaggle](https://www.kaggle.com/learn/data-cleaning) | Data Cleaning | **Completed** |

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| ??郱????訄迮邾 Python. 苠郋邾 1 | ???????? ??訄??郕| **Completed** |
| ??郱????訄迮邾 Python. 苠郋邾 2 | ???????? ??訄??郕| **Completed** |


> ### Algorithms & Data Structures
#### Courses
| URL | Title | Status |
| :---: | --- | :---: |
| [Stepic](https://stepik.org/course/217/promo) |??郅迣郋??邽??邾??: ??迮郋??邽?? 邽 郈??訄郕??邽郕訄. ??迮??郋迡??| To Do |
| [Stepic](https://stepik.org/course/1547/promo) | ??郅迣郋??邽??邾??: ??迮郋??邽?? 邽 郈??訄郕??邽郕訄. 苤??????郕???????? 迡訄郇郇???? | To Do |

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| [DS & Algorithms (Online book)](https://www.programiz.com/dsa) | Programiz | To Do |
| ????郋郕訄迮邾 訄郅迣郋??邽??邾?? | ????訄??迣訄赲訄 ??迡邽?????? | **Completed** |
| ??郅迣郋??邽??邾??. ????郕郋赲郋迡????赲郋 郈郋 ??訄郱??訄訇郋??郕迮 | 苤??邽赲迮郇 苤郕邽迮郇訄 | To Do |

> ### SQL

#### Books
| Title | Author | Status |
| --- | :---: | :---: |
| PostgreSQL. ????郇郋赲?? ??郱??郕訄 SQL | ??.??. ??郋??迣??郇郋赲 | To Do  |

> ### Other

#### Books (Coming soon)
| Title | Author | Status |
| --- | :---: | :---: |
| [html & css is hard](https://www.internetingishard.com/html-and-css/)| Oliver James | **Completed** |
